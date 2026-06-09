"""Convenience loaders so notebooks read data with one short, consistent call.

``load("sales")`` returns a parsed DataFrame (dates already converted); ``load("regions")``
returns a GeoDataFrame. If the data has not been generated yet, the error message tells the
student exactly what to run instead of failing with a cryptic ``FileNotFoundError``.
"""

from __future__ import annotations

import pandas as pd

from .utils import DATA_PROCESSED, DATA_RAW

# name -> (path, kind). "csv" is read with pandas, "geojson" with geopandas.
_DATASETS = {
    "sales": (DATA_RAW / "sales.csv", "csv", ["date"]),
    "customers": (DATA_RAW / "customers.csv", "csv", None),
    "transactions": (DATA_RAW / "transactions.csv", "csv", ["date"]),
    "operations": (DATA_RAW / "operations.csv", "csv", None),
    "dashboard": (DATA_PROCESSED / "dashboard.csv", "csv", ["month"]),
    "regions": (DATA_RAW / "regions.geojson", "geojson", None),
    "stores": (DATA_RAW / "stores.geojson", "geojson", None),
}


def available() -> list[str]:
    """Return the names of all loadable datasets."""
    return list(_DATASETS)


def load(name: str):
    """Load a generated dataset by name (see :func:`available`).

    Raises a helpful error if the name is unknown or the file is missing.
    """
    if name not in _DATASETS:
        raise KeyError(f"Unknown dataset {name!r}. Available: {', '.join(available())}.")
    path, kind, parse_dates = _DATASETS[name]
    if not path.exists():
        raise FileNotFoundError(
            f"{path.name} not found. Generate the synthetic data first:\n"
            f"    uv run python scripts/generate_synthetic_data.py"
        )
    if kind == "geojson":
        import geopandas as gpd

        return gpd.read_file(path)
    return pd.read_csv(path, parse_dates=parse_dates)


__all__ = ["load", "available"]
