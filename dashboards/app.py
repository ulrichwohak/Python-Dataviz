"""Streamlit dashboard built on the prepared dashboard dataset.

Run it with:

    uv run python scripts/fetch_data.py                # once, to create the data
    uv run streamlit run dashboards/app.py

The dashboard reads ``data/processed/dashboard.csv`` (month × region × product × channel) and
lets the user filter by region, product category, and channel, then shows headline KPIs and a
few interactive plotly charts.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# Make the installed helpers importable even when Streamlit runs the file directly.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from dataviz_course.utils import DATA_PROCESSED  # noqa: E402

st.set_page_config(page_title="Sales Dashboard", layout="wide")


@st.cache_data
def load_dashboard() -> pd.DataFrame:
    path = DATA_PROCESSED / "dashboard.csv"
    if not path.exists():
        st.error(
            "dashboard.csv not found. Generate it first:\n\n"
            "`uv run python scripts/fetch_data.py`"
        )
        st.stop()
    return pd.read_csv(path, parse_dates=["month"])


df = load_dashboard()

st.title("Sales Dashboard")
st.caption("Synthetic data — for teaching only. Filter on the left; charts update live.")

# --- Filters ---
with st.sidebar:
    st.header("Filters")
    regions = st.multiselect("Region", sorted(df["region"].unique()), default=list(sorted(df["region"].unique())))
    categories = st.multiselect(
        "Product category", sorted(df["product_category"].unique()),
        default=list(sorted(df["product_category"].unique())),
    )
    channels = st.multiselect("Channel", sorted(df["channel"].unique()), default=list(sorted(df["channel"].unique())))

mask = (
    df["region"].isin(regions)
    & df["product_category"].isin(categories)
    & df["channel"].isin(channels)
)
view = df[mask]

if view.empty:
    st.warning("No data for the current filter selection.")
    st.stop()

# --- KPIs ---
col1, col2, col3 = st.columns(3)
col1.metric("Total revenue", f"€{view['revenue'].sum():,.0f}")
col2.metric("Total units sold", f"{view['units_sold'].sum():,.0f}")
col3.metric("Avg campaign share", f"{view['campaign_share'].mean():.0%}")

# --- Charts ---
left, right = st.columns(2)

monthly = view.groupby("month", as_index=False)["revenue"].sum()
left.plotly_chart(
    px.line(monthly, x="month", y="revenue", title="Monthly revenue"),
    use_container_width=True,
)

by_region = view.groupby("region", as_index=False)["revenue"].sum().sort_values("revenue")
right.plotly_chart(
    px.bar(by_region, x="revenue", y="region", orientation="h", title="Revenue by region"),
    use_container_width=True,
)

by_cat = view.groupby(["month", "product_category"], as_index=False)["revenue"].sum()
st.plotly_chart(
    px.area(by_cat, x="month", y="revenue", color="product_category", title="Revenue by product category"),
    use_container_width=True,
)

with st.expander("Show filtered data"):
    st.dataframe(view, use_container_width=True)
