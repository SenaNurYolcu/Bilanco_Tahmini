"""Re-download official company reports for documented source anomalies.

Preserves the original KAP XLS files. Corrections are emitted only if the downloaded
PDF contains the expected unit, period and numerical evidence. A current copy of
an old report does not establish its first-release vintage.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import re
import urllib.request

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
SOURCE_SPECS = [
    {
        "ticker": "THYAO", "year": 2015, "quarter": 4,
        "url": "https://investor.turkishairlines.com/documents/financial-results/31_12_2015_eng_try.pdf",
        "original_file": "data/kap_raw_xls/THYAO_2015_Q4.xls",
        "evidence_page": 1,
        "checks": [r"Million\s+Turkish\s+Lira", r"31\s+December\s+2015", r"TOTAL\s+ASSETS\s+47\.638\s+31\.876"],
        "verified_unit_multiplier": 1_000_000,
        "expected_assets_reported": 47_638,
        "note": "KAP XLS header says TL; official PDF explicitly says Million TRY. Apply multiplier to monetary amounts, never per-share earnings.",
    },
    {
        "ticker": "THYAO", "year": 2016, "quarter": 1,
        "url": "https://investor.turkishairlines.com/documents/financial-results/31_03_2016_eng_try.pdf",
        "original_file": "data/kap_raw_xls/THYAO_2016_Q1.xls",
        "evidence_page": 1,
        "checks": [r"Million\s+Turkish\s+Lira", r"31\s+March\s+2016", r"TOTAL\s+ASSETS\s+48\.349\s+47\.638"],
        "verified_unit_multiplier": 1_000_000,
        "expected_assets_reported": 48_349,
        "note": "KAP XLS header says TL; official PDF explicitly says Million TRY. Apply multiplier to monetary amounts, never per-share earnings.",
    },
    {
        "ticker": "KAREL", "year": 2012, "quarter": 1,
        "url": "https://www.karel.com.tr/sites/default/files/2023-11/karel-elektronik-31032012.pdf",
        "original_file": "data/kap_raw_xls/KAREL_2012_Q1.xls",
        "evidence_page": 8,
        "checks": [r"2012", r"11\.528\.269\s+5\.425\.142", r"\(4\.778\.913\)\s+\(5\.179\.962\)", r"8\.800\.694\s+\(52\.435\.387\)"],
        "field_overrides": {
            "T15_isletme_nakit_akisi_ytd": 11_528_269,
            "T16_yatirim_nakit_akisi_ytd": -4_778_913,
            "T17_finansman_nakit_akisi_ytd": 8_800_694,
        },
        "note": "Several KAP cash-flow cells contain corrupted decimal strings. Replace only the three verified totals from company PDF cash-flow page; do not rescale other cells heuristically.",
    },
    {
        "ticker": "TOASO", "year": 2013, "quarter": 1,
        "url": "https://www.tofas.com.tr/en/InvestorRelations/FinancialStatements/Documents/TOFAS0313.pdf",
        "original_file": "data/kap_raw_xls/TOASO_2013_Q1.xls",
        "evidence_page": 3,
        "checks": [r"thousands\s+of\s+Turkish\s+Lira", r"31\s+March\s+2013", r"Total\s+assets\s+6\.266\.179\s+6\.067\.343"],
        "verified_unit_multiplier": 1_000,
        "expected_assets_reported": 6_266_179,
        "note": "KAP XLS header says TL; official company financial report explicitly states thousands of TRY. Excludes per-share earnings. The report contains an inconsistent approval-date sentence, which must not be used as publication evidence.",
    },
    {
        "ticker": "TOASO", "year": 2014, "quarter": 3,
        "url": "https://www.tofas.com.tr/en/InvestorRelations/FinancialStatements/Documents/TOFAS%20CMB%200914%20ENG.pdf",
        "original_file": "data/kap_raw_xls/TOASO_2014_Q3.xls",
        "evidence_page": 3,
        "checks": [r"thousands\s+of\s+Turkish\s+Lira", r"30\s+September\s+2014", r"Total\s+assets\s+6\.550\.101\s+5\.928\.202"],
        "verified_unit_multiplier": 1_000,
        "expected_assets_reported": 6_550_101,
        "note": "KAP XLS header says TL; official company financial report explicitly states thousands of TRY. Apply to monetary amounts, never per-share earnings.",
    },
]


def retrieve_reports(output_dir: Path, manifest_path: Path, refresh: bool = False) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for spec in SOURCE_SPECS:
        record = {k: v for k, v in spec.items() if k != "checks"}
        record["source_vintage_status"] = "historical_company_copy_unverified"
        record["available_at"] = None
        record["retrieved_at"] = datetime.now(timezone.utc).isoformat()
        original = ROOT / spec["original_file"]
        if original.is_file():
            record["original_sha256"] = hashlib.sha256(original.read_bytes()).hexdigest()
        dest = output_dir / f'{spec["ticker"]}_{spec["year"]}_Q{spec["quarter"]}_official.pdf'
        try:
            cached = dest.is_file() and not refresh
            if cached:
                raw = dest.read_bytes()
            else:
                req = urllib.request.Request(spec["url"], headers={"User-Agent": "Mozilla/5.0 BilancoResearch/1.0"})
                with urllib.request.urlopen(req, timeout=30) as response:
                    raw = response.read()
                    record["resolved_url"] = response.url
            if not raw.startswith(b"%PDF-"):
                raise ValueError("Official source returned a non-PDF response")
            reader = PdfReader(io.BytesIO(raw))
            text = reader.pages[spec["evidence_page"] - 1].extract_text()
            missing_checks = [pattern for pattern in spec["checks"] if not re.search(pattern, text, re.I)]
            if missing_checks:
                raise ValueError(f"Report evidence did not match: {missing_checks}")
            dest.write_bytes(raw)
            dest.with_suffix(".evidence.txt").write_text(text, encoding="utf-8")
            record["path"] = str(dest.relative_to(ROOT))
            record["sha256"] = hashlib.sha256(raw).hexdigest()
            record["status"] = "verified"
            record["retrieval_mode"] = "cache" if cached else "fresh_http"
            if cached:
                # File system access today is not the historical retrieval time.
                record["retrieved_at"] = None
            record["evidence_checks"] = spec["checks"]
        except Exception as exc:
            record["status"] = "failed"
            record["error"] = f"{type(exc).__name__}: {exc}"
            # Fail closed: a consumer cannot apply planned, unverified corrections.
            record.pop("verified_unit_multiplier", None)
            record.pop("field_overrides", None)
        records.append(record)
        print(f'{spec["ticker"]} {spec["year"]}Q{spec["quarter"]}: {record["status"]}', flush=True)
    manifest = {
        "schema_version": "1.0",
        "purpose": "Source-backed corrections; original files preserved; first-release vintage not proven",
        "sources": records,
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    temp = manifest_path.with_suffix(".part")
    temp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(manifest_path)
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", help="Re-download even if a verified PDF exists locally")
    args = parser.parse_args()
    result = retrieve_reports(ROOT / "data/kap_refreshed", ROOT / "data/kap_refresh_manifest.json", args.refresh)
    if any(source["status"] != "verified" for source in result["sources"]):
        raise SystemExit(1)
