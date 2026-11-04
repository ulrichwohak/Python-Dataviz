# Dashboards

A focused **Streamlit** data story over the prepared dataset
(`data/processed/amazon_monthly.csv`). It is optional companion material; the scheduled Sessions 4–6 use Power BI.

## Run it

```bash
uv run python scripts/fetch_data.py                # once, to create the data
uv run streamlit run dashboards/app.py
```

Streamlit opens a browser tab. The default view shows spending in the donated Amazon sample;
one shipping-state selector supports the follow-up “what about my state?” The summary cards
and monthly line update together. The state bars retain the all-state benchmark and highlight
the selected state. Selecting “All states” restores the overview.

The app is deliberately small. Its purpose is to demonstrate an interaction contract, visible
filter state, clear units, restrained visual hierarchy, and a reproducible Python delivery path.
The Power BI workshops in [`workshops/power-bi/`](../workshops/power-bi/) use the same
prepared data to compare those principles across tools.

The app reads a prepared historical CSV and responds to the state selector. It does not
collect new data or refresh automatically.

## Why Streamlit (not Voilà)?

The optional Python companion uses **Streamlit** because:

- It is a **standalone Python app** — no notebook server or `.ipynb` runtime required, so
  non-coders can use the result.
- The script-plus-widgets model (`st.multiselect`, `st.metric`, `st.plotly_chart`) is quick to
  teach and reads top-to-bottom like the notebooks students already know.
- It is cross-platform and installs cleanly via `uv` with no extra system dependencies.

Voilà renders an existing notebook as an app, which is convenient but ties the dashboard to
notebook internals and is harder to evolve into a real deliverable. Streamlit better matches
the goal of producing something a stakeholder could actually use.
