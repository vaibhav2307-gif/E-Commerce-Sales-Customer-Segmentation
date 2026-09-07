# Day 7 Verification — RFM Analysis

## Scope completed

- Added `notebooks/04_rfm_analysis.ipynb`.
- Added reusable RFM functions in `src/rfm_analysis.py`.
- Recency uses days since the customer's latest positive purchase.
- Frequency uses distinct invoice count.
- Monetary uses summed positive-sales revenue.
- Reference date is one day after the latest transaction retained for customer-level RFM.
- Distribution statistics, skewness, histograms, and boxplots are calculated at runtime.
- Four-bin relative RFM scores are implemented with reversed scoring for recency.

## Integrity checks

- No raw dataset or fabricated RFM values are committed.
- The notebook retrieves the documented UCI Online Retail dataset at runtime.
- Customers without a usable `customer_id` are excluded from customer-level RFM rather than assigned a synthetic identity.
- The scoring method is documented as a relative ranking, not a predictive model or absolute customer-value measure.

## Verification status

- Notebook structure is valid Jupyter Notebook JSON.
- The RFM module uses the existing cleaned positive-sales schema (`customer_id`, `invoice_no`, `invoice_date`, `revenue`).
- GitHub file presence is verified after commit.
- Numerical outputs require runtime execution with dataset access and are intentionally not hard-coded here.
