"""
fetch_kap_financials_2010_2020.py
=================================
Bilanco_Tahmini reposundaki (docs/model_oncesi/degiskenler.json ve DEGISKEN_LISTESI.md)
kurallara uygun olarak KAP'tan 2010-2020 yillari arasindaki (44 ceyrek) finansal raporlari
ceker ve secilen 6 farkli sektordeki 5'er sirketin (toplam 30 BIST sirketi) tablo verilerini
data/kap_raw_xls/ altina Arsivler.

Ayrica KAP /tr/api/disclosure/members/byCriteria servisi uzerinden her sirket-ceyrek
finansal raporunun ilk kamuya aciklanma tarihini (first_published_at) ve bildirim
numarasini (disclosure_index) dogrular.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import io
import json
import re
import shutil
import subprocess
import tempfile
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
KAP_RAW_DIR = ROOT_DIR / "data" / "kap_raw_xls"
KAP_ZIPS_DIR = ROOT_DIR / "data" / "kap_zips"
KAP_RAW_DIR.mkdir(parents=True, exist_ok=True)
KAP_ZIPS_DIR.mkdir(parents=True, exist_ok=True)

# 6 Farkli Sektorden 5'er Sirket (Toplam 30 Sirket)
SELECTED_COMPANIES = {
    # 1. Teknoloji ve Savunma (TEKNOLOJİ)
    "ASELS": {
        "sector_group": "Teknoloji ve Savunma",
        "kap_main_sector": "TEKNOLOJİ",
        "kap_sub_sector": "SAVUNMA",
        "title": "ASELSAN ELEKTRONİK SANAYİ VE TİCARET A.Ş.",
        "mkkMemberOid": "4028e4a1413b7ef401413bc2251e0047",
    },
    "LOGO": {
        "sector_group": "Teknoloji ve Savunma",
        "kap_main_sector": "TEKNOLOJİ",
        "kap_sub_sector": "BİLİŞİM",
        "title": "LOGO YAZILIM SANAYİ VE TİCARET A.Ş.",
        "mkkMemberOid": "4028e4a14158e41e01415b41210a6e8c",
    },
    "NETAS": {
        "sector_group": "Teknoloji ve Savunma",
        "kap_main_sector": "TEKNOLOJİ",
        "kap_sub_sector": "BİLİŞİM",
        "title": "NETAŞ TELEKOMÜNİKASYON A.Ş.",
        "mkkMemberOid": "4028e4a240f2ef47014111d7df220232",
    },
    "ALCTL": {
        "sector_group": "Teknoloji ve Savunma",
        "kap_main_sector": "TEKNOLOJİ",
        "kap_sub_sector": "BİLİŞİM",
        "title": "ALCATEL LUCENT TELETAŞ TELEKOMÜNİKASYON A.Ş.",
        "mkkMemberOid": "4028e4a140f2ed71014110e38acb01b5",
    },
    "KAREL": {
        "sector_group": "Teknoloji ve Savunma",
        "kap_main_sector": "TEKNOLOJİ",
        "kap_sub_sector": "BİLİŞİM",
        "title": "KAREL ELEKTRONİK SANAYİ VE TİCARET A.Ş.",
        "mkkMemberOid": "4028e4a246b4c5a90147d42c754a6bba",
    },
    # 2. Enerji ve Rafineri (ELEKTRİK GAZ VE SU / RAFİNERİ)
    "TUPRS": {
        "sector_group": "Enerji ve Rafineri",
        "kap_main_sector": "İMALAT",
        "kap_sub_sector": "KİMYA İLAÇ PETROL LASTİK VE PLASTİK ÜRÜNLER",
        "title": "TÜPRAŞ-TÜRKİYE PETROL RAFİNERİLERİ A.Ş.",
        "mkkMemberOid": "4028e4a140f2ed720140f37f139c01bc",
    },
    "AYGAZ": {
        "sector_group": "Enerji ve Rafineri",
        "kap_main_sector": "İMALAT",
        "kap_sub_sector": "KİMYA İLAÇ PETROL LASTİK VE PLASTİK ÜRÜNLER",
        "title": "AYGAZ A.Ş.",
        "mkkMemberOid": "4028e4a140e95be70140ee03bd6000e0",
    },
    "AKSEN": {
        "sector_group": "Enerji ve Rafineri",
        "kap_main_sector": "ELEKTRİK GAZ VE SU",
        "kap_sub_sector": "ELEKTRİK GAZ VE BUHAR",
        "title": "AKSA ENERJİ ÜRETİM A.Ş.",
        "mkkMemberOid": "4028e4a241733d42014179341a147ddb",
    },
    "ZOREN": {
        "sector_group": "Enerji ve Rafineri",
        "kap_main_sector": "ELEKTRİK GAZ VE SU",
        "kap_sub_sector": "ELEKTRİK GAZ VE BUHAR",
        "title": "ZORLU ENERJİ ELEKTRİK ÜRETİM A.Ş.",
        "mkkMemberOid": "4028e4a140f2ed7201412c19687407a7",
    },
    "AKENR": {
        "sector_group": "Enerji ve Rafineri",
        "kap_main_sector": "ELEKTRİK GAZ VE SU",
        "kap_sub_sector": "ELEKTRİK GAZ VE BUHAR",
        "title": "AKENERJİ ELEKTRİK ÜRETİM A.Ş.",
        "mkkMemberOid": "4028e4a14184e9cf01419bffce0b5a69",
    },
    # 3. Ulaştırma ve Lojistik (ULAŞTIRMA VE DEPOLAMA)
    "THYAO": {
        "sector_group": "Ulaştırma ve Lojistik",
        "kap_main_sector": "ULAŞTIRMA VE DEPOLAMA",
        "kap_sub_sector": "ULAŞTIRMA VE DEPOLAMA",
        "title": "TÜRK HAVA YOLLARI A.O.",
        "mkkMemberOid": "4028e4a140f2ed720140f376bebb01a7",
    },
    "CLEBI": {
        "sector_group": "Ulaştırma ve Lojistik",
        "kap_main_sector": "ULAŞTIRMA VE DEPOLAMA",
        "kap_sub_sector": "ULAŞTIRMA VE DEPOLAMA",
        "title": "ÇELEBİ HAVA SERVİSİ A.Ş.",
        "mkkMemberOid": "4028e4a140ee84900140f1f1584c0015",
    },
    "RYSAS": {
        "sector_group": "Ulaştırma ve Lojistik",
        "kap_main_sector": "ULAŞTIRMA VE DEPOLAMA",
        "kap_sub_sector": "ULAŞTIRMA VE DEPOLAMA",
        "title": "REYSAŞ TAŞIMACILIK VE LOJİSTİK TİCARET A.Ş.",
        "mkkMemberOid": "4028e4a140ee847b0140f203980d0030",
    },
    "GSDDE": {
        "sector_group": "Ulaştırma ve Lojistik",
        "kap_main_sector": "ULAŞTIRMA VE DEPOLAMA",
        "kap_sub_sector": "ULAŞTIRMA VE DEPOLAMA",
        "title": "GSD DENİZCİLİK GAYRİMENKUL İNŞAAT SANAYİ VE TİCARET A.Ş.",
        "mkkMemberOid": "4028e4a140e95be70140ee2a7f39013b",
    },
    "TAVHL": {
        "sector_group": "Ulaştırma ve Lojistik",
        "kap_main_sector": "ULAŞTIRMA VE DEPOLAMA",
        "kap_sub_sector": "ULAŞTIRMA VE DEPOLAMA",
        "title": "TAV HAVALİMANLARI HOLDİNG A.Ş.",
        "mkkMemberOid": "4028e4a140f2ed720140f31195ef010e",
    },
    # 4. Otomotiv ve Sanayi (METAL EŞYA MAKİNE ELEKTRİKLİ CİHAZLAR VE ULAŞIM ARAÇLARI)
    "FROTO": {
        "sector_group": "Otomotiv ve Sanayi",
        "kap_main_sector": "İMALAT",
        "kap_sub_sector": "METAL EŞYA MAKİNE ELEKTRİKLİ CİHAZLAR VE ULAŞIM ARAÇLARI",
        "title": "FORD OTOMOTİV SANAYİ A.Ş.",
        "mkkMemberOid": "4028e4a140f2ed71014106890fae0138",
    },
    "TOASO": {
        "sector_group": "Otomotiv ve Sanayi",
        "kap_main_sector": "İMALAT",
        "kap_sub_sector": "METAL EŞYA MAKİNE ELEKTRİKLİ CİHAZLAR VE ULAŞIM ARAÇLARI",
        "title": "TOFAŞ TÜRK OTOMOBİL FABRİKASI A.Ş.",
        "mkkMemberOid": "4028e4a140f2ed710140f328bed700a5",
    },
    "TTRAK": {
        "sector_group": "Otomotiv ve Sanayi",
        "kap_main_sector": "İMALAT",
        "kap_sub_sector": "METAL EŞYA MAKİNE ELEKTRİKLİ CİHAZLAR VE ULAŞIM ARAÇLARI",
        "title": "TÜRK TRAKTÖR VE ZİRAAT MAKİNELERİ A.Ş.",
        "mkkMemberOid": "4028e4a140f2ed710140f340e1f400c3",
    },
    "OTKAR": {
        "sector_group": "Otomotiv ve Sanayi",
        "kap_main_sector": "İMALAT",
        "kap_sub_sector": "METAL EŞYA MAKİNE ELEKTRİKLİ CİHAZLAR VE ULAŞIM ARAÇLARI",
        "title": "OTOKAR OTOMOTİV VE SAVUNMA SANAYİ A.Ş.",
        "mkkMemberOid": "4028e4a140f2ed720140f306b2fb00e2",
    },
    "ARCLK": {
        "sector_group": "Otomotiv ve Sanayi",
        "kap_main_sector": "İMALAT",
        "kap_sub_sector": "METAL EŞYA MAKİNE ELEKTRİKLİ CİHAZLAR VE ULAŞIM ARAÇLARI",
        "title": "ARÇELİK A.Ş.",
        "mkkMemberOid": "4028e4a240e95dc90140ed55b43900cf",
    },
    # 5. Perakende ve Gıda (PERAKENDE TİCARET / GIDA İÇECEK)
    "BIMAS": {
        "sector_group": "Perakende ve Gıda",
        "kap_main_sector": "TOPTAN VE PERAKENDE TİCARET",
        "kap_sub_sector": "PERAKENDE TİCARET",
        "title": "BİM BİRLEŞİK MAĞAZALAR A.Ş.",
        "mkkMemberOid": "4028e4a140e95be70140ee1b7b030119",
    },
    "MGROS": {
        "sector_group": "Perakende ve Gıda",
        "kap_main_sector": "TOPTAN VE PERAKENDE TİCARET",
        "kap_sub_sector": "PERAKENDE TİCARET",
        "title": "MİGROS TİCARET A.Ş.",
        "mkkMemberOid": "4028e4a141462df2014150162e1c3424",
    },
    "ULKER": {
        "sector_group": "Perakende ve Gıda",
        "kap_main_sector": "İMALAT",
        "kap_sub_sector": "GIDA, İÇECEK VE TÜTÜN",
        "title": "ÜLKER BİSKÜVİ SANAYİ A.Ş.",
        "mkkMemberOid": "4028e4a14184e9c901419801438a422b",
    },
    "CCOLA": {
        "sector_group": "Perakende ve Gıda",
        "kap_main_sector": "İMALAT",
        "kap_sub_sector": "GIDA, İÇECEK VE TÜTÜN",
        "title": "COCA-COLA İÇECEK A.Ş.",
        "mkkMemberOid": "4028e4a140ee35c00140ee586bdd0034",
    },
    "AEFES": {
        "sector_group": "Perakende ve Gıda",
        "kap_main_sector": "İMALAT",
        "kap_sub_sector": "GIDA, İÇECEK VE TÜTÜN",
        "title": "ANADOLU EFES BİRACILIK VE MALT SANAYİİ A.Ş.",
        "mkkMemberOid": "4028e4a140e95bea0140ed2fde10009d",
    },
    # 6. Demir-Çelik ve Ana Metal (ANA METAL SANAYİ)
    "EREGL": {
        "sector_group": "Demir-Çelik ve Ana Metal",
        "kap_main_sector": "İMALAT",
        "kap_sub_sector": "ANA METAL SANAYİ",
        "title": "EREĞLİ DEMİR VE ÇELİK FABRİKALARI T.A.Ş.",
        "mkkMemberOid": "4028e4a240e95dc90140ede4c12a0133",
    },
    "KRDMD": {
        "sector_group": "Demir-Çelik ve Ana Metal",
        "kap_main_sector": "İMALAT",
        "kap_sub_sector": "ANA METAL SANAYİ",
        "title": "KARDEMİR KARABÜK DEMİR ÇELİK SANAYİ VE TİCARET A.Ş.",
        "mkkMemberOid": "4028e4a140f2ed7201412ace3ada0707",
    },
    "CEMTS": {
        "sector_group": "Demir-Çelik ve Ana Metal",
        "kap_main_sector": "İMALAT",
        "kap_sub_sector": "ANA METAL SANAYİ",
        "title": "ÇEMTAŞ ÇELİK MAKİNA SANAYİ VE TİCARET A.Ş.",
        "mkkMemberOid": "4028e4a140ee84900140f1f334ce0025",
    },
    "BRSAN": {
        "sector_group": "Demir-Çelik ve Ana Metal",
        "kap_main_sector": "İMALAT",
        "kap_sub_sector": "ANA METAL SANAYİ",
        "title": "BORUSAN BİRLEŞİK BORU FABRİKALARI SANAYİ VE TİCARET A.Ş.",
        "mkkMemberOid": "4028e4a140f2ed7201412ac9ca5d06e6",
    },
    "SARKY": {
        "sector_group": "Demir-Çelik ve Ana Metal",
        "kap_main_sector": "İMALAT",
        "kap_sub_sector": "ANA METAL SANAYİ",
        "title": "SARKUYSAN ELEKTROLİTİK BAKIR SANAYİ VE TİCARET A.Ş.",
        "mkkMemberOid": "4028e4a140f2ed7101410294f924012d",
    },
}


def kap_get_with_retry(url: str, min_sleep: float = 6.5, max_attempts: int = 3) -> bytes:
    """Bound retries and timeouts; a blocked source must not stall an entire rebuild."""
    for attempt in range(max_attempts):
        time.sleep(min_sleep if attempt == 0 else 5.0)
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) BilancoResearch/1.0",
                "Accept-Language": "tr",
                "Referer": "https://www.kap.org.tr/tr/finansal-tablolar",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt + 1 < max_attempts:
                retry_after = e.headers.get("Retry-After")
                wait = min(float(retry_after), 45.0) if (retry_after and retry_after.isdigit()) else 15.0
                print(f"  [HTTP 429] {url} (deneme {attempt+1}/{max_attempts}) -> {wait} sn bekleniyor...", flush=True)
                time.sleep(wait)
                continue
            raise
        except Exception as e:
            if attempt + 1 == max_attempts:
                raise
            time.sleep(10.0)
    raise RuntimeError(f"Failed to download {url}")


def kap_post_with_retry(url: str, body: dict, min_sleep: float = 5.0, max_attempts: int = 3) -> bytes:
    for attempt in range(max_attempts):
        time.sleep(min_sleep if attempt == 0 else 5.0)
        req = urllib.request.Request(
            url,
            data=json.dumps(body).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) BilancoResearch/1.0",
                "Accept-Language": "tr",
                "Referer": "https://www.kap.org.tr/tr/bildirim-sorgu",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt + 1 < max_attempts:
                retry_after = e.headers.get("Retry-After")
                wait = min(float(retry_after), 45.0) if (retry_after and retry_after.isdigit()) else 15.0
                print(f"  [HTTP 429] POST {url} (deneme {attempt+1}/{max_attempts}) -> {wait} sn bekleniyor...", flush=True)
                time.sleep(wait)
                continue
            raise
        except Exception as e:
            if attempt + 1 == max_attempts:
                raise
            time.sleep(10.0)
    raise RuntimeError(f"Failed POST {url}")


def extract_archive_entries(zip_path: Path, raw_bytes: bytes) -> list[tuple[str, bytes]]:
    """Hem standart ZIP hem de KAP'in bazi donemlerde (orn. 2015 Q4) sundugu RAR arsivlerini acar."""
    if not raw_bytes.startswith(b"Rar!"):
        try:
            zf = zipfile.ZipFile(io.BytesIO(raw_bytes))
            entries = [(name, zf.read(name)) for name in zf.namelist() if name.lower().endswith(".xls")]
            if not entries:
                raise ValueError(f"KAP archive contains no XLS files: {zip_path}")
            return entries
        except zipfile.BadZipFile as exc:
            raise ValueError(f"KAP response is not a ZIP/RAR archive: {zip_path}") from exc
    # RAR veya farkli arsiv ise Windows bsdtar (tar.exe) ile gecici klasore ac
    entries: list[tuple[str, bytes]] = []
    tmp_dir = Path(tempfile.mkdtemp(prefix="kap_rar_"))
    try:
        listing = subprocess.run(["tar", "-tf", str(zip_path)], check=True, capture_output=True, text=True)
        for name in listing.stdout.splitlines():
            path = Path(name)
            if path.is_absolute() or ".." in path.parts:
                raise ValueError(f"Unsafe archive member: {name}")
        subprocess.run(["tar", "-xf", str(zip_path), "-C", str(tmp_dir)], check=True, capture_output=True)
        for fp in tmp_dir.rglob("*.xls"):
            entries.append((fp.name, fp.read_bytes()))
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)
    if not entries:
        raise ValueError(f"KAP archive contains no XLS files: {zip_path}")
    return entries


