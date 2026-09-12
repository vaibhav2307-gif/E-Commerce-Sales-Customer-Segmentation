"""Reusable portfolio-level analysis summaries and plotting helpers."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd


def monthly_sales_summary(sales: pd.DataFrame) -> pd.DataFrame:
    """Return monthly revenue, orders and active-customer counts."""
    required = {"invoice_date", "invoice_no", "customer_id", "revenue"}
    missing = required - set(sales.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    data = sales.dropna(subset=["invoice_date"]).copy()
    data["month"] = data["invoice_date"].dt.to_period("M").astype(str)
    return (
        data.groupby("month")
        .agg(
            revenue=("revenue", "sum"),
            orders=("invoice_no", "nunique"),
            active_customers=("customer_id", "nunique"),
        )
        .reset_index()
    )


def country_summary(sales: pd.DataFrame) -> pd.DataFrame:
    """Return revenue, orders and customers by country."""
    required = {"country", "invoice_no", "customer_id", "revenue"}
    missing = required - set(sales.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    return (
        sales.groupby("country")
        .agg(
            revenue=("revenue", "sum"),
            orders=("invoice_no", "nunique"),
            customers=("customer_id", "nunique"),
        )
        .sort_values("revenue", ascending=False)
        .reset_index()
    )


def customer_concentration(sales: pd.DataFrame) -> pd.DataFrame:
    """Return customer revenue and cumulative revenue share for concentration analysis."""
    required = {"customer_id", "revenue"}
    missing = required - set(sales.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    customer = (
        sales.groupby("customer_id", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
        .reset_index(drop=True)
    )
    total = customer["revenue"].sum()
    customer["cumulative_revenue_share"] = (
        customer["revenue"].cumsum() / total if total else 0
    )
    customer["customer_rank"] = customer.index + 1
    customer["customer_share"] = customer["customer_rank"] / len(customer)
    return customer


def plot_monthly_revenue(monthly: pd.DataFrame):
    """Create a clean monthly revenue trend chart."""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(monthly["month"], monthly["revenue"], marker="o", linewidth=2)
    ax.set_title("Monthly Revenue Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue")
    ax.tick_params(axis="x", rotation=45)
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    return fig, ax


def plot_segment_revenue(profile: pd.DataFrame):
    """Plot cluster revenue contribution using runtime-derived segment labels."""
    required = {"segment_label", "customers", "monetary_mean"}
    missing = required - set(profile.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    data = profile.sort_values("monetary_mean", ascending=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(data["segment_label"], data["monetary_mean"])
    ax.set_title("Customer Segments: Mean Monetary Value")
    ax.set_xlabel("Mean customer monetary value")
    ax.set_ylabel("Segment")
    fig.tight_layout()
    return fig, ax


def plot_revenue_concentration(concentration: pd.DataFrame):
    """Plot cumulative customer revenue share against customer share."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(concentration["customer_share"], concentration["cumulative_revenue_share"], linewidth=2)
    ax.plot([0, 1], [0, 1], linestyle="--", linewidth=1)
    ax.set_title("Customer Revenue Concentration")
    ax.set_xlabel("Share of customers, ranked by revenue")
    ax.set_ylabel("Cumulative share of revenue")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    return fig, ax
