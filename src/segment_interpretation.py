"""Business-facing profiling helpers for K-Means customer segments."""

from __future__ import annotations

import pandas as pd


def profile_clusters(clustered_rfm: pd.DataFrame) -> pd.DataFrame:
    """Summarize each cluster using customer count and RFM mean/median."""
    required = {"cluster", "recency", "frequency", "monetary"}
    missing = required - set(clustered_rfm.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    return (
        clustered_rfm.groupby("cluster")
        .agg(
            customers=("cluster", "size"),
            recency_mean=("recency", "mean"),
            recency_median=("recency", "median"),
            frequency_mean=("frequency", "mean"),
            frequency_median=("frequency", "median"),
            monetary_mean=("monetary", "mean"),
            monetary_median=("monetary", "median"),
        )
        .reset_index()
    )


def add_relative_segment_labels(profile: pd.DataFrame) -> pd.DataFrame:
    """Assign interpretable archetypes using cross-cluster median comparisons.

    The labels are descriptive, not learned classes. For each cluster, R/F/M
    are compared with the median cluster profile. Recency is inverted because
    lower recency means more recent activity. This keeps the naming rule
    transparent and data-driven without inventing absolute thresholds.
    """
    out = profile.copy()
    med = out[["recency_mean", "frequency_mean", "monetary_mean"]].median()
    out["recent"] = out["recency_mean"] <= med["recency_mean"]
    out["frequent"] = out["frequency_mean"] >= med["frequency_mean"]
    out["high_value"] = out["monetary_mean"] >= med["monetary_mean"]

    def label(row: pd.Series) -> str:
        if row["recent"] and row["frequent"] and row["high_value"]:
            return "High-Value Loyal"
        if row["recent"] and row["high_value"]:
            return "Recent High-Value"
        if row["frequent"] and row["high_value"]:
            return "Frequent High-Value"
        if row["recent"] and row["frequent"]:
            return "Recent Frequent"
        if row["recent"]:
            return "Recent / Developing"
        if row["frequent"]:
            return "Frequent / Lower Value"
        if row["high_value"]:
            return "High-Value / At Risk"
        return "Lower Engagement"

    out["segment_label"] = out.apply(label, axis=1)
    return out
