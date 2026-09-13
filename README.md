# E-Commerce Sales & Customer Segmentation

A portfolio-ready data analytics and machine learning project focused on understanding e-commerce sales, customer purchasing behavior, and actionable customer segments.

> **Project status:** Day 12 — Power BI dashboard specification and DAX measures added. Numerical findings remain runtime-derived and are never fabricated.

## Problem Statement

E-commerce businesses generate large volumes of transaction data but need a structured way to understand sales performance, customer behavior, and opportunities for retention and targeted marketing. This project turns transaction-level data into reproducible analysis and customer segmentation insights without fabricating results.

## Objectives

- Validate and understand the real e-commerce transaction data.
- Clean and prepare data using documented, reproducible decisions.
- Analyze sales, products, customers, trends, and geographic performance where supported.
- Measure customer value with RFM analysis where required fields are available.
- Build and evaluate K-Means customer segmentation when supported by the data.
- Translate evidence into practical business recommendations.
- Present the validated analysis through a Power BI dashboard design.

## Technology Stack

Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Jupyter, `ucimlrepo`, Power BI, and Git/GitHub.

## Dataset

The project uses the **UCI Online Retail** dataset (dataset ID 352), a transactional dataset for a UK-based registered non-store online retailer. The original workbook is intentionally not committed because of its size; notebooks retrieve it reproducibly with `ucimlrepo`. See [`data/DATASET.md`](data/DATASET.md) for provenance and citation.

No synthetic or fabricated data is presented as real data.

## Analysis Completed

### Days 1–5

The project includes reproducible data understanding, cleaning, and sales/product/customer EDA covering core sales KPIs, order-value and quantity distributions, product performance, monthly trends, weekday behavior, geography, customer purchasing behavior, and customer orders-versus-revenue relationships.

### Day 6 — Business Insights

`reports/day6_business_insights.md` establishes an evidence-first framework using **Finding → Evidence → Business Meaning → Recommendation**. Numerical findings are intentionally generated from executed notebook outputs rather than hard-coded.

### Days 7–10 — Customer Segmentation

The project implements RFM analysis, transparent clustering preparation, K-Means evaluation, and data-driven business-facing segment labels. Segment results are generated at runtime from the real UCI data.

### Day 11 — Final Analysis & Visuals

`notebooks/08_final_analysis.ipynb` consolidates executive KPIs, revenue trends, country/product performance, customer revenue concentration, and the final RFM/K-Means segmentation view.

### Day 12 — Power BI

`dashboard/POWER_BI_GUIDE.md` defines the Power BI data model, report pages, visual layout, slicers, interaction design, and data-integrity rules. `dashboard/measures.dax` contains reusable DAX measures for sales and customer metrics.

A `.pbix` binary is not fabricated or claimed as generated; it should be built in Power BI Desktop from the real UCI source and validated Python outputs.

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
│   ├── 03_eda_part2.ipynb
│   ├── 04_rfm_analysis.ipynb
│   ├── 05_clustering_preparation.ipynb
│   ├── 06_kmeans_clustering.ipynb
│   ├── 07_segment_interpretation.ipynb
│   └── 08_final_analysis.ipynb
├── src/
│   ├── data_cleaning.py
│   ├── eda.py
│   ├── rfm_analysis.py
│   ├── clustering_prep.py
│   ├── kmeans_clustering.py
│   ├── segment_interpretation.py
│   └── final_analysis.py
├── dashboard/
│   ├── POWER_BI_GUIDE.md
│   └── measures.dax
├── images/
├── reports/
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
- Keep Power BI measures dynamic and aligned with the Python analytical definitions.

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
