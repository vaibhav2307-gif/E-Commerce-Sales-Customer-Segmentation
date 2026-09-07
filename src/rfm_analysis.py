"""Reusable RFM analysis helpers for the UCI Online Retail dataset."""

from __future__ import annotations

import pandas as pd


def build_rfm(df: pd.DataFrame, reference_date=None) -> pd.DataFrame:
    """Build customer-level Recency, Frequency and Monetary metrics.

    The input is expected to be a cleaned positive-sales transaction view.
    Frequency is the number of distinct invoices; Monetary is total revenue.
    If no reference date is supplied, one day after the latest transaction is used.
    """
    required = {"customer_id", "invoice_no", "invoice_date", "revenue"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    work = df.loc[
        df["customer_id"].notna()
        & df["invoice_date"].notna()
        & df["revenue"].notna()
    ].copy()
    if work.empty:
        raise ValueError("No customer-level transactions remain for RFM analysis.")

    if reference_date is None:
        reference_date = work["invoice_date"].max() + pd.Timedelta(days=1)
    reference_date = pd.Timestamp(reference_date)

    rfm = (
        work.groupby("customer_id")
        .agg(
            last_purchase=("invoice_date", "max"),
            frequency=("invoice_no", "nunique"),
            monetary=("revenue", "sum"),
        )
        .reset_index()
    )
    rfm["recency"] = (reference_date - rfm["last_purchase"]).dt.days
    return rfm[["customer_id", "recency", "frequency", "monetary", "last_purchase"]]


def add_rfm_scores(rfm: pd.DataFrame, n_bins: int = 4) -> pd.DataFrame:
    """Add relative quartile-style RFM scores, with higher scores as better."""
    if n_bins < 2:
        raise ValueError("n_bins must be at least 2")
    out = rfm.copy()
    rank_recency = out["recency"].rank(method="first")
    rank_frequency = out["frequency"].rank(method="first")
    rank_monetary = out["monetary"].rank(method="first")
    labels = list(range(1, n_bins + 1))
    out["r_score"] = pd.qcut(rank_recency, n_bins, labels=list(reversed(labels))).astype(int)
    out["f_score"] = pd.qcut(rank_frequency, n_bins, labels=labels).astype(int)
    out["m_score"] = pd.qcut(rank_monetary, n_bins, labels=labels).astype(int)
    out["rfm_score"] = (
        out["r_score"].astype(str)
        + out["f_score"].astype(str)
        + out["m_score"].astype(str)
    )
    return out
