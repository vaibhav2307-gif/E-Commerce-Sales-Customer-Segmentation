# Day 9 — K-Means Clustering Verification

## Scope
Evaluated K-Means cluster counts and fit a reproducible customer segmentation model using the model-ready RFM feature matrix from Day 8.

## Methodology checks
- Candidate values of `k` from 2 through 8 are evaluated when valid for the available customer rows.
- Inertia and silhouette score are both calculated from the actual dataset at runtime.
- The highest observed silhouette candidate is selected as the initial model choice.
- `random_state=42` and `n_init=20` are fixed for reproducibility.
- Cluster labels remain numeric identifiers; business-facing segment names are intentionally deferred to Day 10.
- Cluster profiles report count, mean and median Recency, Frequency and Monetary values for interpretation in the next stage.

## Data integrity
No cluster count, inertia, silhouette score, cluster size, or RFM statistic is hard-coded. The notebook retrieves the documented UCI Online Retail dataset at runtime.

## Verification status
The K-Means helper, notebook, and verification report were committed to the repository. The notebook uses the Day 8 preprocessing path rather than introducing a separate or inconsistent feature-engineering definition.
