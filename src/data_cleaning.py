"""Reusable cleaning helpers for the UCI Online Retail dataset.

The functions are intentionally conservative: they standardize types and
create a transaction revenue field, while leaving business filtering choices
explicit for the notebook.
"""

from __future__ import annotations

import pandas as pd


COLUMN_MAP = {
    "InvoiceNo": "invoice_no",
    "StockCode": "stock_code",
    "Description": "description",
    "Quantity": "quantity",
    "InvoiceDate": "invoice_date",
    "UnitPrice": "unit_price",
    "CustomerID": "customer_id",
    "Country": "country",
}


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with standardized column names where recognized."""
    out = df.copy()
    out = out.rename(columns={k: v for k, v in COLUMN_MAP.items() if k in out.columns})
    return out


def clean_online_retail(df: pd.DataFrame) -> pd.DataFrame:
    """Apply documented type fixes and remove exact duplicate transactions.

    Rows with missing customer IDs or non-positive quantity/price are retained
    because their treatment depends on the downstream business question.
    """
    out = standardize_columns(df)

    if "invoice_date" in out.columns:
        out["invoice_date"] = pd.to_datetime(out["invoice_date"], errors="coerce")
    for column in ("quantity", "unit_price", "customer_id"):
        if column in out.columns:
            out[column] = pd.to_numeric(out[column], errors="coerce")

    out = out.drop_duplicates().reset_index(drop=True)

    if {"quantity", "unit_price"}.issubset(out.columns):
        out["revenue"] = out["quantity"] * out["unit_price"]

    return out


def quality_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return a compact quality summary for each column."""
    return pd.DataFrame(
        {
            "dtype": df.dtypes.astype(str),
            "missing_count": df.isna().sum(),
            "missing_pct": (df.isna().mean() * 100).round(2),
            "unique_count": df.nunique(dropna=True),
        }
    )
