# Dashboards

An interactive **Streamlit** dashboard over the prepared dataset
(`data/processed/dashboard.csv`).

## Run it

```bash
uv run python scripts/fetch_data.py                # once, to create the data
uv run streamlit run dashboards/app.py
```

Streamlit opens a browser tab. Use the sidebar to filter by region, product category, and
channel; the KPIs and charts update live.

## Why Streamlit (not Voilà)?

The course uses **Streamlit** for the dashboard week because:

- It is a **standalone Python app** — no notebook server or `.ipynb` runtime required, so
  non-coders can use the result.
- The script-plus-widgets model (`st.multiselect`, `st.metric`, `st.plotly_chart`) is quick to
  teach and reads top-to-bottom like the notebooks students already know.
- It is cross-platform and installs cleanly via `uv` with no extra system dependencies.

Voilà renders an existing notebook as an app, which is convenient but ties the dashboard to
notebook internals and is harder to evolve into a real deliverable. Streamlit better matches
the goal of producing something a stakeholder could actually use.
