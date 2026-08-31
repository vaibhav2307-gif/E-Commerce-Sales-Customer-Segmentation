# Day 3 — Cleaning Notes

## Scope

The cleaning workflow standardizes recognized UCI Online Retail columns, parses dates, converts numeric fields, removes exact duplicate rows, and derives transaction revenue.

## Important business rules

Cancellations, non-positive quantities/prices, and missing customer IDs are not silently discarded from the base cleaned dataset. They are measured first and can be excluded explicitly for sales/customer analyses where positive completed sales are required.

## Verification

- Cleaning logic is implemented in `src/data_cleaning.py`.
- Notebook: `notebooks/02_data_cleaning.ipynb`.
- The notebook retrieves the real UCI dataset at runtime rather than embedding fabricated values.
- The positive-sales analytical view requires valid dates, quantity > 0, and unit price > 0.
- Raw/processed data remain excluded by `.gitignore` unless deliberately committed.
