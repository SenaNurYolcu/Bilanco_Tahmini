"""
parse_and_build_dataset.py
==========================
Bilanco_Tahmini reposundaki (docs/model_oncesi/degiskenler.json ve DEGISKEN_LISTESI.md)
veri sozlesmesine uygun olarak:
1. data/kap_raw_xls/ altindaki KAP finansal rapor dosyalarini (2010-2015 BIFF8 .xls ve
   2016-2020 HTML .xls formatlarini) ayristirir.
2. Her sirket-ceyrek icin birim (TL / 1.000 TL / Bin TL / Milyon TL) normalizasyonu yaparak tum
   parasal kalemleri tam TL (TRY) cinsine cevirir.
3. Yillik kumulatif (YTD) gelir ve nakit akisi kalemlerinden tek ceyreklik (3 aylik)
   akislari (Q1 = YTD_Q1, Q2 = 3Aylik veya YTD_Q2 - YTD_Q1, Q3 = 3Aylik veya YTD_Q3 - YTD_Q2,
   Q4 = YTD_Q4 - YTD_Q3) turetir.
4. Kaynak, birim, rapor surumu ve eksik nedenlerini korur. Ayni donemin
   finansal tutarlari hedef verisidir; otomatik olarak model girdisi sayilmaz.
5. Guncel makro snapshotini tarihsel vintage olarak sunmaz.
"""

from __future__ import annotations

import html
import json
import math
import re
import hashlib
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from fetch_kap_financials_2010_2020 import SELECTED_COMPANIES

ROOT_DIR = Path(__file__).resolve().parent.parent
KAP_RAW_DIR = ROOT_DIR / "data" / "kap_raw_xls"
EXTERNAL_DIR = ROOT_DIR / "data" / "external"
OUTPUT_CSV = ROOT_DIR / "data" / "bist_bilanco_tahmini_2010_2020.csv"

QUARTER_END_DATES = {
    1: "03-31",
    2: "06-30",
    3: "09-30",
    4: "12-31",
}


def normalize_tr(text: Any) -> str:
    """Türkçe metinleri karşılaştırma için küçük harfe ve standart ASCII karakterlere indirger."""
    if text is None or (isinstance(text, float) and math.isnan(text)):
        return ""
    s = str(text).strip()
    s = s.replace("İ", "i").replace("I", "ı")
    s = s.lower()
    tr_map = str.maketrans("çğıöşüâîû", "cgiosuaiu")
    s = s.translate(tr_map)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def parse_number(val: Any) -> float | None:
    """KAP tablolarındaki sayısal hücreleri float'a çevirir. Boş hücreler None döner (0 değil)."""
    if val is None:
        return None
    if isinstance(val, (int, float)):
        if math.isnan(val) or math.isinf(val):
            return None
        return float(val)
    s = str(val).strip()
    if not s or s in ("-", "--", "nan", "None", "null"):
        return None
    if re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", s):
        return None
    neg = False
    if s.startswith("(") and s.endswith(")"):
        neg = True
        s = s[1:-1].strip()
    if "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s:
        s = s.replace(",", ".")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    elif "." in s:
        parts = s.split(".")
        if (
            len(parts) == 2
            and len(parts[1]) == 3
            and len(parts[0]) >= 1
            and parts[0].lstrip("-").isdigit()
            and parts[1].isdigit()
        ):
            s = s.replace(".", "")
    # Metin/dipnot ve tarihleri sayisal veri diye birlestirmeyin.
    if not re.fullmatch(r"-?\d+(?:\.\d+)?", s):
        return None
    if not s or s == "-" or s == ".":
        return None
    try:
        res = float(s)
        return -abs(res) if neg else res
    except ValueError:
        return None


def detect_unit_multiplier(unit_str: str) -> tuple[str, float]:
    """Raporlama birimini (TL, 1.000 TL, Bin TL, Milyon TL) tespit eder ve TL çarpanını döndürür."""
    u_raw = (unit_str or "").strip()
    u = normalize_tr(u_raw)
    if not u:
        return "unknown", float("nan")
    if "milyon" in u or "1.000.000" in u or "1000000" in u:
        return u_raw, 1_000_000.0
    if "1.000" in u or "1000" in u or "bin" in u or "1,000" in u:
        return u_raw, 1_000.0
    if u in ("tl", "try", "turk lirasi"):
        return u_raw, 1.0
    return u_raw, float("nan")


