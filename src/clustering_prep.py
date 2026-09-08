"""Reusable preprocessing helpers for customer clustering."""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

RFM_FEATURES = ["recency", "frequency", "monetary"]


def prepare_clustering_features(
    rfm: pd.DataFrame,
    skew_threshold: float = 1.0,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series]:
    """Transform skewed positive RFM features and standardize them.

    A log1p transform is applied only when observed absolute skewness exceeds
    the supplied threshold. No customers are removed as outliers here.
    StandardScaler then puts all three features on a comparable scale for
    distance-based clustering. Returns raw features, model-ready features,
    and the observed skewness values before transformation.
    """
    missing = set(RFM_FEATURES) - set(rfm.columns)
    if missing:
        raise ValueError(f"Missing RFM features: {sorted(missing)}")

    raw = rfm[RFM_FEATURES].dropna().copy()
    if raw.empty:
        raise ValueError("No complete RFM rows available for clustering.")
    if (raw < 0).any().any():
        raise ValueError("RFM features must be non-negative before log1p transformation.")

    skewness = raw.skew()
    transformed = raw.copy()
    transformed_columns = []
    for col in RFM_FEATURES:
        if abs(skewness[col]) > skew_threshold:
            transformed[col] = np.log1p(transformed[col])
            transformed_columns.append(col)

    scaler = StandardScaler()
    scaled = pd.DataFrame(
        scaler.fit_transform(transformed),
        index=transformed.index,
        columns=RFM_FEATURES,
    )
    return raw, scaled, skewness
