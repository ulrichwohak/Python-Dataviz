# Data

All datasets used in this course are **synthetic** and **generated**, not downloaded. They
are produced deterministically (fixed random seed) so every student gets identical data.

## How to (re)generate

```bash
uv run python scripts/fetch_data.py
```

This performs no network downloads in the prototype; it generates deterministic synthetic
data. It writes raw datasets to `data/raw/` and prepared datasets to `data/processed/`. Both
folders are git-ignored (except `.gitkeep`), so the data is never committed — regenerate it
after cloning. Notebooks read these **local** files; they never download data at runtime.

## Datasets

Generated into `data/raw/`:

| File | Grain | Key columns |
| --- | --- | --- |
| `sales.csv` | weekly × region × product × channel | `date, region, product_category, channel, revenue, units_sold, price, campaign_indicator` |
| `customers.csv` | one row per customer | `customer_id, age, income, segment, region, acquisition_channel, churn_probability, customer_lifetime_value` |
| `transactions.csv` | one row per transaction | `transaction_id, customer_id, date, product_category, revenue, discount, quantity` |
| `operations.csv` | one row per employee | `department, tenure, satisfaction_score, monthly_performance, training_hours` |
| `regions.geojson` | one polygon per region | `region_id, region_name, geometry, population, average_income, sales_per_capita` |
| `stores.geojson` | one point per store | `store_id, region_id, store_name, geometry, monthly_revenue` |

Generated into `data/processed/`:

| File | Description |
| --- | --- |
| `dashboard.csv` | Tidy table combining time, region, product category, and channel sales metrics — the basis for the dashboard and interactive notebooks. |

## Built-in imperfections

To make the visualisations realistic, the generated data deliberately includes missing
values, outliers, skewed variables, seasonality and trend, and group differences. The exact
data-generating process is documented in
[`src/dataviz_course/synthetic_data.py`](../src/dataviz_course/synthetic_data.py).