def extract_rows_from_biff8(file_path: Path) -> tuple[dict[str, str], list[tuple[str, float | None, float | None]]]:
    """2010-2015 BIFF8 (.xls) dosyasından üstbilgileri ve (etiket, cari_donem, cari_3aylik) satırlarını çıkarır."""
    df = pd.read_excel(file_path, header=None, engine="xlrd")
    meta = {
        "consolidation": "",
        "original_unit": "",
        "published_at_header": "",
    }
    rows: list[tuple[str, float | None, float | None]] = []

    col_ytd = 2
    col_3m: int | None = 4

    for _, r in df.iterrows():
        c0 = str(r[0]).strip() if pd.notna(r[0]) else ""
        c0_norm = normalize_tr(c0)

        # Dinamik sütun başlığı kontrolü ('Cari Dönem' ve 'Cari Dönem 3 Aylık' hangi sütunda?)
        row_norms = [normalize_tr(r[j]) if j < len(r) and pd.notna(r[j]) else "" for j in range(min(8, len(r)))]
        if any(rn == "cari donem" or rn.startswith("cari donem ") for rn in row_norms[1:]):
            found_ytd = None
            found_3m = None
            for j in range(1, len(row_norms)):
                rn = row_norms[j]
                if rn == "cari donem" and found_ytd is None:
                    found_ytd = j
                elif ("3 aylik" in rn or "uc aylik" in rn) and "cari" in rn and found_3m is None:
                    found_3m = j
            if found_ytd is not None:
                col_ytd = found_ytd
                col_3m = found_3m
            continue

        if not c0:
            continue

        # Üstbilgi satırı: "ASELSAN ... / ASELS , 2010/9 Aylık [] 12.11.2010 11:35:43"
        if not meta["published_at_header"] and ("[]" in c0 or "[" in c0):
            m = re.search(r"\]\s*(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})", c0)
            if m:
                d_str = m.group(1)
                pts = d_str.split()
                d_parts = pts[0].split(".")
                meta["published_at_header"] = f"{d_parts[2]}-{d_parts[1]}-{d_parts[0]} {pts[1]}"

        if c0_norm == "finansal tablo turu":
            for j in range(1, min(6, len(r))):
                if pd.notna(r[j]) and str(r[j]).strip():
                    if not meta["consolidation"]:
                        meta["consolidation"] = str(r[j]).strip()
                    break
            continue
        if c0_norm == "raporlama birimi":
            for j in range(1, min(6, len(r))):
                if pd.notna(r[j]) and str(r[j]).strip():
                    u_cand = str(r[j]).strip()
                    if not meta["original_unit"] and u_cand:
                        meta["original_unit"] = u_cand
                    break
            continue

        c_ytd_raw = r[col_ytd] if col_ytd < len(r) else None
        c_3m_raw = r[col_3m] if (col_3m is not None and col_3m < len(r)) else None

        val_ytd = parse_number(c_ytd_raw)
        val_3m = parse_number(c_3m_raw)

        rows.append((c0, val_ytd, val_3m))

    return meta, rows


# Hızlı derlenmiş regex kalıpları (2016-2020 HTML .xls dosyaları için)
RE_UNIT = re.compile(r"Sunum Para Birimi\s*</td>\s*<td[^>]*>\s*([^<]+)", re.I | re.S)
RE_CONS = re.compile(r"Finansal Tablo Niteli[^\s<]*\s*</td>\s*<td[^>]*>\s*([^<]+)", re.I | re.S)
RE_LABEL_TR = re.compile(r'content-tr"[^>]*>\s*([^<]+)', re.I | re.S)
RE_CTX_CELL = re.compile(r'<td\s+class="taxonomy-context-value[^"]*"[^>]*>(.*?)</td>', re.I | re.S)
RE_TITLE_VAL = re.compile(r'title="([^"]+)"', re.I | re.S)
RE_INNER_TEXT = re.compile(r"<[^>]+>")