def download_all_quarters(start_year=2010, end_year=2020, quarters=(1, 2, 3, 4)):
    tickers = set(SELECTED_COMPANIES.keys())
    alias_map = {"KRDMA": "KRDMD", "KRDMB": "KRDMD", "KRDMD": "KRDMD"}
    manifest_dir = ROOT_DIR / "data" / "kap_refreshed"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = manifest_dir / f"archive_manifest_{start_year}_{end_year}.json"
    manifest = {"schema_version": "1.0", "archives": [], "files": []}
    for yr in range(start_year, end_year + 1):
        for per in quarters:
            zip_path = KAP_ZIPS_DIR / f"kap_{yr}_Q{per}.zip"
            url = f"https://www.kap.org.tr/tr/api/financialTable/download/{yr}/{per}"
            retrieved_at = None
            if zip_path.is_file() and zip_path.stat().st_size > 1000:
                raw_zip = zip_path.read_bytes()
            else:
                print(f"[KAP ZIP] {yr} Q{per} indiriliyor...", flush=True)
                raw_zip = kap_get_with_retry(url, min_sleep=6.5)
                retrieved_at = datetime.now(timezone.utc).isoformat()
                # Do not cache HTML challenge/error responses as archives.
                if not (raw_zip.startswith(b"PK") or raw_zip.startswith(b"Rar!")):
                    raise ValueError(f"KAP returned a non-archive response: {url}")
                temp_path = zip_path.with_suffix(".part")
                temp_path.write_bytes(raw_zip)
                temp_path.replace(zip_path)

            entries = extract_archive_entries(zip_path, raw_zip)
            manifest["archives"].append({
                "year": yr, "quarter": per, "url": url,
                "sha256": hashlib.sha256(raw_zip).hexdigest(),
                "retrieved_at": retrieved_at,
                "retrieval_mode": "fresh_http" if retrieved_at else "existing_archive_unknown_retrieval_date",
                "vintage_status": "archive_snapshot_not_first_release_proof",
            })
            extracted = 0
            for name, file_bytes in entries:
                # Filename format:
                # 2010-2015: MT_ASELS.xls or MT_KRDMA.xls
                # 2016-2020: ASELS_884518_2020_3.xls or KRDMA, KRDMB, KRDMD_884518_2020_3.xls
                matched_ticker = None
                stem = Path(name).stem
                if stem.startswith("MT_"):
                    code_part = stem[3:]
                    codes = [c.strip() for c in re.split(r"[, \-]+", code_part) if c.strip()]
                    for c in codes:
                        mapped = alias_map.get(c, c)
                        if mapped in tickers:
                            matched_ticker = mapped
                            break
                else:
                    parts = stem.split("_")
                    if len(parts) >= 4 and parts[-2].isdigit() and parts[-1].isdigit():
                        if (int(parts[-2]), int(parts[-1])) != (yr, per):
                            raise ValueError(f"Archive report period mismatch: {name} vs {yr} Q{per}")
                    first_part = parts[0] if parts else ""
                    codes = [c.strip() for c in re.split(r"[, \-]+", first_part) if c.strip()]
                    for c in codes:
                        mapped = alias_map.get(c, c)
                        if mapped in tickers:
                            matched_ticker = mapped
                            break

                if matched_ticker:
                    disc_idx = ""
                    if not stem.startswith("MT_"):
                        parts = stem.split("_")
                        if len(parts) >= 2 and parts[1].isdigit():
                            disc_idx = parts[1]
                    out_file = KAP_RAW_DIR / f"{matched_ticker}_{yr}_Q{per}{('_' + disc_idx) if disc_idx else ''}.xls"
                    if not out_file.is_file():
                        out_file.write_bytes(file_bytes)
                    # Record both digests: preserved files may differ from a newly fetched archive.
                    manifest["files"].append({
                        "ticker": matched_ticker, "year": yr, "quarter": per,
                        "path": str(out_file.relative_to(ROOT_DIR)), "archive_member": name,
                        "source_url": url, "disclosure_index": disc_idx or None,
                        "sha256": hashlib.sha256(out_file.read_bytes()).hexdigest(),
                        "archive_member_sha256": hashlib.sha256(file_bytes).hexdigest(),
                        "matches_archive": out_file.read_bytes() == file_bytes,
                    })
                    extracted += 1
            print(f"  -> {yr} Q{per}: {extracted}/30 sirket dosyasi hazir.", flush=True)
            temp_manifest = manifest_path.with_suffix(".part")
            temp_manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            temp_manifest.replace(manifest_path)


