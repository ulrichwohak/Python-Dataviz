"""Create numerical checks and reference figures for the three Power BI workshops."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = Path(__file__).resolve().parent / "output"


def main():
    OUTPUT.mkdir(exist_ok=True)
    data = pd.read_csv(ROOT / "data/processed/amazon_monthly.csv", parse_dates=["month"])
    monthly = data.groupby("month")["spending_usd"].sum()
    states = data.groupby("state")["spending_usd"].sum().sort_values()
    note = "Berke et al., donated Amazon histories, 2018–2022. Seven categories; not representative of all shoppers."
    for filename, kind, series, title in [
        ("python_monthly_spending.png", "line", monthly, "Monthly sample spending (USD)"),
        ("python_state_spending.png", "barh", states, "Sample spending by shipping state (USD)"),
    ]:
        fig, ax = plt.subplots(figsize=(10, 5 if kind == "line" else 12))
        series.plot(kind=kind, ax=ax, color="#176B73")
        ax.set_title(title)
        fig.text(0.01, 0.01, note, fontsize=8)
        fig.tight_layout(rect=(0, 0.05, 1, 1))
        fig.savefig(OUTPUT / filename, dpi=150)
        plt.close(fig)
    data.groupby("state")[["spending_usd", "quantity", "purchase_records"]].sum().to_csv(OUTPUT / "verification_totals.csv")
    rows = []
    for category in ["ALL", *sorted(data.category.unique())]:
        for year in ["ALL", 2018, 2019, 2020, 2021, 2022]:
            selected = data
            if category != "ALL":
                selected = selected.loc[selected.category == category]
            if year != "ALL":
                selected = selected.loc[selected.month.dt.year == year]
            rows.append({"category": category, "year": year, "aggregate_rows": len(selected),
                         "spending_usd": round(selected.spending_usd.sum(), 2),
                         "quantity": int(selected.quantity.sum()),
                         "purchase_records": int(selected.purchase_records.sum())})
    pd.DataFrame(rows).to_csv(OUTPUT / "verification_filters.csv", index=False)
    print(data[["spending_usd", "quantity", "purchase_records"]].sum())
    print(f"Wrote reference outputs to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
