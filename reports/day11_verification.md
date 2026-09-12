# Day 11 Verification — Final Analysis & Visuals

## Scope

Day 11 consolidates the validated sales, customer, RFM and K-Means work into a portfolio-ready final analysis notebook and reusable visualization helpers. Power BI work is intentionally deferred to Day 12.

## Verification checklist

- [x] `notebooks/08_final_analysis.ipynb` rebuilds the analysis from the UCI Online Retail dataset at runtime.
- [x] The notebook uses the project's existing positive-sales analytical view and does not invent a second cleaning policy.
- [x] Executive KPIs are generated dynamically through `sales_kpis`.
- [x] Monthly revenue, order and active-customer summaries are generated dynamically.
- [x] Country and product summaries reuse the existing EDA logic.
- [x] Customer revenue concentration is calculated dynamically; no percentile or revenue-share result is hard-coded.
- [x] Final segmentation reuses the Day 7–10 RFM, clustering preparation, K-Means evaluation and relative-label methodology.
- [x] Segment sizes, RFM statistics and selected k are generated at runtime.
- [x] Visualization helpers use descriptive titles and axis labels and return Matplotlib figures for reuse.
- [x] No campaign lift, causality, margin or retention outcome is claimed because those fields are not present in the transaction dataset.
- [x] Day 12 Power BI work is not included.

## Execution note

The repository notebooks retrieve the public dataset with `ucimlrepo`. This repository session does not provide a local internet-enabled notebook runtime, so numerical notebook outputs were not fabricated or represented as executed here. The verification therefore checks the code paths, dependencies and data-driven methodology rather than inventing runtime metrics.

## Files added

- `src/final_analysis.py`
- `notebooks/08_final_analysis.ipynb`
- `reports/day11_verification.md`
