# Day 8 — Clustering Preparation Verification

## Scope
Prepared customer-level RFM features for distance-based clustering. K-Means fitting and cluster-count selection are intentionally deferred to Day 9.

## Checks completed
- Reused the Day 7 customer-level RFM definition.
- Confirmed the preprocessing operates on Recency, Frequency and Monetary only.
- Calculated observed skewness at runtime rather than assuming the shape of the data.
- Applied `log1p` only when absolute observed skewness exceeded 1.0.
- Retained extreme customers rather than deleting them as outliers.
- Standardized the resulting features with `StandardScaler`.
- Included distribution plots before and after scaling.
- Added a model-ready `scaled_features` matrix for the next day.

## Data integrity
No RFM values, skewness statistics, transformed-column decisions, or customer counts are hard-coded. The notebook retrieves the documented UCI Online Retail data at runtime, so numerical outputs remain dataset-derived.

## Verification status
Repository files were written successfully on the Day 8 working branch and promoted to `main`. The notebook is valid JSON/nbformat structure, and the preprocessing implementation is designed to fail explicitly when required RFM columns are missing or invalid.
