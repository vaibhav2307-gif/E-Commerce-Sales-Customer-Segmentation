# Day 6 — Business Insights Framework

## Important limitation

The repository intentionally does not store a downloaded copy of the UCI workbook. The notebooks retrieve the source dataset at runtime. Therefore, this report does **not** hard-code numerical findings that have not been verified from an executed dataset run.

## Evidence-first insight framework

The Day 4 and Day 5 notebooks now calculate the evidence required for business interpretation:

| Area | Evidence to inspect | Business meaning | Recommendation rule |
|---|---|---|---|
| Sales trend | Monthly revenue, orders, customers | Identifies growth/decline periods and changes in demand | Investigate sustained peaks/declines and align inventory or campaigns accordingly |
| Product performance | Product revenue, units, distinct orders | Shows which products contribute to commercial activity | Prioritize consistently strong products; investigate weak products before discontinuation |
| Customer value | Customer revenue, orders, units | Separates repeat/high-value behavior from lower activity | Use later RFM segmentation for targeted retention and loyalty actions |
| Geography | Country revenue, orders, customers | Shows geographic concentration and market reach | Protect strong markets and investigate expansion opportunities where evidence supports them |
| Weekday behavior | Revenue and order volume by weekday | Reveals purchasing timing | Align campaigns and operational capacity with observed demand patterns |

## Findings

**Finding → Evidence → Business Meaning → Recommendation** is the required format for each final finding. Numerical values should be copied from executed notebook outputs, not manually invented.

### 1. Sales timing

- **Finding:** Determine the strongest and weakest sustained months from the monthly table.
- **Evidence:** `notebooks/03_eda_part2.ipynb` produces monthly revenue, order, and customer metrics.
- **Business Meaning:** Sustained changes can indicate seasonality or changes in customer activity.
- **Recommendation:** Plan inventory, staffing, and promotional timing around validated demand patterns.

### 2. Product contribution

- **Finding:** Rank products by revenue and compare units and distinct orders.
- **Evidence:** Day 4 product-performance analysis.
- **Business Meaning:** Revenue leaders may warrant stronger availability and merchandising attention.
- **Recommendation:** Protect availability of validated high-contribution products while reviewing low-contribution products in context.

### 3. Customer purchasing behavior

- **Finding:** Examine the distribution of customer revenue, order counts, and units.
- **Evidence:** Day 5 customer-level analysis and orders-versus-revenue visualization.
- **Business Meaning:** Customer value is not evenly distributed; later RFM analysis can make this actionable.
- **Recommendation:** Avoid one-size-fits-all retention strategies and use RFM segments once validated.

### 4. Geographic concentration

- **Finding:** Identify countries with the highest revenue and compare their order/customer counts.
- **Evidence:** Day 5 country-level table.
- **Business Meaning:** Revenue concentration may create both a strong-market opportunity and geographic dependency.
- **Recommendation:** Protect service quality in validated leading markets and investigate under-served markets only where the data supports the opportunity.

## Day 6 conclusion

The project now has an evidence-first business interpretation framework. Final numeric findings are deliberately deferred to executed notebook outputs rather than fabricated in documentation. This preserves analytical integrity and makes the recommendations reproducible.
