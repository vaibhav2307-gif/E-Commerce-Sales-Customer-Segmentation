"""Reusable K-Means clustering helpers for customer segmentation."""

from __future__ import annotations

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def evaluate_k_range(
    features: pd.DataFrame,
    k_values=range(2, 9),
    random_state: int = 42,
    n_init: int = 20,
) -> pd.DataFrame:
    """Evaluate K-Means candidates using inertia and silhouette score."""
    if features.empty:
        raise ValueError("No clustering features supplied.")
    results = []
    for k in k_values:
        if k < 2 or k >= len(features):
            continue
        model = KMeans(n_clusters=k, random_state=random_state, n_init=n_init)
        labels = model.fit_predict(features)
        results.append(
            {
                "k": k,
                "inertia": model.inertia_,
                "silhouette_score": silhouette_score(features, labels),
            }
        )
    if not results:
        raise ValueError("No valid k values remain for the supplied feature matrix.")
    return pd.DataFrame(results)


def fit_kmeans(
    features: pd.DataFrame,
    n_clusters: int,
    random_state: int = 42,
    n_init: int = 20,
) -> tuple[KMeans, pd.Series]:
    """Fit a reproducible K-Means model and return model plus labels."""
    if n_clusters < 2 or n_clusters >= len(features):
        raise ValueError("n_clusters must be at least 2 and smaller than the number of rows.")
    model = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init)
    labels = pd.Series(model.fit_predict(features), index=features.index, name="cluster")
    return model, labels