def extract_rows_from_html_xls(file_path: Path) -> tuple[dict[str, str], list[tuple[str, float | None, float | None]]]:
    """2016-2020 HTML tabanlı (.xls) dosyasından üstbilgileri ve (etiket, cari_donem, cari_3aylik) satırlarını hızla çıkarır."""
    html_text = file_path.read_bytes().decode("utf-8", errors="ignore")

    meta = {
        "consolidation": "",
        "original_unit": "",
        "published_at_header": "",
    }
    m_unit = RE_UNIT.search(html_text[:15000])
    if m_unit:
        meta["original_unit"] = html.unescape(m_unit.group(1)).strip()
    m_cons = RE_CONS.search(html_text[:15000])
    if m_cons:
        meta["consolidation"] = html.unescape(m_cons.group(1)).strip()

    rows: list[tuple[str, float | None, float | None]] = []
    chunks = html_text.split('<tr class="')
    last_role = ""

    for ch in chunks[1:]:
        head_part = ch[:140]
        if "presentation-disabled" in head_part:
            continue
        if "presentation-enabled" not in head_part:
            continue

        # Tablo rol kodunu kontrol et (general_role_210... = BS, 310... = IS, 510.../520... = CF, 610... = EQ)
        m_role = re.search(r"general_role_(\d{3})", head_part)
        if m_role:
            role_prefix = m_role.group(1)
            if role_prefix != last_role:
                last_role = role_prefix
                if role_prefix.startswith("21"):
                    rows.append(("Finansal Durum Tablosu", None, None))
                elif role_prefix.startswith("31") or role_prefix.startswith("32"):
                    rows.append(("Gelir Tablosu", None, None))
                elif role_prefix.startswith("51") or role_prefix.startswith("52"):
                    rows.append(("Nakit Akış Tablosu", None, None))
                elif role_prefix.startswith("61"):
                    rows.append(("Özkaynak Değişim Tablosu", None, None))

        m_lbl = RE_LABEL_TR.search(ch)
        if not m_lbl:
            continue
        label = html.unescape(m_lbl.group(1)).strip()
        if not label:
            continue

        ctx_cells = RE_CTX_CELL.findall(ch)
        parsed_vals: list[float | None] = []
        for cell_html in ctx_cells:
            m_t = RE_TITLE_VAL.search(cell_html)
            if m_t:
                # HTML title is a machine number, not Turkish formatted display.
                try:
                    value = float(m_t.group(1))
                    parsed_vals.append(value if math.isfinite(value) else None)
                except ValueError:
                    parsed_vals.append(None)
            else:
                txt_val = html.unescape(RE_INNER_TEXT.sub(" ", cell_html)).strip()
                parsed_vals.append(parse_number(txt_val))

        val_ytd = parsed_vals[0] if len(parsed_vals) >= 1 else None
        val_3m = parsed_vals[2] if len(parsed_vals) >= 3 else None

        rows.append((label, val_ytd, val_3m))

    return meta, rows


