# Dataset — UCI Online Retail

## Source

This project uses the **Online Retail** dataset from the UCI Machine Learning Repository, dataset ID **352**.

Source: https://archive.ics.uci.edu/dataset/352/online-retail

The dataset contains transactional records for a UK-based, registered, non-store online retailer. UCI reports 541,909 instances and describes eight fields relevant to this project: `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, and `Country`.

## Why this dataset

It directly supports the project's intended sales analytics and customer segmentation workflow:

- transaction-level sales analysis
- product and country analysis
- customer purchasing behavior
- time-based sales trends
- RFM analysis using customer, date, frequency, and monetary information
- K-Means clustering after appropriate preprocessing

## Repository policy

The original workbook is approximately 22.6 MB, so the raw dataset is **not committed to this repository**. The Day 2 notebook retrieves the dataset using the `ucimlrepo` Python package.

To reproduce the notebook locally:

```bash
pip install -r requirements.txt
```

Then run `notebooks/01_data_understanding.ipynb` with internet access.

## License and citation

UCI lists the dataset under **CC BY 4.0**. Cite the source as:

> Chen, D. (2015). Online Retail [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33.

The project does not claim ownership of the source dataset.
