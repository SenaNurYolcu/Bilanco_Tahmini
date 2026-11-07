import sys
import io
import zipfile
import json
import hashlib
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from external_point_in_time import external_asof
from fetch_external_macro_and_risk import parse_tcmb_inflation, fetch_ecb, SourceClient


def test_latest_revised_value_is_not_available_at_original_release():
    data = pd.DataFrame([
        {"series_name": "GPR", "period_end": "2020-01-31", "value": 100,
         "available_at": "2020-02-03T10:00:00Z", "pit_eligible": True},
        {"series_name": "GPR", "period_end": "2020-01-31", "value": 999,
         "available_at": "2026-11-07T10:00:00Z", "pit_eligible": True},
    ])
    assert external_asof(data, "GPR", "2020-03-31")["value"] == 100


def test_false_strings_and_missing_availability_are_excluded():
    data = pd.DataFrame([
        {"series_name": "GPR", "period_end": "2020-01-31", "value": 999,
         "available_at": "2020-02-03", "pit_eligible": "False"},
        {"series_name": "GPR", "period_end": "2020-01-31", "value": 999,
         "available_at": "", "pit_eligible": "True"},
    ])
    assert external_asof(data, "GPR", "2020-03-31") is None


def test_future_observation_is_not_selected_even_with_invalid_early_release():
    data = pd.DataFrame([{"series_name": "GPR", "period_end": "2020-12-31", "value": 100,
                          "available_at": "2020-01-01", "pit_eligible": True}])
    assert external_asof(data, "GPR", "2020-03-31") is None


def test_general_ppi_is_never_substituted_for_domestic_ppi():
    raw = b'<table><tr><td>12-2013</td><td>6.97</td><td>&nbsp;</td><td>1.11</td><td></td></tr><tr><td>01-2014</td><td></td><td>10.72</td><td></td><td>3.32</td></tr></table>'
    data = parse_tcmb_inflation(raw, producer=True)
    domestic = data.loc[data.series_name == "M05_YIUFE_YoY"]
    assert domestic.period_end.tolist() == ["2014-01-31"]
    assert domestic.value.tolist() == [10.72]
    assert data.loc[data.series_name == "legacy_UFE_YoY", "value"].tolist() == [6.97]


def test_ecb_cross_rate_uses_try_per_eur_divided_by_usd_per_eur():
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w") as archive:
        archive.writestr("eurofxref-hist.csv", "Date,USD,TRY\n2010-01-04,1.5,3\n")

    class Client:
        def get(self, *_args):
            return stream.getvalue(), {"source_url": "https://www.ecb.europa.eu/", "sha256": "a" * 64}

    data = fetch_ecb(Client()).set_index("series_name")
    assert data.loc["USDTRY_ECB_cross_reference", "value"] == 2
    assert data.loc["EURTRY_ECB_reference", "value"] == 3
    assert not data.pit_eligible.any()


def test_changed_cached_file_cannot_inherit_original_retrieval_time(tmp_path):
    path = tmp_path / "data.csv"
    path.write_bytes(b"revised locally")
    metadata = {"source_url": "https://example.com/data.csv", "retrieved_at": "2020-01-01T00:00:00Z",
                "sha256": hashlib.sha256(b"original content").hexdigest()}
    path.with_name("data.csv.source.json").write_text(json.dumps(metadata))
    _, record = SourceClient(tmp_path, offline=True).get(metadata["source_url"], "data.csv")
    assert record["retrieved_at"] == ""
    assert record["provenance_status"] == "cache_provenance_unverified"


def test_unchanged_cache_preserves_verified_retrieval_time(tmp_path):
    path = tmp_path / "data.csv"
    path.write_bytes(b"original content")
    metadata = {"source_url": "https://example.com/data.csv", "retrieved_at": "2020-01-01T00:00:00Z",
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    path.with_name("data.csv.source.json").write_text(json.dumps(metadata))
    _, record = SourceClient(tmp_path, offline=True).get(metadata["source_url"], "data.csv")
    assert record["retrieved_at"] == metadata["retrieved_at"]
    assert record["provenance_status"] == "cached_content_hash_verified"