def parse_financial_rows(rows: list[tuple[str, float | None, float | None]], mult: float) -> dict[str, float | None]:
    """
    (etiket, cari_ytd, cari_3m) satır listesini Bilanço, Gelir Tablosu ve Nakit Akış
    bölümlerine ayırarak T01-T17 ve F01-F14 kalemlerini tam TL cinsinden döndürür.
    """
    out: dict[str, float | None] = {
        "T01_hasilat_ytd": None,
        "T01_hasilat_3m_raw": None,
        "T02_satislarin_maliyeti_ytd": None,
        "T02_satislarin_maliyeti_3m_raw": None,
        "T03_brut_kar_ytd": None,
        "T03_brut_kar_3m_raw": None,
        "T04_esas_faaliyet_kari_ytd": None,
        "T04_esas_faaliyet_kari_3m_raw": None,
        "T05_finansman_gideri_ytd": None,
        "T05_finansman_gideri_3m_raw": None,
        "F07_finansman_geliri_ytd": None,
        "F07_finansman_geliri_3m_raw": None,
        "T06_vergi_gideri_geliri_ytd": None,
        "T06_vergi_gideri_geliri_3m_raw": None,
        "T07_donem_net_kari_ytd": None,
        "T07_donem_net_kari_3m_raw": None,
        "T07_ana_ortaklik_net_kari_ytd": None,
        "T07_ana_ortaklik_net_kari_3m_raw": None,
        "T08_nakit_ve_nakit_benzerleri": None,
        "F10_kisa_vadeli_ticari_alacaklar": None,
        "F10_uzun_vadeli_ticari_alacaklar": None,
        "T09_ticari_alacaklar": None,
        "T10_stoklar": None,
        "donen_varliklar": None,
        "duran_varliklar": None,
        "T11_toplam_varliklar": None,
        "F13_kisa_vadeli_finansal_borclar": None,
        "F13_uzun_vadeli_finansal_borclar": None,
        "T12_finansal_borclar": None,
        "kisa_vadeli_ticari_borclar": None,
        "uzun_vadeli_ticari_borclar": None,
        "F12_ticari_borclar": None,
        "kisa_vadeli_yukumlulukler": None,
        "uzun_vadeli_yukumlulukler": None,
        "T13_toplam_yukumlulukler": None,
        "T14_toplam_ozkaynaklar": None,
        "T14_ana_ortakliga_ait_ozkaynaklar": None,
        "odenmis_sermaye": None,
        "kap_raporlanan_hbk_ytd": None,
        "T15_isletme_nakit_akisi_ytd": None,
        "T16_yatirim_nakit_akisi_ytd": None,
        "T17_finansman_nakit_akisi_ytd": None,
    }

    def scale(v: float | None) -> float | None:
        return round(v * mult, 2) if v is not None else None

    statement = "BS"
    bs_section = "DONEN"
    cf_section = ""

    kisa_borc_parts: list[float] = []
    uzun_borc_parts: list[float] = []
    alt_cash_parts: list[float] = []
    alt_rev_ytd: float | None = None
    alt_rev_3m: float | None = None
    alt_cogs_ytd: float | None = None
    alt_cogs_3m: float | None = None

    for label, v_ytd, v_3m in rows:
        ln = normalize_tr(label)
        if not ln:
            continue

        # Tablo geçişlerini tespit et (geri dönüşlere de izin ver, örn. TTRAK_2014_Q2 kapak satırları)
        if ln in ("bilanco", "finansal durum tablosu", "finansal durum tablosu (bilanco)", "donen varliklar", "aktif kalemler"):
            statement = "BS"
            bs_section = "DONEN"
            if ln == "donen varliklar" and v_ytd is not None:
                out["donen_varliklar"] = scale(v_ytd)
            continue
        elif ln == "nazim hesaplar":
            statement = "OFF_BS"
            continue
        elif ln in (
            "gelir tablosu",
            "kapsamli gelir tablosu",
            "kar veya zarar ve diger kapsamli gelir tablosu",
            "kar veya zarar tablosu",
            "kar veya zarar kismi",
            "surdurulen faaliyetler",
        ):
            statement = "IS"
            continue
        elif (
            ln in ("nakit akim tablosu", "nakit akis tablosu", "nakit akis tablosu dolayli yontem", "nakit akis tablosu dogrudan yontem")
            or "isletme faaliyetlerine iliskin nakit akimlari" in ln
            or "a. isletme faaliyetlerinden nakit akislari" in ln
            or "a - esas faaliyetlere iliskin nakit akislari" in ln
            or "faaliyetlerden kaynaklanan nakit akimlari" in ln
        ):
            statement = "CF"
            if v_ytd is not None and ("a. isletme" in ln or "isletme faaliyetlerinden nakit akislari" in ln):
                out["T15_isletme_nakit_akisi_ytd"] = scale(v_ytd)
            cf_section = "OP"
            continue
        elif "ozsermaye degisim tablosu" in ln or "ozkaynak degisim tablosu" in ln or "ozkaynaklar degisim tablosu" in ln or "finansal tablo dipnot" in ln:
            statement = "EQ"
            continue

        # ---------------- 1. BİLANÇO (BS) ----------------
        if statement == "BS":
            if ln == "donen varliklar":
                bs_section = "DONEN"
                if v_ytd is not None:
                    out["donen_varliklar"] = scale(v_ytd)
                continue
            elif ln == "toplam donen varliklar":
                if v_ytd is not None:
                    out["donen_varliklar"] = scale(v_ytd)
                bs_section = "DURAN"
                continue
            elif ln == "duran varliklar":
                bs_section = "DURAN"
                if v_ytd is not None:
                    out["duran_varliklar"] = scale(v_ytd)
                continue
            elif ln == "toplam duran varliklar":
                if v_ytd is not None:
                    out["duran_varliklar"] = scale(v_ytd)
                continue
            elif ln in ("toplam varliklar", "toplam aktifler", "aktif toplami"):
                if v_ytd is not None:
                    out["T11_toplam_varliklar"] = scale(v_ytd)
                bs_section = "KISA_YUK"
                continue
            elif ln in ("kisa vadeli yukumlulukler", "pasif kalemler"):
                bs_section = "KISA_YUK"
                if ln == "kisa vadeli yukumlulukler" and v_ytd is not None:
                    out["kisa_vadeli_yukumlulukler"] = scale(v_ytd)
                continue
            elif ln == "toplam kisa vadeli yukumlulukler":
                if v_ytd is not None:
                    out["kisa_vadeli_yukumlulukler"] = scale(v_ytd)
                bs_section = "UZUN_YUK"
                continue
            elif ln == "uzun vadeli yukumlulukler":
                bs_section = "UZUN_YUK"
                if v_ytd is not None:
                    out["uzun_vadeli_yukumlulukler"] = scale(v_ytd)
                continue
            elif ln == "toplam uzun vadeli yukumlulukler":
                if v_ytd is not None:
                    out["uzun_vadeli_yukumlulukler"] = scale(v_ytd)
                continue
            elif ln == "toplam yukumlulukler":
                if v_ytd is not None:
                    out["T13_toplam_yukumlulukler"] = scale(v_ytd)
                bs_section = "OZKAYNAK"
                continue
            elif ln in ("o z k a y n a k l a r", "ozkaynaklar", "toplam ozkaynaklar"):
                bs_section = "OZKAYNAK"
                if v_ytd is not None:
                    out["T14_toplam_ozkaynaklar"] = scale(v_ytd)
                continue
            elif ln == "ana ortakliga ait ozkaynaklar":
                if v_ytd is not None:
                    out["T14_ana_ortakliga_ait_ozkaynaklar"] = scale(v_ytd)
                continue
            elif ln in ("odenmis sermaye", "sermaye") and out["odenmis_sermaye"] is None:
                if v_ytd is not None:
                    out["odenmis_sermaye"] = scale(v_ytd)
                continue

            if bs_section == "DONEN":
                if ln in ("nakit ve benzerleri", "nakit ve nakit benzerleri") and out["T08_nakit_ve_nakit_benzerleri"] is None:
                    out["T08_nakit_ve_nakit_benzerleri"] = scale(v_ytd)
                elif ln in ("nakit degerler", "bankalar") and v_ytd is not None:
                    alt_cash_parts.append(scale(v_ytd))
                elif ln == "ticari alacaklar" and out["F10_kisa_vadeli_ticari_alacaklar"] is None:
                    out["F10_kisa_vadeli_ticari_alacaklar"] = scale(v_ytd)
                elif ln == "stoklar" and out["T10_stoklar"] is None:
                    out["T10_stoklar"] = scale(v_ytd)
            elif bs_section == "DURAN":
                if ln == "ticari alacaklar" and out["F10_uzun_vadeli_ticari_alacaklar"] is None:
                    out["F10_uzun_vadeli_ticari_alacaklar"] = scale(v_ytd)
            elif bs_section == "KISA_YUK":
                if ln in ("finansal borclar", "kisa vadeli borclanmalar", "uzun vadeli borclanmalarin kisa vadeli kisimlari", "alinan krediler"):
                    if v_ytd is not None:
                        kisa_borc_parts.append(scale(v_ytd))
                elif ln == "ticari borclar" and out["kisa_vadeli_ticari_borclar"] is None:
                    out["kisa_vadeli_ticari_borclar"] = scale(v_ytd)
            elif bs_section == "UZUN_YUK":
                if ln in ("finansal borclar", "uzun vadeli borclanmalar"):
                    if v_ytd is not None:
                        uzun_borc_parts.append(scale(v_ytd))
                elif ln == "ticari borclar" and out["uzun_vadeli_ticari_borclar"] is None:
                    out["uzun_vadeli_ticari_borclar"] = scale(v_ytd)

        # ---------------- 2. GELİR TABLOSU (IS) ----------------
        elif statement == "IS":
            if ln in ("satis gelirleri", "hasilat") and out["T01_hasilat_ytd"] is None:
                if v_ytd is not None:
                    out["T01_hasilat_ytd"] = scale(v_ytd)
                    out["T01_hasilat_3m_raw"] = scale(v_3m)
            elif ln in ("finans sektoru faaliyetleri hasilati", "faiz, ucret, prim, komisyon ve diger gelirler", "esas faaliyet gelirleri") and alt_rev_ytd is None:
                if v_ytd is not None:
                    alt_rev_ytd = scale(v_ytd)
                    alt_rev_3m = scale(v_3m)
            elif ln in ("satislarin maliyeti (-)", "satislarin maliyeti") and out["T02_satislarin_maliyeti_ytd"] is None:
                if v_ytd is not None:
                    out["T02_satislarin_maliyeti_ytd"] = scale(v_ytd)
                    out["T02_satislarin_maliyeti_3m_raw"] = scale(v_3m)
            elif ln in ("finans sektoru faaliyetleri maliyeti (-)", "faiz, ucret, prim, komisyon ve diger giderler (-)", "esas faaliyet giderleri (-)") and alt_cogs_ytd is None:
                if v_ytd is not None:
                    alt_cogs_ytd = scale(v_ytd)
                    alt_cogs_3m = scale(v_3m)
            elif ln in ("brut kar/zarar", "brut kar (zarar)", "ticari faaliyetlerden brut kar (zarar)", "ticari faaliyetlerden brut kar/zarar"):
                if out["T03_brut_kar_ytd"] is None or (out["T03_brut_kar_ytd"] == 0 and v_ytd):
                    if v_ytd is not None:
                        out["T03_brut_kar_ytd"] = scale(v_ytd)
                        out["T03_brut_kar_3m_raw"] = scale(v_3m)
            elif ln in ("faaliyet kari/zarari", "esas faaliyet kari/zarari", "esas faaliyet kari (zarari)", "net faaliyet k/z", "esas faaliyet kari veya zarari") and out["T04_esas_faaliyet_kari_ytd"] is None:
                if v_ytd is not None:
                    out["T04_esas_faaliyet_kari_ytd"] = scale(v_ytd)
                    out["T04_esas_faaliyet_kari_3m_raw"] = scale(v_3m)
            elif ln in ("finansal gelirler", "finansman gelirleri", "esas faaliyet disi finansal gelirler") and out["F07_finansman_geliri_ytd"] is None:
                if v_ytd is not None:
                    out["F07_finansman_geliri_ytd"] = scale(v_ytd)
                    out["F07_finansman_geliri_3m_raw"] = scale(v_3m)
            elif ln in ("finansal giderler (-)", "finansman giderleri (-)", "finansman giderleri", "esas faaliyet disi finansal giderler (-)") and out["T05_finansman_gideri_ytd"] is None:
                if v_ytd is not None:
                    out["T05_finansman_gideri_ytd"] = scale(v_ytd)
                    out["T05_finansman_gideri_3m_raw"] = scale(v_3m)
            elif ("surdurulen faaliyetler vergi" in ln or ln == "vergi karsiligi (-)") and not ln.startswith("-") and out["T06_vergi_gideri_geliri_ytd"] is None:
                if v_ytd is not None:
                    out["T06_vergi_gideri_geliri_ytd"] = scale(v_ytd)
                    out["T06_vergi_gideri_geliri_3m_raw"] = scale(v_3m)
            elif ln in (
                "donem kari/zarari",
                "donem kari (zarari)",
                "surdurulen faaliyetler donem kari/zarari",
                "surdurulen faaliyetler donem kari (zarari)",
                "net donem kari/zarari",
                "net donem kari (zarari)",
                "donem net kari veya zarari",
            ):
                if out["T07_donem_net_kari_ytd"] is None or ln in ("donem kari/zarari", "donem kari (zarari)", "donem net kari veya zarari"):
                    if v_ytd is not None:
                        out["T07_donem_net_kari_ytd"] = scale(v_ytd)
                        out["T07_donem_net_kari_3m_raw"] = scale(v_3m)
            elif ln in ("ana ortaklik paylari", "- ana ortaklik paylari") and out["T07_ana_ortaklik_net_kari_ytd"] is None:
                if v_ytd is not None:
                    out["T07_ana_ortaklik_net_kari_ytd"] = scale(v_ytd)
                    out["T07_ana_ortaklik_net_kari_3m_raw"] = scale(v_3m)
            elif ln in (
                "hisse basina kazanc",
                "pay basina kazanc",
                "adi hisse basina kazanc",
                "surdurulen faaliyetlerden pay basina kazanc",
                "- surdurulen faaliyetlerden pay basina kazanc",
                "surdurulen faaliyetlerden hisse basina kazanc",
            ) and out["kap_raporlanan_hbk_ytd"] is None:
                if v_ytd is not None:
                    out["kap_raporlanan_hbk_ytd"] = float(v_ytd)

        # ---------------- 3. NAKİT AKIŞ TABLOSU (CF) ----------------
        elif statement == "CF":
            # 2013-2020 standart satırları:
            if ln.startswith("a. isletme faaliyetlerinden nakit akislari") or ln == "isletme faaliyetlerinden nakit akislari":
                cf_section = "OP"
                if v_ytd is not None:
                    out["T15_isletme_nakit_akisi_ytd"] = scale(v_ytd)
                continue
            elif ln.startswith("b. yatirim faaliyetlerinden") or ln in ("yatirim faaliyetlerinden kaynaklanan nakit akislari", "yatirim faaliyetlerinden nakit akislari"):
                cf_section = "INV"
                if v_ytd is not None:
                    out["T16_yatirim_nakit_akisi_ytd"] = scale(v_ytd)
                continue
            elif ln.startswith("c. finansman faaliyetlerinden") or ln == "finansman faaliyetlerinden nakit akislari":
                cf_section = "FIN"
                if v_ytd is not None:
                    out["T17_finansman_nakit_akisi_ytd"] = scale(v_ytd)
                continue

            # 2010-2012 serbest Nakit Akım Tablosu bölüm geçişleri:
            if (
                "isletme faaliyetlerine iliskin nakit" in ln
                or "faaliyetlerden kaynaklanan nakit" in ln
                or "esas faaliyetlere iliskin nakit" in ln
                or "isletme faaliyetlerinden nakit" in ln
            ) and v_ytd is None:
                cf_section = "OP"
                continue
            elif (
                "yatirim faaliyetlerine iliskin nakit" in ln
                or "yatirim faaliyetlerindeki nakit" in ln
                or "yatirim faaliyetlerinden nakit" in ln
                or "yatirim faaliyetlerinden kaynaklanan nakit" in ln
            ) and v_ytd is None:
                cf_section = "INV"
                continue
            elif (
                "finansman faaliyetlerine iliskin nakit" in ln
                or "finansal faaliyetlerdeki nakit" in ln
                or "finansman faaliyetlerinden nakit" in ln
                or "finansman faaliyetlerinden kaynaklanan nakit" in ln
            ) and v_ytd is None:
                cf_section = "FIN"
                continue
            elif (
                "nakit hareketlerindeki net" in ln
                or "nakit degerlerdeki net" in ln
                or "nakit ve nakit benzeri degerlerdeki net" in ln
                or "nakit ve nakit benzerlerindeki net" in ln
                or "nakit ve benzerlerindeki net" in ln
                or "yabanci para cevrim farklarinin etkisinden once" in ln
                or "donem basi nakit" in ln
                or "donem basindaki nakit" in ln
            ):
                cf_section = "END"
                continue

            if v_ytd is not None:
                if out["T15_isletme_nakit_akisi_ytd"] is None and (
                    "isletme faaliyetlerinden saglanan" in ln
                    or "isletme faaliyetlerinden elde edilen" in ln
                    or "isletme faaliyetlerinden kullanilan" in ln
                    or "isletme faaliyetlerinden kaynaklanan net" in ln
                    or "esas faaliyetlerden saglanan" in ln
                    or "faaliyetlerden elde edilen net nakit" in ln
                    or "faaliyetlerden saglanan net nakit" in ln
                    or ("faaliyetlerden saglanan" in ln and "nakit" in ln)
                ):
                    out["T15_isletme_nakit_akisi_ytd"] = scale(v_ytd)
                elif out["T16_yatirim_nakit_akisi_ytd"] is None and (
                    "yatirim faaliyetlerinde kullanilan" in ln
                    or "yatirim faaliyetlerinden saglanan" in ln
                    or "yatirim faaliyetlerinde (kullanilan)" in ln
                    or "yatirim faaliyetlerinden elde edilen" in ln
                    or "yatirim faaliyetlerinden kaynaklanan" in ln
                    or "yatirim faaliyetlerinden kullanilan" in ln
                ):
                    out["T16_yatirim_nakit_akisi_ytd"] = scale(v_ytd)
                elif out["T17_finansman_nakit_akisi_ytd"] is None and (
                    "finansman faaliyetlerinden saglanan" in ln
                    or "finansman faaliyetlerinde kullanilan" in ln
                    or "finansman faaliyetlerinden kullanilan" in ln
                    or "finansman faaliyetlerinden elde edilen" in ln
                    or "finansman faaliyetlerinden kaynaklanan" in ln
                    or "finansal faaliyetlerde kullanilan" in ln
                    or "finansal faaliyetlerden saglanan" in ln
                    or "finansal faaliyetlerden kullanilan" in ln
                    or "finansman faaliyetlerinden (kullanilan)" in ln
                ):
                    out["T17_finansman_nakit_akisi_ytd"] = scale(v_ytd)

    # Hasılat yedeği (GSDDE 2010-2013 gibi esas faaliyet geliri üst satırda yer alanlar için)
    if out["T01_hasilat_ytd"] is None and alt_rev_ytd is not None:
        out["T01_hasilat_ytd"] = alt_rev_ytd
        out["T01_hasilat_3m_raw"] = alt_rev_3m
    if out["T02_satislarin_maliyeti_ytd"] is None and alt_cogs_ytd is not None:
        out["T02_satislarin_maliyeti_ytd"] = alt_cogs_ytd
        out["T02_satislarin_maliyeti_3m_raw"] = alt_cogs_3m

    # Bilanço türetilmiş toplam kontrolü:
    if out["T08_nakit_ve_nakit_benzerleri"] is None and alt_cash_parts:
        out["T08_nakit_ve_nakit_benzerleri"] = round(sum(alt_cash_parts), 2)
    if out["F10_kisa_vadeli_ticari_alacaklar"] is not None and out["F10_uzun_vadeli_ticari_alacaklar"] is not None:
        out["T09_ticari_alacaklar"] = round(
            (out["F10_kisa_vadeli_ticari_alacaklar"] or 0.0) + (out["F10_uzun_vadeli_ticari_alacaklar"] or 0.0), 2
        )
    if kisa_borc_parts:
        out["F13_kisa_vadeli_finansal_borclar"] = round(sum(kisa_borc_parts), 2)
    if uzun_borc_parts:
        out["F13_uzun_vadeli_finansal_borclar"] = round(sum(uzun_borc_parts), 2)
    if out["F13_kisa_vadeli_finansal_borclar"] is not None and out["F13_uzun_vadeli_finansal_borclar"] is not None:
        out["T12_finansal_borclar"] = round(
            (out["F13_kisa_vadeli_finansal_borclar"] or 0.0) + (out["F13_uzun_vadeli_finansal_borclar"] or 0.0), 2
        )
    if out["kisa_vadeli_ticari_borclar"] is not None and out["uzun_vadeli_ticari_borclar"] is not None:
        out["F12_ticari_borclar"] = round(
            (out["kisa_vadeli_ticari_borclar"] or 0.0) + (out["uzun_vadeli_ticari_borclar"] or 0.0), 2
        )
    if out["T11_toplam_varliklar"] is None:
        if out["donen_varliklar"] is not None and out["duran_varliklar"] is not None:
            out["T11_toplam_varliklar"] = round(out["donen_varliklar"] + out["duran_varliklar"], 2)
    if out["T13_toplam_yukumlulukler"] is None:
        if out["kisa_vadeli_yukumlulukler"] is not None and out["uzun_vadeli_yukumlulukler"] is not None:
            out["T13_toplam_yukumlulukler"] = round(
                (out["kisa_vadeli_yukumlulukler"] or 0.0) + (out["uzun_vadeli_yukumlulukler"] or 0.0), 2
            )
        elif out["T11_toplam_varliklar"] is not None and out["T14_toplam_ozkaynaklar"] is not None:
            out["T13_toplam_yukumlulukler"] = round(out["T11_toplam_varliklar"] - out["T14_toplam_ozkaynaklar"], 2)
    if out["T03_brut_kar_ytd"] is None and out["T01_hasilat_ytd"] is not None and out["T02_satislarin_maliyeti_ytd"] is not None:
        out["T03_brut_kar_ytd"] = round(out["T01_hasilat_ytd"] + out["T02_satislarin_maliyeti_ytd"], 2)
        if out["T01_hasilat_3m_raw"] is not None and out["T02_satislarin_maliyeti_3m_raw"] is not None:
            out["T03_brut_kar_3m_raw"] = round(out["T01_hasilat_3m_raw"] + out["T02_satislarin_maliyeti_3m_raw"], 2)
    return out


