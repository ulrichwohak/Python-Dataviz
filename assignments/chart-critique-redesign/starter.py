"""Create a baseline for legacy, ungraded redesign practice.

This is not a starter for the graded individual-figure assignment.

Run from the repository root:

    uv run python assignments/chart-critique-redesign/starter.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = REPO_ROOT / "data" / "processed" / "amazon_monthly.csv"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"


def main() -> None:
    """Aggregate monthly state spending_usd and export the baseline chart."""
    if not DATA_PATH.exists():
        raise SystemExit(
            "amazon_monthly.csv is missing. From the repository root, first run "
            "`uv run python scripts/fetch_data.py`."
        )

    dashboard = pd.read_csv(DATA_PATH, parse_dates=["month"])
    monthly = (
        dashboard.groupby(["month", "state"], as_index=False)["spending_usd"]
        .sum()
        .pivot(index="month", columns="state", values="spending_usd")
    )

    # This plot is intentionally a weak communication design. Its aggregation is valid.
    ax = monthly.plot(figsize=(11, 6), marker="o", colormap="rainbow", grid=True)
    ax.set_title("Sample spending by shipping state (USD)")
    ax.set_xlabel("Month")
    ax.set_ylabel("Sample spending (USD)")
    ax.legend(title="Shipping state")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "weak_chart.png"
    ax.figure.tight_layout()
    ax.figure.savefig(output_path, dpi=160)
    plt.close(ax.figure)
    print(f"Wrote {output_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
