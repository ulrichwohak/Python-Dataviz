"""Deterministic synthetic datasets for the course.

Everything here is fake but plausible. The data-generating process (DGP) is documented inline
so students can reason about *why* a chart looks the way it does. All randomness flows from a
single integer ``seed`` (default :data:`dataviz_course.utils.SEED`), so every machine produces
byte-identical CSVs.

Deliberate imperfections are baked in — missing values, outliers, skew, seasonality, trend,
and group differences — because real business data is never clean and visualisation is partly
about spotting these things.

Public entry point: :func:`generate_all`, also exposed via
``scripts/generate_synthetic_data.py``.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from .utils import DATA_PROCESSED, DATA_RAW, SEED, ensure_data_dirs

# --- Shared category vocabularies (kept consistent across datasets so they can be joined) ---
REGIONS = ["North", "South", "East", "West", "Central", "Coastal"]
PRODUCT_CATEGORIES = ["Electronics", "Apparel", "Home", "Grocery"]
CHANNELS = ["Online", "Retail", "Partner"]
SEGMENTS = ["Value", "Mainstream", "Premium"]
ACQUISITION_CHANNELS = ["Organic", "Paid Search", "Referral", "Social"]
DEPARTMENTS = ["Sales", "Engineering", "Support", "Operations", "Marketing"]


# --------------------------------------------------------------------------------------------
# 1. Weekly sales time series
# --------------------------------------------------------------------------------------------
def make_sales(seed: int = SEED) -> pd.DataFrame:
    """Weekly revenue per region × product × channel over two years.

    DGP: a per-cell base level (region, product, and channel multipliers) scaled by a gentle
    upward **trend**, an annual **seasonality** sine wave with a Nov/Dec holiday bump, a random
    **campaign** uplift (~15% of weeks, +40% revenue), and lognormal multiplicative noise.
    Imperfections: ~1% missing ``revenue`` and ~0.2% extreme high outliers.
    """
    rng = np.random.default_rng(seed)
    weeks = pd.date_range("2023-01-02", periods=104, freq="W-MON")

    region_mult = dict(zip(REGIONS, [1.2, 0.9, 1.0, 0.8, 1.3, 0.7], strict=True))
    product_base = {"Electronics": 18000, "Apparel": 9000, "Home": 12000, "Grocery": 15000}
    product_price = {"Electronics": 220.0, "Apparel": 45.0, "Home": 80.0, "Grocery": 12.0}
    channel_mult = {"Online": 1.1, "Retail": 1.0, "Partner": 0.6}

    records = []
    for i, date in enumerate(weeks):
        trend = 1 + 0.004 * i
        season = 1 + 0.25 * np.sin(2 * np.pi * date.dayofyear / 365.25)
        if date.month in (11, 12):
            season *= 1.25
        for region in REGIONS:
            for product in PRODUCT_CATEGORIES:
                for channel in CHANNELS:
                    campaign = int(rng.random() < 0.15)
                    base = product_base[product] * region_mult[region] * channel_mult[channel]
                    revenue = base * trend * season * (1 + 0.4 * campaign) * rng.lognormal(0, 0.15)
                    price = product_price[product] * rng.normal(1.0, 0.03)
                    units = max(0.0, revenue / price + rng.normal(0, 5))
                    records.append(
                        (date, region, product, channel, revenue, units, price, campaign)
                    )

    df = pd.DataFrame(
        records,
        columns=[
            "date", "region", "product_category", "channel",
            "revenue", "units_sold", "price", "campaign_indicator",
        ],
    )
    # Outliers, then missing (so some outliers are also hidden by missingness — realistic).
    outlier = rng.random(len(df)) < 0.002
    df.loc[outlier, "revenue"] *= rng.uniform(5, 9, int(outlier.sum()))
    missing = rng.random(len(df)) < 0.01
    df.loc[missing, "revenue"] = np.nan

    df["revenue"] = df["revenue"].round(2)
    df["units_sold"] = df["units_sold"].round().astype("Int64")
    df["price"] = df["price"].round(2)
    return df


# --------------------------------------------------------------------------------------------
# 2. Customer table
# --------------------------------------------------------------------------------------------
def make_customers(n: int = 2000, seed: int = SEED) -> pd.DataFrame:
    """One row per customer with skewed income and segment-driven churn / lifetime value.

    DGP: ``segment`` is sampled with class imbalance; ``income`` is **lognormal** (right-skewed)
    with a segment-dependent scale; ``churn_probability`` has a segment baseline plus noise;
    ``customer_lifetime_value`` rises with income and falls with churn. Imperfections: ~3%
    missing ``income`` and a handful of ultra-high income outliers.
    """
    rng = np.random.default_rng(seed + 1)
    segment = rng.choice(SEGMENTS, size=n, p=[0.5, 0.35, 0.15])
    income_scale = {"Value": 35_000, "Mainstream": 60_000, "Premium": 120_000}
    base_churn = {"Value": 0.35, "Mainstream": 0.20, "Premium": 0.10}

    income = np.array([income_scale[s] for s in segment]) * rng.lognormal(0, 0.4, n)
    churn = np.clip(
        np.array([base_churn[s] for s in segment]) + rng.normal(0, 0.08, n), 0.01, 0.95
    )
    clv_factor = {"Value": 1.5, "Mainstream": 2.5, "Premium": 4.0}
    seg_factor = np.array([clv_factor[s] for s in segment])
    clv = income * 0.05 * seg_factor * (1 - churn) * rng.lognormal(0, 0.2, n)

    df = pd.DataFrame(
        {
            "customer_id": [f"C{i:05d}" for i in range(1, n + 1)],
            "age": np.clip(rng.normal(42, 13, n), 18, 85).round().astype(int),
            "income": income,
            "segment": segment,
            "region": rng.choice(REGIONS, size=n),
            "acquisition_channel": rng.choice(ACQUISITION_CHANNELS, size=n),
            "churn_probability": churn.round(3),
            "customer_lifetime_value": clv,
        }
    )
    outlier = rng.random(n) < 0.01
    df.loc[outlier, "income"] *= rng.uniform(3, 6, int(outlier.sum()))
    missing = rng.random(n) < 0.03
    df.loc[missing, "income"] = np.nan
    df["income"] = df["income"].round(0)
    df["customer_lifetime_value"] = df["customer_lifetime_value"].round(2)
    return df


# --------------------------------------------------------------------------------------------
# 3. Transaction table (depends on the customer table)
# --------------------------------------------------------------------------------------------
def make_transactions(customers: pd.DataFrame, seed: int = SEED) -> pd.DataFrame:
    """One row per transaction; transaction counts scale with customer segment.

    DGP: each customer makes a Poisson number of purchases (Premium buy more often); each line
    has a ``product_category``, a ``quantity``, a ``discount`` (mostly zero, occasionally up to
    40%), and a ``revenue`` derived from a per-category price × quantity × (1 − discount).
    """
    rng = np.random.default_rng(seed + 2)
    price = {"Electronics": 220.0, "Apparel": 45.0, "Home": 80.0, "Grocery": 12.0}
    seg_rate = {"Value": 1.5, "Mainstream": 3.0, "Premium": 6.0}
    dates = pd.date_range("2023-01-01", "2024-12-31", freq="D")

    rows = []
    tid = 1
    for cust_id, segment in zip(customers["customer_id"], customers["segment"], strict=True):
        n_tx = rng.poisson(seg_rate[segment])
        for _ in range(n_tx):
            product = rng.choice(PRODUCT_CATEGORIES)
            quantity = int(rng.integers(1, 6))
            discount = float(rng.choice([0.0, 0.0, 0.0, 0.1, 0.2, 0.4], p=[0.55, 0.15, 0.1, 0.1, 0.07, 0.03]))
            unit = price[product] * rng.normal(1.0, 0.05)
            revenue = max(0.0, unit * quantity * (1 - discount))
            rows.append(
                (f"T{tid:06d}", cust_id, rng.choice(dates), product, round(revenue, 2), discount, quantity)
            )
            tid += 1

    return pd.DataFrame(
        rows,
        columns=["transaction_id", "customer_id", "date", "product_category", "revenue", "discount", "quantity"],
    ).sort_values("date").reset_index(drop=True)


# --------------------------------------------------------------------------------------------
# 4. Operations / employee table (built for distributions and comparisons)
# --------------------------------------------------------------------------------------------
def make_operations(n: int = 600, seed: int = SEED) -> pd.DataFrame:
    """One row per employee, shaped for box / violin plots and group comparison.

    DGP: ``department`` drives clear group differences in ``monthly_performance`` and
    ``satisfaction_score``; ``tenure`` is **exponential** (right-skewed); ``training_hours`` is
    **gamma**. Imperfections: performance outliers and ~4% missing ``satisfaction_score``.
    """
    rng = np.random.default_rng(seed + 3)
    department = rng.choice(DEPARTMENTS, size=n, p=[0.3, 0.2, 0.2, 0.2, 0.1])
    perf_mean = {"Sales": 72, "Engineering": 80, "Support": 68, "Operations": 70, "Marketing": 74}
    sat_mean = {"Sales": 6.5, "Engineering": 7.2, "Support": 5.8, "Operations": 6.0, "Marketing": 7.0}

    performance = np.array([perf_mean[d] for d in department]) + rng.normal(0, 8, n)
    satisfaction = np.clip(np.array([sat_mean[d] for d in department]) + rng.normal(0, 1.2, n), 1, 10)

    df = pd.DataFrame(
        {
            "employee_id": [f"E{i:04d}" for i in range(1, n + 1)],
            "department": department,
            "tenure": np.round(rng.exponential(4.0, n), 1),
            "satisfaction_score": satisfaction.round(1),
            "monthly_performance": performance.round(1),
            "training_hours": np.round(rng.gamma(2.0, 6.0, n), 1),
        }
    )
    outlier = rng.random(n) < 0.02
    df.loc[outlier, "monthly_performance"] *= rng.uniform(1.3, 1.8, int(outlier.sum()))
    df["monthly_performance"] = df["monthly_performance"].round(1)
    missing = rng.random(n) < 0.04
    df.loc[missing, "satisfaction_score"] = np.nan
    return df


# --------------------------------------------------------------------------------------------
# 5. Geospatial: synthetic region polygons and store points
# --------------------------------------------------------------------------------------------
def make_geodata(seed: int = SEED):
    """Build artificial region polygons and store points (no external shapefiles).

    A 3×2 grid of square regions is laid out in EPSG:4326 over a plausible degree range, so
    week 6 can demonstrate reprojection to a projected CRS. Returns ``(regions_gdf, stores_gdf)``.
    """
    import geopandas as gpd
    from shapely.geometry import Point, Polygon

    rng = np.random.default_rng(seed + 4)
    lons = np.linspace(10.0, 16.0, 4)  # 3 columns
    lats = np.linspace(46.0, 50.0, 3)  # 2 rows

    region_rows = []
    cells = [(c, r) for r in range(2) for c in range(3)]
    for region, (c, r) in zip(REGIONS, cells, strict=True):
        poly = Polygon(
            [
                (lons[c], lats[r]),
                (lons[c + 1], lats[r]),
                (lons[c + 1], lats[r + 1]),
                (lons[c], lats[r + 1]),
            ]
        )
        population = int(rng.integers(150_000, 1_200_000))
        average_income = round(float(rng.normal(48_000, 9_000)), 0)
        sales_per_capita = round(float(rng.normal(900, 250)), 2)
        region_rows.append(
            {
                "region_id": f"R{c + 3 * r + 1}",
                "region_name": region,
                "population": population,
                "average_income": average_income,
                "sales_per_capita": sales_per_capita,
                "geometry": poly,
            }
        )
    regions = gpd.GeoDataFrame(region_rows, crs="EPSG:4326")

    store_rows = []
    sid = 1
    for _, reg in regions.iterrows():
        minx, miny, maxx, maxy = reg.geometry.bounds
        n_stores = int(rng.integers(4, 9))
        for _ in range(n_stores):
            pt = Point(rng.uniform(minx, maxx), rng.uniform(miny, maxy))
            store_rows.append(
                {
                    "store_id": f"S{sid:03d}",
                    "region_id": reg["region_id"],
                    "store_name": f"{reg['region_name']} #{sid:03d}",
                    "monthly_revenue": round(float(rng.normal(120_000, 35_000)), 2),
                    "geometry": pt,
                }
            )
            sid += 1
    stores = gpd.GeoDataFrame(store_rows, crs="EPSG:4326")
    return regions, stores


# --------------------------------------------------------------------------------------------
# 6. Prepared dashboard table (processed)
# --------------------------------------------------------------------------------------------
def make_dashboard(sales: pd.DataFrame) -> pd.DataFrame:
    """Aggregate weekly sales to a monthly tidy table for filtering in the dashboard.

    Combines time (month), geography (region), product category, and channel with summed
    revenue / units and a campaign share — exactly the shape a dashboard's filters expect.
    """
    df = sales.dropna(subset=["revenue"]).copy()
    df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()
    grouped = (
        df.groupby(["month", "region", "product_category", "channel"], as_index=False)
        .agg(
            revenue=("revenue", "sum"),
            units_sold=("units_sold", "sum"),
            avg_price=("price", "mean"),
            campaign_share=("campaign_indicator", "mean"),
        )
    )
    grouped["revenue"] = grouped["revenue"].round(2)
    grouped["avg_price"] = grouped["avg_price"].round(2)
    grouped["campaign_share"] = grouped["campaign_share"].round(3)
    return grouped


# --------------------------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------------------------
def generate_all(seed: int = SEED, *, raw_dir: Path = DATA_RAW, processed_dir: Path = DATA_PROCESSED) -> dict[str, Path]:
    """Generate every dataset and write it to ``data/raw`` and ``data/processed``.

    Returns a mapping of dataset name -> written path. Deterministic for a given ``seed``.
    """
    ensure_data_dirs()
    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)

    sales = make_sales(seed)
    customers = make_customers(seed=seed)
    transactions = make_transactions(customers, seed=seed)
    operations = make_operations(seed=seed)
    regions, stores = make_geodata(seed)
    dashboard = make_dashboard(sales)

    written: dict[str, Path] = {}

    def _csv(df: pd.DataFrame, path: Path) -> None:
        df.to_csv(path, index=False)
        written[path.stem] = path

    _csv(sales, raw_dir / "sales.csv")
    _csv(customers, raw_dir / "customers.csv")
    _csv(transactions, raw_dir / "transactions.csv")
    _csv(operations, raw_dir / "operations.csv")
    _csv(dashboard, processed_dir / "dashboard.csv")

    regions.to_file(raw_dir / "regions.geojson", driver="GeoJSON")
    written["regions"] = raw_dir / "regions.geojson"
    stores.to_file(raw_dir / "stores.geojson", driver="GeoJSON")
    written["stores"] = raw_dir / "stores.geojson"

    return written


__all__ = [
    "REGIONS", "PRODUCT_CATEGORIES", "CHANNELS", "SEGMENTS",
    "ACQUISITION_CHANNELS", "DEPARTMENTS",
    "make_sales", "make_customers", "make_transactions", "make_operations",
    "make_geodata", "make_dashboard", "generate_all",
]
