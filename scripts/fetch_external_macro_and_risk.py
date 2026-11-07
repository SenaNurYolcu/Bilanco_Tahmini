"""Official macro/risk snapshots with honest release/vintage provenance.

Outputs: data/external/rebuilt/{macro_observations.csv,macro_source_status.csv,
source_manifest.json}. Current historical downloads are never claimed PIT.
Yahoo FX, OECD interbank rates and seasonally adjusted IP are not silently used
as TCMB FX, commercial credit rates or calendar-adjusted industrial production.

Run with --refresh to download, --offline to reproduce cached inputs. An optional
--evds-spec JSON maps verified M03/M06/M08 codes; EVDS_API_KEY stays in headers.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import io
import json
import os
import re
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT_DIR / "data/external/rebuilt"
GPR_URL = "https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls"
GEPU_URL = "https://www.policyuncertainty.com/media/Global_Policy_Uncertainty_Data.csv"
OFR_URL = "https://www.financialresearch.gov/financial-stress-index/data/fsi.csv"
ECB_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip"
WB_URL = "https://thedocs.worldbank.org/en/doc/74e8be41ceb20fa0da750cda2f6b9e4e-0050012026/related/CMO-Historical-Data-Monthly.xlsx"
TCMB_BASE = "https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Istatistikler/Enflasyon+Verileri/"
EVDS_GUIDE = "https://evds3.tcmb.gov.tr/igmevdsms-dis/documents/showDocument?docId=8"


class SourceClient:
    def __init__(self, directory: Path, *, refresh=False, offline=False):
        self.directory = directory
        self.refresh, self.offline = refresh, offline
        self.records = []
        directory.mkdir(parents=True, exist_ok=True)

    def get(self, url, name, *, headers=None):
        path = self.directory / name
        meta_path = path.with_name(path.name + ".source.json")
        meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
        cached_hash = hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else ""
        cache_verified = bool(cached_hash and meta.get("sha256") == cached_hash and meta.get("source_url") == url)
        cache_file = str(path.relative_to(ROOT_DIR)) if path.is_relative_to(ROOT_DIR) else str(path)
        record = {"source_url": url, "cache_file": cache_file,
                  "retrieved_at": meta.get("retrieved_at", "") if cache_verified else "", "status": "cached",
                  "provenance_status": "cached_content_hash_verified" if cache_verified else "cache_provenance_unverified"}
        if (self.refresh or not path.exists()) and not self.offline:
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "BilancoTahminiResearch/2.0", **(headers or {})})
                with urllib.request.urlopen(req, timeout=30) as response:
                    raw = response.read()
                    if not raw:
                        raise ValueError("empty response")
                    record["http_last_modified"] = response.headers.get("Last-Modified", "")
                record.update(status="downloaded", retrieved_at=datetime.now(timezone.utc).isoformat(),
                              sha256=hashlib.sha256(raw).hexdigest(), provenance_status="downloaded_from_source")
                # A changed/interrupted raw file cannot inherit an old receipt time.
                temporary = path.with_name(path.name + ".tmp")
                temporary.write_bytes(raw)
                temporary.replace(path)
                # Last-Modified is not an observation's original publication date.
                temporary_meta = meta_path.with_name(meta_path.name + ".tmp")
                temporary_meta.write_text(json.dumps(record, ensure_ascii=False, indent=2))
                temporary_meta.replace(meta_path)
            except (OSError, ValueError) as exc:
                record.update(status="cached_after_download_failure" if path.exists() else "download_failed",
                              error=f"{type(exc).__name__}: {exc}")
                if not path.exists():
                    self.records.append(record)
                    raise
        if not path.exists():
            record["status"] = "offline_cache_missing"
            self.records.append(record)
            raise FileNotFoundError(path)
        raw = path.read_bytes()
        record["sha256"] = hashlib.sha256(raw).hexdigest()
        self.records.append(record)
        return raw, record


def parse_tcmb_inflation(raw: bytes, *, producer=False):
    """Do not fill a blank domestic YI-UFE column with the older general UFE."""
    rows = []
    for tr in re.findall(r"<tr\b[^>]*>(.*?)</tr>", raw.decode("utf-8"), re.I | re.S):
        cells = [html.unescape(re.sub(r"<[^>]+>", " ", cell)).strip()
                 for cell in re.findall(r"<td\b[^>]*>(.*?)</td>", tr, re.I | re.S)]
        if len(cells) < (3 if producer else 2) or not re.fullmatch(r"\d{2}-\d{4}", cells[0]):
            continue
        mm, yyyy = cells[0].split("-")
        values = [("M05_YIUFE_YoY", cells[2]), ("legacy_UFE_YoY", cells[1])] if producer else [("M04_TUFE_YoY", cells[1])]
        for series, value in values:
            try:
                rows.append({"period_end": pd.Period(f"{yyyy}-{mm}", "M").end_time.date().isoformat(),
                             "series_name": series, "value": float(value.replace(",", "."))})
            except ValueError:
                pass
    return pd.DataFrame(rows, columns=["period_end", "series_name", "value"])


def to_observations(frame, record, *, feature_map, unit, release_rule):
    result = frame.copy()
    result["feature_id"] = result["series_name"].map(feature_map).fillna("proxy_only")
    result["unit"] = unit
    result["source_url"] = record["source_url"]
    result["source_sha256"] = record["sha256"]
    result["retrieved_at"] = record.get("retrieved_at", "")
    result["source_fetch_status"] = record.get("status", "")
    result["source_provenance_status"] = record.get("provenance_status", "")
    result["vintage_id"] = record["sha256"][:16]
    result["publication_date"] = ""
    result["available_at"] = ""
    result["availability_status"] = "historical_release_and_vintage_unverified"
    result["pit_eligible"] = False
    result["release_rule"] = release_rule
    return result


def fetch_ecb(client):
    raw, record = client.get(ECB_URL, "ecb_eurofxref_hist.zip")
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        data = pd.read_csv(archive.open("eurofxref-hist.csv"))
    data.columns = data.columns.str.strip()
    data = data.rename(columns={"Date": "period_end"})
    data["EURTRY_ECB_reference"] = pd.to_numeric(data["TRY"], errors="coerce")
    data["USDTRY_ECB_cross_reference"] = data["EURTRY_ECB_reference"] / pd.to_numeric(data["USD"], errors="coerce")
    long = data.melt(id_vars="period_end", value_vars=["EURTRY_ECB_reference", "USDTRY_ECB_cross_reference"],
                     var_name="series_name", value_name="value").dropna(subset=["value"])
    return to_observations(long, record, feature_map={"EURTRY_ECB_reference": "M02", "USDTRY_ECB_cross_reference": "M01"},
                           unit="TRY per currency unit", release_rule="ECB around 16:00 CET working days; latest download, original vintages unverified")


def fetch_gpr(client):
    raw, record = client.get(GPR_URL, "data_gpr_export.xls")
    data = pd.read_excel(io.BytesIO(raw))
    data["period_end"] = pd.to_datetime(data["month"]).dt.to_period("M").dt.to_timestamp("M").dt.strftime("%Y-%m-%d")
    long = data.melt(id_vars="period_end", value_vars=["GPR", "GPRT", "GPRA"], var_name="series_name", value_name="value").dropna()
    return to_observations(long, record, feature_map={"GPR": "R01", "GPRT": "R04", "GPRA": "R04"}, unit="index",
                           release_rule="Monthly beginning of following month; methodology changed in 2021; historical latest snapshot is not PIT")


def fetch_gepu(client):
    raw, record = client.get(GEPU_URL, "Global_Policy_Uncertainty_Data.csv")
    data = pd.read_csv(io.BytesIO(raw))
    for col in ["Year", "Month", "GEPU_ppp"]:
        data[col] = pd.to_numeric(data[col], errors="coerce")
    data = data.dropna(subset=["Year", "Month", "GEPU_ppp"])
    data["period_end"] = [pd.Period(f"{int(y)}-{int(m):02}", "M").end_time.date().isoformat() for y, m in zip(data.Year, data.Month)]
    data["series_name"], data["value"] = "GEPU_ppp", data["GEPU_ppp"]
    return to_observations(data[["period_end", "series_name", "value"]], record, feature_map={"GEPU_ppp": "R02"}, unit="index",
                           release_rule="Monthly series; per-observation publication dates and historical vintages not established")


def fetch_ofr(client):
    raw, record = client.get(OFR_URL, "ofr_fsi.csv")
    data = pd.read_csv(io.BytesIO(raw)).rename(columns={"Date": "period_end", "OFR FSI": "value"})
    data["series_name"] = "OFR_FSI"
    return to_observations(data[["period_end", "series_name", "value"]].dropna(), record, feature_map={"OFR_FSI": "R03"}, unit="index",
                           release_rule="OFR publishes data from two business days prior; holiday calendar and historical vintages not established")


def fetch_worldbank(client):
    raw, record = client.get(WB_URL, "worldbank_pink_sheet_monthly.xlsx")
    data = pd.read_excel(io.BytesIO(raw), sheet_name="Monthly Prices", header=4)
    units = data.iloc[0].to_dict()
    date_col = data.columns[0]
    data = data[data[date_col].astype(str).str.fullmatch(r"\d{4}M\d{2}")].copy()
    data["period_end"] = [pd.Period(str(v).replace("M", "-"), "M").end_time.date().isoformat() for v in data[date_col]]
    # Raw candidate bank; no company/sector commodity mapping is presumed.
    wanted = [c for c in data.columns if c in {"Crude oil, Brent", "Natural gas, Europe", "Coal, Australian", "Iron ore, cfr spot", "Aluminum", "Copper", "Wheat, US HRW"}]
    if not wanted:
        raise ValueError("World Bank columns changed: no expected commodity labels")
    long = data.melt(id_vars="period_end", value_vars=wanted, var_name="series_name", value_name="value")
    long["value"] = pd.to_numeric(long["value"], errors="coerce")
    result = to_observations(long.dropna(subset=["value"]), record, feature_map={c: "M07" for c in wanted},
                             unit="", release_rule="Monthly current-vintage candidates; sector mapping and historical publications unverified")
    result["unit"] = result["series_name"].map(units)
    return result


def fetch_evds_spec(client, spec_path):
    # The EVDS acquisition implementation is PHP, as requested.
    import subprocess
    if client.offline:
        raise ValueError('Offline EVDS uses stored observations, not an API call')
    if not os.environ.get('EVDS_API_KEY'):
        raise ValueError('EVDS_API_KEY missing; use the PHP secret prompt separately')
    subprocess.run(['php', str(ROOT_DIR/'scripts/fetch_evds_data.php'),
                    '--spec', str(spec_path)], check=True)
    return [pd.read_csv(OUT_DIR/'evds/observations.csv').dropna(subset=['value'])]


def build_macro_and_risk_tables(*, refresh=False, offline=False, evds_spec=None):
    client = SourceClient(OUT_DIR / "raw", refresh=refresh, offline=offline)
    outputs, status = [], []
    operations = [("R01,R04", fetch_gpr), ("R02", fetch_gepu), ("R03", fetch_ofr),
                  ("M01,M02", fetch_ecb), ("M07", fetch_worldbank)]
    for feature_ids, call in operations:
        try:
            outputs.append(call(client))
            status.append({"feature_ids": feature_ids, "status": "snapshot_only", "reason": "Historical release/vintage unverified; excluded from strict PIT joins"})
        except Exception as exc:
            status.append({"feature_ids": feature_ids, "status": "failed", "reason": f"{type(exc).__name__}: {exc}"})
    for producer, suffix in [(False, "Tuketici+Fiyatlari"), (True, "Uretici+Fiyatlari")]:
        feature_id = "M05" if producer else "M04"
        try:
            raw, record = client.get(TCMB_BASE + suffix, "tcmb_ufe.html" if producer else "tcmb_tufe.html")
            frame = parse_tcmb_inflation(raw, producer=producer)
            if frame.empty:
                raise ValueError("TCMB table empty or schema changed")
            outputs.append(to_observations(frame, record, feature_map={"M04_TUFE_YoY": "M04", "M05_YIUFE_YoY": "M05"}, unit="percent year-on-year",
                                           release_rule="Monthly; exact original release dates/vintages unknown. UFE and domestic YI-UFE distinct"))
            status.append({"feature_ids": feature_id, "status": "snapshot_only", "reason": "Official TCMB table; original publication history not established"})
        except Exception as exc:
            status.append({"feature_ids": feature_id, "status": "failed", "reason": f"{type(exc).__name__}: {exc}"})
    if evds_spec:
        try:
            outputs.extend(fetch_evds_spec(client, evds_spec))
        except Exception as exc:
            status.append({"feature_ids": "M03,M06,M08", "status": "failed", "reason": str(exc)})
    elif (OUT_DIR/'evds/observations.csv').exists():
        evds=pd.read_csv(OUT_DIR/'evds/observations.csv')
        # Missing data are retained in the EVDS sidecar; numeric values only here.
        outputs.append(evds.dropna(subset=['value']))
    present={str(fid) for frame in outputs if 'feature_id' in frame
             for fid in frame.loc[frame['value'].notna(),'feature_id'].unique()}
    for fid in ['M03','M06']:
        status.append({'feature_ids':fid,'status':'snapshot_only' if fid in present else 'not_fetched',
                       'reason':'Verified EVDS series; latest snapshot, original release/vintage unverified' if fid in present
                       else 'Verified EVDS catalogue mapping is available; authenticated data download has not completed'})
    status.append({'feature_ids':'M08','status':'sector_mapping_required',
                   'reason':'Document defines a family without fixed sector series; no arbitrary common index substituted'})
    observations = pd.concat(outputs, ignore_index=True) if outputs else pd.DataFrame()
    if not observations.empty:
        observations = observations.sort_values(["feature_id", "series_name", "period_end"]).reset_index(drop=True)
    observations.to_csv(OUT_DIR / "macro_observations.csv", index=False)
    pd.DataFrame(status).to_csv(OUT_DIR / "macro_source_status.csv", index=False)
    (OUT_DIR / "source_manifest.json").write_text(json.dumps(client.records, ensure_ascii=False, indent=2))
    print(json.dumps({"observations": len(observations), "historical_pit_eligible": int(observations.get("pit_eligible", pd.Series(dtype=bool)).sum()), "source_status": status}, ensure_ascii=False, indent=2))
    return observations


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--evds-spec")
    args = parser.parse_args()
    build_macro_and_risk_tables(refresh=args.refresh, offline=args.offline, evds_spec=args.evds_spec)
