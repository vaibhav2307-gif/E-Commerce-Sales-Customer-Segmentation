# E-Commerce Sales & Customer Segmentation

A portfolio-ready data analytics and machine learning project focused on understanding e-commerce sales, customer purchasing behavior, and actionable customer segments.

> **Project status:** Day 2 — Dataset selected and data-understanding workflow added. Cleaning and deeper analysis will follow only after the dataset has been inspected.

## Problem Statement

E-commerce businesses generate large volumes of transaction data but need a structured way to understand sales performance, customer behavior, and opportunities for retention and targeted marketing. This project turns transaction-level data into reproducible analysis and customer segmentation insights without fabricating results.

## Objectives

- Understand the structure and quality of the available e-commerce transaction data.
- Clean and prepare data using documented, reproducible decisions.
- Analyze sales, products, customers, trends, and other dimensions supported by the dataset.
- Measure customer value using Recency, Frequency, and Monetary (RFM) analysis where the required fields are available.
- Build and evaluate a K-Means customer segmentation model when the data supports it.
- Translate analytical findings into practical business recommendations.
- Provide a portfolio-ready workflow using Python, Jupyter, and supporting dashboard assets.

## Expected Business Outcomes

The completed project is intended to help answer questions such as:

- Which products, categories, periods, or regions contribute most to revenue?
- How do customers differ in purchasing frequency and value?
- Which customer groups may deserve retention, reactivation, or loyalty initiatives?
- How can customer segments support more targeted business decisions?

Actual findings, metrics, segment names, and recommendations will be based only on the dataset and analyses completed in this repository.

## Technology Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- `ucimlrepo` for reproducible access to the selected UCI dataset
- Power BI (where supported by the available data and tooling)
- Git / GitHub

## Project Workflow

1. Data understanding
2. Data cleaning and preprocessing
3. Exploratory data analysis
4. Business insights
5. RFM customer analysis
6. Clustering preparation
7. K-Means customer segmentation
8. Segment interpretation
9. Dashboard and reporting
10. Final validation and documentation

## Dataset

The selected dataset is **UCI Online Retail (dataset ID 352)**. UCI describes it as a transactional dataset for a UK-based, registered, non-store online retailer covering 01/12/2010 through 09/12/2011. The source reports 541,909 instances and the fields used by this project include invoice number, product code, description, quantity, invoice date, unit price, customer ID, and country. citeturn0search0

The original workbook is approximately 22.6 MB, so it is intentionally not committed to GitHub. The Day 2 notebook retrieves it through `ucimlrepo`. See [`data/DATASET.md`](data/DATASET.md) for provenance, citation, licensing, and reproduction instructions.

No synthetic or fabricated data is presented as real data.

## Day 2 Data Understanding

The repository now contains `notebooks/01_data_understanding.ipynb`. The notebook inspects:

- row and column counts
- data types
- missing values
- duplicate records
- unique-value cardinality
- numeric and categorical fields
- date/time candidates
- key customer/product/invoice fields
- country distribution
- date parsing and date range

Cancellations, non-positive quantities/prices, and customer-ID missingness are deliberately left for the Day 3 cleaning stage rather than silently removed during initial inspection.

## Repository Structure

```text
.
├── data/
│   ├── raw/
│   ├── processed/
│   └── DATASET.md
├── notebooks/
│   └── 01_data_understanding.ipynb
├── src/
├── dashboard/
├── images/
├── reports/
├── README.md
├── requirements.txt
└── .gitignore
```

## Reproducibility Principles

- Inspect the real dataset before writing dataset-specific analysis.
- Document important cleaning and modeling decisions.
- Avoid hard-coded analytical results.
- Use fixed random states for stochastic machine-learning steps where appropriate.
- Keep raw data separate from processed data.
- Do not commit secrets, credentials, or unnecessarily large/raw datasets.

## Development Plan

This repository is being developed in 14 deliberate stages. Each stage adds a meaningful project improvement, verifies the result, and then stops for review before the next stage begins.

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