def fetch_publication_dates(start_year=2010, end_year=2020, refresh=False):
    cat_path = ROOT_DIR / "data" / f"kap_fr_catalog_{start_year}_{end_year}.json"
    if cat_path.is_file() and not refresh:
        cached = json.loads(cat_path.read_text(encoding="utf-8"))
        if not isinstance(cached.get("disclosures"), list):
            raise ValueError(f"Invalid cached KAP catalog: {cat_path}")
        print(f"KAP katalogu kullaniliyor (yenilemek icin --refresh-catalog): {cat_path}", flush=True)
        return

    all_oids = [v["mkkMemberOid"] for v in SELECTED_COMPANIES.values()]
    url = "https://www.kap.org.tr/tr/api/disclosure/members/byCriteria"
    all_rows = []
    for yr in range(start_year, end_year + 2):
        to_date = f"{yr}-12-31" if yr <= end_year else f"{yr}-05-31"
        print(f"[KAP Katalog] {yr} sorgulaniyor...", flush=True)
        body = {
            "fromDate": f"{yr}-01-01",
            "toDate": to_date,
            "mkkMemberOidList": all_oids,
            "disclosureClass": "FR",
            "subjectList": [],
        }
        raw = kap_post_with_retry(url, body, min_sleep=6.0)
        rows = json.loads(raw.decode("utf-8"))
        if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
            raise ValueError(f"Invalid KAP catalog response for {yr}")
        all_rows.extend(rows)

    temp_path = cat_path.with_suffix(".part")
    temp_path.write_text(
        json.dumps({"companies": SELECTED_COMPANIES, "disclosures": all_rows}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    temp_path.replace(cat_path)
    print(f"KAP bildirim katalogu kaydedildi: {cat_path} ({len(all_rows)} bildirim)", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="KAP quarterly archive collection; preserves existing raw files.")
    parser.add_argument("--start-year", type=int, default=2010)
    parser.add_argument("--end-year", type=int, default=2020)
    parser.add_argument("--quarters", type=int, nargs="+", choices=(1, 2, 3, 4), default=[1, 2, 3, 4])
    parser.add_argument("--refresh-catalog", action="store_true")
    args = parser.parse_args()
    if args.start_year > args.end_year:
        parser.error("--start-year must be <= --end-year")
    download_all_quarters(args.start_year, args.end_year, args.quarters)
    fetch_publication_dates(args.start_year, args.end_year, args.refresh_catalog)
