# E-Commerce Sales & Customer Segmentation

A portfolio-ready data analytics and machine learning project focused on understanding e-commerce sales, customer purchasing behavior, and actionable customer segments.

> **Project status:** Day 13 — documentation and portfolio polish completed. Numerical findings remain runtime-derived and are never fabricated.

## Business Problem

E-commerce transaction data can reveal where revenue is generated, how customers purchase, which products and markets contribute most, and how customer value differs across the base. This project builds a reproducible analytics-to-segmentation workflow that turns transaction-level data into evidence-based business recommendations.

## Project Objectives

- Validate and understand a real e-commerce transaction dataset.
- Apply transparent, reproducible data-cleaning decisions.
- Analyze sales, products, customers, time patterns, and geography.
- Build customer-level RFM measures.
- Prepare RFM features for distance-based clustering.
- Evaluate K-Means cluster counts and create customer segments.
- Translate model output into transparent business archetypes.
- Provide a Power BI-ready dashboard specification and dynamic DAX measures.

## Dataset

The project uses the **UCI Online Retail** dataset (dataset ID 352), a transactional dataset for a UK-based registered non-store online retailer. The original workbook is intentionally not committed because of its size; notebooks retrieve it reproducibly with `ucimlrepo`. Full provenance and citation details are documented in [`data/DATASET.md`](data/DATASET.md).

No synthetic or fabricated data is presented as real data.

## End-to-End Workflow

```text
UCI Online Retail
       │
       ▼
Data understanding
       │
       ▼
Conservative cleaning
       │
       ▼
Sales / product / customer EDA
       │
       ▼
RFM customer metrics
       │
       ▼
Skew-aware preprocessing + scaling
       │
       ▼
K-Means evaluation
       │
       ▼
Relative business segment labels
       │
       ├──────────────► Final analysis & visuals
       │
       └──────────────► Power BI dashboard specification
```

## Analysis Highlights

### Sales analytics

The EDA layer covers executive sales KPIs, order-value and quantity distributions, product performance, monthly trends, weekday behavior, country performance, customer purchasing behavior, and customer orders-versus-revenue relationships.

### RFM segmentation

Customer Recency, Frequency and Monetary value are calculated from the validated positive-sales analytical view. RFM features are transformed only when observed skewness exceeds the documented threshold, then standardized before K-Means clustering.

### K-Means segmentation

Candidate cluster counts from **k=2 through k=8** are evaluated with inertia and silhouette score. The reproducible workflow uses the highest observed silhouette candidate as the initial selected `k`. Cluster IDs are then translated into relative, descriptive business archetypes using the observed cluster profiles.

### Business interpretation

Segment actions are framed as hypotheses rather than measured campaign effects. Examples include protecting high-value engaged customers, nurturing developing customers, improving basket value for frequent lower-value customers, and testing win-back activity for high-value customers with deteriorated recency.

### Power BI

The `dashboard/` folder contains the recommended report model, page layout, interaction design, and DAX measures. A `.pbix` file is not fabricated; the dashboard should be built and refreshed in Power BI Desktop using the real source and validated Python outputs.

## Reproducibility & Integrity

- Use the real UCI source dataset.
- Keep business filters explicit; the cleaned dataset does not silently discard cancellations or non-sales rows.
- Use the positive-sales view consistently for sales and customer-value analysis.
- Do not hard-code numerical findings, rankings, cluster sizes, or segment assignments.
- Use fixed random states for stochastic ML steps.
- Do not infer product categories because the source dataset has no formal category field.
- Do not claim causality, campaign lift, margin impact, or retention outcomes that the transaction data cannot measure.
- The repository avoids committing the large raw workbook.

## Technology Stack

Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Jupyter, `ucimlrepo`, Power BI, DAX, and Git/GitHub.

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

## 14-Day Development Plan

| Day | Focus | Status |
|---:|---|---|
| 1 | Project setup and documentation | Complete |
| 2 | Dataset and data understanding | Complete |
| 3 | Data cleaning | Complete |
| 4–5 | Exploratory data analysis | Complete |
| 6 | Business insights | Complete |
| 7 | RFM analysis | Complete |
| 8 | Clustering preparation | Complete |
| 9 | K-Means segmentation | Complete |
| 10 | Segment interpretation | Complete |
| 11 | Advanced visualization and final analysis | Complete |
| 12 | Power BI dashboard support | Complete |
| 13 | Documentation and portfolio polish | Complete |
| 14 | Final quality check | Next |
