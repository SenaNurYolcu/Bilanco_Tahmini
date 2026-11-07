"""As-of access requires the particular vintage's verified availability."""
from __future__ import annotations
import pandas as pd


def external_asof(observations: pd.DataFrame, series_name: str, cutoff) -> dict | None:
    """CSV string 'False' is never eligible; missing release/vintage is excluded."""
    if observations.empty:
        return None
    data = observations.loc[observations["series_name"].eq(series_name)].copy()
    eligible = data["pit_eligible"].astype(str).str.lower().eq("true")
    data["_available"] = pd.to_datetime(data["available_at"], utc=True, errors="coerce")
    data["_period"] = pd.to_datetime(data["period_end"], utc=True, errors="coerce")
    cutoff = pd.Timestamp(cutoff)
    cutoff = cutoff.tz_localize("UTC") if cutoff.tzinfo is None else cutoff.tz_convert("UTC")
    data = data.loc[eligible & data["_available"].notna() & (data["_available"] <= cutoff) & (data["_period"] <= cutoff)]
    if data.empty:
        return None
    row = data.sort_values(["_period", "_available"]).iloc[-1]
    return {k: row[k] for k in observations.columns}
