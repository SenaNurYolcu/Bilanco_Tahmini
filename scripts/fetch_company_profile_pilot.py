"""Extract a bounded, source-backed company-note pilot from downloaded PDFs.

This is a note extraction pilot, not a complete historical feature panel. Every
record remains excluded from PIT training until its original vintage is proved.
Unresolved source conflicts and gross/net distinctions are retained explicitly.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import re
import unicodedata

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
KEYWORDS = {
    "C02": ["bölümlere göre", "segment", "revenue by", "business segments"],
    "C03": ["yurtdışı satışlar", "ihracat", "export", "foreign sales", "domestic sales"],
    "C04": ["coğrafi", "geographical", "geographic", "country", "countries"],
    "C05": ["müşteri", "customer", "government", "public sector"],
    "C06": ["ithalat", "tedarik", "supplier", "imports", "imported"],
    "C07": ["yakıt", "enerji maliyet", "fuel", "energy cost", "commodity"],
    "C08": ["sabit fiyat", "endeksli fiyat", "fixed price", "indexed", "contract currency"],
    "C09": ["sipariş", "backlog", "order book", "order intake", "take or pay"],
    "C10": ["kapasite", "üretim adedi", "capacity", "sales volume", "unit price"],
    "F19": ["pozisyon", "döviz", "foreign currency", "exchange rate risk"],
    "F20": ["değişken faiz", "vade", "floating", "maturity", "interest rate risk", "hedg"],
}


def norm(text):
    text = text.replace("ı", "i").replace("İ", "i").lower()
    text = "".join(c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", text)


def number(token):
    negative = token.strip().startswith("(") or token.strip().startswith("-")
    value = int(re.sub(r"[^0-9]", "", token))
    return -value if negative else value


def label_pattern(label):
    return r"\s*".join(re.escape(c) for c in norm(label).replace(" ", ""))


def matched_value(text, label):
    match = re.search(label_pattern(label) + r"\s+(\(?-?\d[\d.]*\)?)", norm(text), re.I)
    if not match:
        raise ValueError(f"Label not found: {label}")
    return number(match.group(1)), match.group(0)


def write_csv(path, rows):
    if not rows:
        raise ValueError(f"No records to write: {path}")
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", newline="", encoding="utf-8-sig") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def build_pilot():
    registry = json.loads((ROOT / "docs/model_oncesi/degiskenler.json").read_text())
    definitions = {f["id"]: f for f in registry["features"] if f["id"] in KEYWORDS}
    source_manifest = json.loads((DATA / "kap_refresh_manifest.json").read_text())
    sources, searches, observations = [], [], []
    for source in source_manifest["sources"]:
        if source["status"] != "verified":
            continue
        path = ROOT / source["path"]
        if hashlib.sha256(path.read_bytes()).hexdigest() != source["sha256"]:
            raise ValueError(f"Source digest changed: {path}")
        pages = [p.extract_text() for p in PdfReader(path).pages]
        source_id = f'{source["ticker"]}_{source["year"]}Q{source["quarter"]}'
        common = {
            "entity_id": source["ticker"], "observation_period": f'{source["year"]}Q{source["quarter"]}',
            "source_document_id": source_id, "source_url": source["url"], "source_sha256": source["sha256"],
            "available_at": "", "first_published_at": "", "vintage_status": "unavailable_vintage",
            "training_eligible": False,
        }
        sources.append({**common, "page_count": len(pages), "path": source["path"]})
        for feature_id, keywords in KEYWORDS.items():
            matches = []
            for page_num, text in enumerate(pages, 1):
                normalized = norm(text)
                for keyword in keywords:
                    position = normalized.find(norm(keyword))
                    if position >= 0:
                        matches.append({"page": page_num, "keyword": keyword, "excerpt": normalized[max(0, position - 120):position + 700]})
                        break
            searches.append({
                **common, "feature_id": feature_id, "feature_label": definitions[feature_id]["label"],
                "raw_components": ";".join(definitions[feature_id]["raw_components"]),
                "search_status": "review_required" if matches else "not_extracted",
                "matched_pages": ";".join(str(x["page"]) for x in matches),
                "candidate_excerpts": json.dumps(matches[:5], ensure_ascii=False),
                "missing_reason": "not_extracted",
                "note": "Keyword hits are candidate passages, not validated measures. No hit does not establish not_disclosed.",
            })

        if source_id != "KAREL_2012Q1":
            continue

        def add(feature_id, component, page, label, expected, unit="TRY", note="", status="extracted_snapshot", text=None):
            value, evidence = matched_value(text if text is not None else pages[page - 1], label)
            if value != expected:
                raise ValueError(f"Unexpected source value for {component}: {value}")
            observations.append({
                **common, "feature_id": feature_id, "raw_component": component, "value": value,
                "unit": unit, "pdf_page": page, "page_or_note": f"PDF {page}; printed page {page - 2}",
                "extraction_status": status, "evidence_excerpt": evidence,
                "is_proxy": False, "coverage_ratio": "", "note": note,
            })

        add("C03", "foreign_sales_gross", 48, "Yurtdışı satışlar", 3_623_653,
            note="Gross foreign sales; not export revenue and not comparable to net revenue before allocation of returns/discounts.")
        add("C03", "domestic_sales_gross", 48, "Yurtiçi satışlar", 47_028_827)
        add("C03", "sales_returns", 48, "Satıştan iadeler (-)", -672_653)
        add("C03", "sales_discounts", 48, "Satış iskontoları (-)", -9_256_824)
        add("C03", "other_sales_reductions", 48, "Diğer indirimler (-)", -442_065,
            text=pages[47].replace("ciğer indirim", "Diğer indirim"))

        # A clearly labelled export amount is a separate observation. Its currency
        # breakdown in the same table is inconsistent; do not derive an export share.
        add("C03", "export_amount_reported_tl", 64, "23. İhracat", 3_093_347,
            status="review_required", note="FX note export TL total does not reconcile with the adjacent USD/EUR columns; period basis and currency conversion require source review. Separate from gross foreign sales.")
        add("C06", "import_amount_reported_tl", 64, "24. İthalat", 8_053_195,
            status="review_required", note="Import flow amount; not an imported-input share or supplier geography measure; period basis requires review.")

        add("F19", "net_fx_position_total_table", 64, "20. Net yabancı para varlık yükümlülük pozisyonu", -20_474_554,
            status="review_required", note="Table agrees with FX assets minus liabilities, but narrative on PDF63 reports −19,918,099 for current period. Source conflict retained.")
        monetary = re.search(r"pozisyonu\s*\(1\+2a\+5\+6a-10-11-12a-14-15-16a\)\s*(\([\d.]+\))", pages[63], re.I)
        if not monetary or number(monetary.group(1)) != -22_063_540:
            raise ValueError("Monetary FX position evidence changed")
        observations.append({**common, "feature_id": "F19", "raw_component": "net_fx_position_monetary", "value": -22_063_540,
            "unit": "TRY", "pdf_page": 64, "page_or_note": "PDF64/printed62, note26; narrative PDF63",
            "extraction_status": "extracted_snapshot", "evidence_excerpt": monetary.group(0), "is_proxy": False,
            "coverage_ratio": "", "note": "Monetary position only; includes neither every nonmonetary exposure nor whole operational FX sensitivity."})
        add("F19", "fx_sensitivity_profit_effect_10pct_appreciation_reported", 66, "TOPLAM (3 + 6 +9)", -2_046_440,
            status="review_required", note="Published aggregate profit/loss sensitivity for 10% foreign-currency appreciation. Source table does not equal a simple 10% of the separately reported monetary net FX position; retain scope/value conflict for review. Not a whole-business forecast.")

        add("F20", "debt_currency_try_short", 32, "TL", 2_028_497,
            note="Carrying amount by currency in note5. Long TRY cell is a dash; do not silently convert to numeric zero.")
        add("F20", "debt_currency_usd_short_try_equivalent", 32, "ABD Doları", 37_158_065,
            text=pages[31].replace("ABc coları", "ABD Doları"), note="Currency is USD; amount expressed in TRY equivalent.")
        add("F20", "debt_maturity_under_1y", 32, "1 yıldan az", 39_186_562)
        add("F20", "debt_maturity_1to5y", 32, "1 - 5 yıl", 13_249_106)
        fixed = pages[66].split("Sabit Faizli Araçlar", 1)[1].split("Değişken Faizli Finansal Araçlar", 1)[0]
        variable = pages[66].split("Değişken Faizli Finansal Araçlar", 1)[1]
        add("F20", "fixed_rate_bank_debt", 67, "Banka kredileri", 15_918_935, text=fixed)
        add("F20", "floating_rate_bank_debt", 67, "Banka kredileri", 36_516_733, text=variable)
        # Ratios need the same reported coverage on both sides. This bank-debt
        # denominator exactly reconciles to the note5 total; still no PIT claim.
        denominator = 15_918_935 + 36_516_733
        if denominator != 39_186_562 + 13_249_106:
            raise ValueError("Debt note denominator reconciliation failed")
        observations.append({**common, "feature_id": "F20", "raw_component": "floating_rate_debt_share", "value": 36_516_733 / denominator,
            "unit": "ratio_0_1", "pdf_page": 67, "page_or_note": "note26 PDF67; denominator note5 PDF32",
            "extraction_status": "derived_snapshot", "evidence_excerpt": "36,516,733 / (15,918,935 + 36,516,733)",
            "is_proxy": False, "coverage_ratio": 1.0, "note": "Reported fixed+floating instruments equal financial-debt maturity total. Latest historical PDF copy; original vintage unavailable."})

        # Explicit disclosure absence is stronger than a failed keyword match.
        segment_text = norm(pages[29])
        if "bolumlere gore raporlama bilgisi bulunmamaktadir" not in segment_text:
            raise ValueError("Segment disclosure-absence evidence changed")
        for row in searches:
            if row["source_document_id"] == source_id and row["feature_id"] in ("C02", "C04"):
                row["missing_reason"] = "not_disclosed"
                row["search_status"] = "not_disclosed_in_report"
                row["note"] = "Note3 PDF30 explicitly says no operating or geographical segment reporting. This does not establish zero exposure."

    write_csv(DATA / "company_profile_pilot.csv", observations)
    write_csv(DATA / "company_profile_pilot_search.csv", searches)
    manifest = {"schema_version": "1.0", "registry_version": registry["version"], "sources": sources,
        "observation_rows": len(observations), "family_source_searches": len(searches),
        "limitation": "Bounded pilot; current historical company PDF copies; no original-vintage proof; no record eligible for PIT training.",
        "families": sorted(KEYWORDS), "unregistered_requested_ids": ["C11", "C12"],
        "missing_reason_policy": "No keyword hit=not_extracted; explicit disclosure absence=not_disclosed; source version unknown=unavailable_vintage."}
    (DATA / "company_profile_pilot_manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k: manifest[k] for k in ("observation_rows", "family_source_searches", "families")}, ensure_ascii=False))
    return manifest


if __name__ == "__main__":
    build_pilot()
