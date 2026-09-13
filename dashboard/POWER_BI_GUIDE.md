# Day 12 — Power BI Dashboard Specification

This folder contains the reproducible specification for the Power BI layer of the project. The repository does **not** contain a fabricated `.pbix` file or fabricated dashboard screenshots. Build the report in Power BI Desktop from the real UCI Online Retail source and the validated Python outputs.

## Data source

Use the UCI Online Retail workbook documented in `data/DATASET.md`. The Python pipeline uses a positive-sales analytical view: `quantity > 0`, `unit_price > 0`, and a valid `invoice_date`. Exact duplicates are removed during cleaning and `revenue = quantity * unit_price` is calculated. Cancellations and non-sales rows are not silently deleted from the cleaned dataset; the Power BI sales visuals should use the same positive-sales rule.

Because the source workbook is intentionally not committed, refresh the source from UCI rather than checking a large workbook into Git.

## Recommended Power BI model

Create a transaction table named `Sales` with these fields:

- `invoice_no`
- `stock_code`
- `description`
- `quantity`
- `invoice_date`
- `unit_price`
- `customer_id`
- `country`
- `revenue`

Create a calendar table named `Calendar` and relate `Calendar[Date]` to `Sales[invoice_date]`.

For the customer-segmentation page, import the customer-level RFM/segment output produced by the validated Python workflow when the notebook is executed. Keep this as a separate `CustomerSegments` table keyed by `customer_id`. Do not manually type cluster assignments or segment sizes.

## Report pages

### Page 1 — Executive Sales Overview

**KPI cards**
- Total Revenue
- Total Orders
- Total Customers
- Average Order Value
- Total Units

**Visuals**
- Monthly revenue line chart
- Revenue by country bar chart
- Top products by revenue bar chart
- Revenue trend with year/month drill-down

**Slicers**
- Date
- Country
- Product / Stock Code

### Page 2 — Customer & Segmentation

**KPI cards**
- Customers segmented
- Average customer monetary value
- Average frequency
- Average recency

**Visuals**
- Customer segment distribution
- Segment mean monetary value
- Frequency vs monetary scatter
- Segment RFM comparison table

Use the business-facing labels from Day 10. Cluster IDs are technical identifiers and should not be presented as customer segment names.

### Page 3 — Product & Geography

**Visuals**
- Top products by revenue
- Top products by units
- Country revenue
- Country orders
- Country customers

Avoid inventing product categories: the UCI dataset does not provide a formal category field.

## Interaction design

- Keep slicers synchronized where useful.
- Enable cross-filtering between country/product/customer visuals.
- Use tooltip pages for detailed product and segment information.
- Use descriptive business titles rather than technical column names.
- Keep currency formatting consistent with the source/business context.
- Add a small methodology note to the report: sales visuals use the validated positive-sales view; segmentation comes from RFM + standardized K-Means features.

## Data-integrity rules

1. Do not paste hard-coded KPI values into cards.
2. Do not manually enter cluster sizes or segment percentages.
3. Do not treat cluster IDs as ordered scores.
4. Do not claim campaign lift, causality, margin, or retention impact from this transaction-only dataset.
5. Refresh from the actual UCI source when producing final screenshots or publishing the report.

## Build limitation

A `.pbix` file is a Power BI Desktop binary artifact and cannot be authoritatively constructed or validated through the repository's text-file GitHub interface. This specification therefore provides the exact model, measures, visuals, filters, and integrity rules needed to build the dashboard without fabricating a dashboard artifact.
