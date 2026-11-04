"""Focused Streamlit data story built on the prepared dashboard dataset.

Run it with:

    uv run python scripts/fetch_data.py                # once, to create the data
    uv run streamlit run dashboards/app.py

The app reads ``data/processed/amazon_monthly.csv`` (month × shipping state × category). Its one
selector answers a defined follow-up question while the all-state default remains meaningful.
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

BLUE = "#2F6690"
ACCENT = "#D1495B"

st.set_page_config(page_title="Sample spending story", layout="wide")


@st.cache_data
def load_dashboard() -> pd.DataFrame:
    path = DATA_PROCESSED / "amazon_monthly.csv"
    if not path.exists():
        st.error(
            "amazon_monthly.csv not found. Generate it first:\n\n"
            "`uv run python scripts/fetch_data.py`"
        )
        st.stop()
    return pd.read_csv(path, parse_dates=["month"])


df = load_dashboard()

st.title("How is sample spending changing—and what about my state?")
st.caption(
    "Berke et al., donated Amazon histories, 2018–2022. Seven categories; voluntary sample, not representative of all shoppers. "
    "Descriptive evidence only."
)

# One control, tied to one explicit follow-up question.
state_options = ["All states", *sorted(df["state"].unique())]
with st.sidebar:
    st.header("Follow-up view")
    selected_state = st.selectbox(
        "Which state should I inspect?",
        state_options,
        help="Choose one state or return to the all-state overview.",
    )

view = df if selected_state == "All states" else df.loc[df["state"].eq(selected_state)]
filter_note = "All states" if selected_state == "All states" else f"Shipping state: {selected_state}"
st.write(f"**Current view:** {filter_note}")

# --- KPIs ---
col1, col2, col3 = st.columns(3)
col1.metric("Sample spending in current view", f"${view['spending_usd'].sum():,.0f}")
col2.metric("Items purchased in current view", f"{view['quantity'].sum():,.0f}")
col3.metric("Months covered", f"{view['month'].nunique():,}")

# --- Charts ---
left, right = st.columns(2)

monthly = view.groupby("month", as_index=False)["spending_usd"].sum().sort_values("month")
monthly_title = (
    "Overall monthly sample spending"
    if selected_state == "All states"
    else f"Monthly sample spending in {selected_state}"
)
monthly_figure = px.line(
    monthly,
    x="month",
    y="spending_usd",
    title=monthly_title,
    labels={"month": "Month", "spending_usd": "Sample spending ($)"},
    color_discrete_sequence=[BLUE],
)
monthly_figure.update_layout(template="plotly_white", hovermode="x unified")
monthly_figure.update_traces(hovertemplate="%{x|%b %Y}<br>Sample spending: $%{y:,.0f}<extra></extra>")
left.plotly_chart(
    monthly_figure,
    width="stretch",
)

by_state = df.groupby("state", as_index=False)["spending_usd"].sum().sort_values("spending_usd")
bar_colours = [ACCENT if state == selected_state else BLUE for state in by_state["state"]]
state_figure = px.bar(
    by_state,
    x="spending_usd",
    y="state",
    orientation="h",
    title="Sample spending context across states",
    labels={"spending_usd": "Sample spending ($)", "state": ""},
)
state_figure.update_traces(
    marker_color=bar_colours,
    hovertemplate="%{y}<br>Sample spending: $%{x:,.0f}<extra></extra>",
)
state_figure.update_layout(template="plotly_white", showlegend=False, height=900)
right.plotly_chart(
    state_figure,
    width="stretch",
)

st.info(
    "Interpretation: use the line for change over time and the state bars for context. "
    "The selector changes the time series; it does not change the state benchmark."
)

with st.expander("Show filtered data"):
    st.dataframe(view, width="stretch")