def load_catalog_dates() -> tuple[dict[tuple[str, int, int], tuple[str, str]], dict[str, str]]:
    """
    data/kap_fr_catalog_2010_2020.json dosyasından:
    1) (ticker, year, quarter) -> (first_published_at, disclosure_index)
    2) disclosure_index -> first_published_at
    sözlüklerini oluşturur.
    """
    cat_path = ROOT_DIR / "data" / "kap_fr_catalog_2010_2020.json"
    if not cat_path.is_file():
        return {}, {}
    data = json.loads(cat_path.read_text(encoding="utf-8"))
    disclosures = data.get("disclosures", [])
    donem_map = {
        "3 Aylık": 1,
        "03 Aylık": 1,
        "1. Çeyrek": 1,
        "6 Aylık": 2,
        "06 Aylık": 2,
        "2. Çeyrek": 2,
        "9 Aylık": 3,
        "09 Aylık": 3,
        "3. Çeyrek": 3,
        "Yıllık": 4,
        "12 Aylık": 4,
        "4. Çeyrek": 4,
    }
    alias_map = {"KRDMA": "KRDMD", "KRDMB": "KRDMD", "KRDMD": "KRDMD"}
    result: dict[tuple[str, int, int], tuple[str, str]] = {}
    by_disc_idx: dict[str, str] = {}

    for d in disclosures:
        basic = d.get("disclosureBasic", d)
        pub_raw = (basic.get("publishDate") or "").strip()
        pub_iso = pub_raw
        m_dt = re.match(r"^(\d{2})\.(\d{2})\.(\d{4})\s+(\d{2}:\d{2}(?::\d{2})?)$", pub_raw)
        if m_dt:
            t_part = m_dt.group(4) if len(m_dt.group(4)) == 8 else f"{m_dt.group(4)}:00"
            pub_iso = f"{m_dt.group(3)}-{m_dt.group(2)}-{m_dt.group(1)} {t_part}"
        disc_idx = str(basic.get("disclosureIndex") or "")
        if disc_idx and pub_iso:
            by_disc_idx[disc_idx] = pub_iso

        codes = [c.strip() for c in re.split(r"[, \-]+", basic.get("stockCodes") or basic.get("stockCode") or "") if c.strip()]
        matched_t = None
        for c in codes:
            m = alias_map.get(c, c)
            if m in SELECTED_COMPANIES:
                matched_t = m
                break
        if not matched_t:
            continue
        yr = basic.get("year")
        q = basic.get("period")
        if not q:
            donem = (basic.get("ruleType") or basic.get("ruleTypeTerm") or basic.get("donem") or "").strip()
            q = donem_map.get(donem)
        if not yr or not q or int(q) not in (1, 2, 3, 4):
            continue
        key = (matched_t, int(yr), int(q))
        if key not in result or (pub_iso and pub_iso < result[key][0]):
            result[key] = (pub_iso, disc_idx)
    return result, by_disc_idx


def build_dataset() -> pd.DataFrame:
    """Compatibility entry point; returns a financial snapshot, not model inputs."""
    from rebuild_dataset import build_financial_snapshot
    return build_financial_snapshot()[0]


if __name__ == "__main__":
    from rebuild_dataset import run
    run()
