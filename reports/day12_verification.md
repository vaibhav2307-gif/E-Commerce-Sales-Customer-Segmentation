# Day 12 Verification — Power BI Dashboard Support

## Scope

Day 12 adds the Power BI report specification and reusable DAX measure definitions for the validated analytics workflow. It does not fabricate a `.pbix` file, screenshots, KPI values, or segment outputs.

## Verification checklist

- [x] `dashboard/POWER_BI_GUIDE.md` defines the recommended data model and report pages.
- [x] Executive sales KPIs map directly to the existing `Sales` fields and positive-sales analytical policy.
- [x] Customer segmentation is explicitly separated into a `CustomerSegments` table and must use Python-generated RFM/K-Means outputs.
- [x] DAX measures calculate values dynamically rather than hard-coding results.
- [x] Calendar-based month-over-month measures are provided separately from the base sales measures.
- [x] Dashboard visual recommendations cover sales, customers, segmentation, products and geography.
- [x] Product-category analysis is not introduced because the source dataset has no formal category field.
- [x] Data-integrity guardrails prohibit manual segment assignments and unsupported causal claims.
- [x] The absence of a committed `.pbix` artifact is explicitly documented rather than misrepresented as a completed binary dashboard.

## Execution note

The GitHub repository interface available in this workflow can create and validate text files but cannot authoritatively generate or open Power BI Desktop `.pbix` binaries. Therefore the Day 12 deliverable is the reproducible dashboard specification and DAX layer. Final Power BI construction and screenshots should be created in Power BI Desktop from the real UCI dataset and validated Python outputs.

## Files added

- `dashboard/POWER_BI_GUIDE.md`
- `dashboard/measures.dax`
- `reports/day12_verification.md`
