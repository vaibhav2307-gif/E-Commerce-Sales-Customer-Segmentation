"""Reusable exploratory-analysis helpers for Online Retail."""

from __future__ import annotations

import pandas as pd


def positive_sales_view(df: pd.DataFrame) -> pd.DataFrame:
    """Return valid positive-sales transactions without modifying the input."""
    required = {"quantity", "unit_price", "invoice_date"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    out = df.loc[
        df["quantity"].gt(0)
        & df["unit_price"].gt(0)
        & df["invoice_date"].notna()
    ].copy()
    out["revenue"] = out["quantity"] * out["unit_price"]
    return out


def sales_kpis(df: pd.DataFrame) -> pd.Series:
    """Calculate core sales KPIs from a positive-sales transaction view."""
    return pd.Series(
        {
            "total_revenue": df["revenue"].sum(),
            "total_orders": df["invoice_no"].nunique(),
            "total_customers": df["customer_id"].nunique(),
            "average_order_value": df.groupby("invoice_no")["revenue"].sum().mean(),
            "total_units": df["quantity"].sum(),
        }
    )


def product_performance(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """Rank products by revenue, retaining units and distinct orders."""
    result = (
        df.groupby(["stock_code", "description"], dropna=False)
        .agg(
            revenue=("revenue", "sum"),
            units=("quantity", "sum"),
            orders=("invoice_no", "nunique"),
        )
        .sort_values("revenue", ascending=False)
    )
    return result.head(top_n).reset_index()
