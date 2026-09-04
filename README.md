# E-Commerce Sales & Customer Segmentation

A portfolio-ready data analytics and machine learning project focused on understanding e-commerce sales, customer purchasing behavior, and actionable customer segments.

> **Project status:** Day 6 — EDA business-insight framework added. Numerical findings remain runtime-derived and are never fabricated.

## Problem Statement

E-commerce businesses generate large volumes of transaction data but need a structured way to understand sales performance, customer behavior, and opportunities for retention and targeted marketing. This project turns transaction-level data into reproducible analysis and customer segmentation insights without fabricating results.

## Objectives

- Validate and understand the real e-commerce transaction data.
- Clean and prepare data using documented, reproducible decisions.
- Analyze sales, products, customers, trends, and geographic performance where supported.
- Measure customer value with RFM analysis where required fields are available.
- Build and evaluate K-Means customer segmentation when supported by the data.
- Translate evidence into practical business recommendations.

## Technology Stack

Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Jupyter, `ucimlrepo`, Power BI where appropriate, and Git/GitHub.

## Dataset

The project uses the **UCI Online Retail** dataset (dataset ID 352), a transactional dataset for a UK-based registered non-store online retailer. The original workbook is intentionally not committed because of its size; notebooks retrieve it reproducibly with `ucimlrepo`. See [`data/DATASET.md`](data/DATASET.md) for provenance and citation.

No synthetic or fabricated data is presented as real data.

## Analysis Completed

### Days 1–5

The project now includes reproducible data understanding, cleaning, and sales/product/customer EDA. The EDA covers core sales KPIs, order-value and quantity distributions, product performance, monthly trends, weekday behavior, geography, customer purchasing behavior, and customer orders-versus-revenue relationships.

### Day 6 — Business Insights

`reports/day6_business_insights.md` establishes an evidence-first framework using:

**Finding → Evidence → Business Meaning → Recommendation**

The framework covers sales timing, product contribution, customer purchasing behavior, and geographic concentration. Numerical findings are intentionally not hard-coded because the source dataset is retrieved at runtime. This prevents unsupported statistics from entering the portfolio documentation.

The source dataset has no formal product-category field, so category-level conclusions are not claimed.

## Repository Structure

```text
.
├── data/
│   ├── raw/
│   ├── processed/
│   └── DATASET.md
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   └── 03_eda_part2.ipynb
├── src/
│   ├── data_cleaning.py
│   └── eda.py
├── dashboard/
├── images/
├── reports/
│   └── day6_business_insights.md
├── README.md
├── requirements.txt
└── .gitignore
```

## Reproducibility Principles

- Use the real source dataset; never fabricate analytical results.
- Keep cleaning and business filters explicit.
- Avoid hard-coded results.
- Preserve raw data separately and avoid committing unnecessarily large source files.
- Use fixed random states for stochastic ML steps where appropriate.

## 14-Day Development Plan

| Day | Focus |
|---:|---|
| 1 | Project setup and documentation |
| 2 | Dataset and data understanding |
| 3 | Data cleaning |
| 4–5 | Exploratory data analysis |
| 6 | Business insights |
| 7 | RFM analysis |
| 8 | Clustering preparation |
| 9 | K-Means segmentation |
| 10 | Segment interpretation |
| 11 | Advanced visualization and final analysis |
| 12 | Power BI dashboard support |
| 13 | Documentation and portfolio polish |
| 14 | Final quality check |
