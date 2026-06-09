"""Reusable plotting style and small chart helpers.

The goal is a consistent "house style" across all eight weeks so students focus on the chart
choices rather than rcParams boilerplate, plus a couple of helpers that encode good defaults
(sorted bars, value labels, thousands separators).
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

# A calm, colour-blind-friendly categorical palette used throughout the course.
HOUSE_PALETTE = [
    "#4C72B0",  # blue
    "#DD8452",  # orange
    "#55A868",  # green
    "#C44E52",  # red
    "#8172B3",  # purple
    "#937860",  # brown
]


def set_house_style() -> None:
    """Apply the course-wide matplotlib/seaborn style. Call once near the top of a notebook."""
    sns.set_theme(style="whitegrid", palette=HOUSE_PALETTE)
    plt.rcParams.update(
        {
            "figure.figsize": (8, 5),
            "figure.dpi": 110,
            "axes.titlesize": 14,
            "axes.titleweight": "bold",
            "axes.labelsize": 12,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "font.size": 11,
        }
    )


def thousands(axis) -> None:
    """Format an axis (e.g. ``ax.yaxis``) with thousands separators: 1200000 -> 1,200,000."""
    axis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))


def currency(axis, symbol: str = "€") -> None:
    """Format an axis as currency, e.g. ``€1,200,000``."""
    axis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{symbol}{x:,.0f}"))


def labelled_barh(ax, labels, values, *, fmt: str = "{:,.0f}", color: str | None = None):
    """Draw a horizontal bar chart sorted by value, with a value label on each bar.

    A small reusable helper because "sorted bars with labels" is the single most common
    business chart and is easy to get subtly wrong (unsorted, unlabelled).
    """
    order = sorted(range(len(values)), key=lambda i: values[i])
    labels = [labels[i] for i in order]
    values = [values[i] for i in order]
    bars = ax.barh(labels, values, color=color or HOUSE_PALETTE[0])
    span = max(values) - min(0, min(values)) or 1
    for bar, value in zip(bars, values, strict=True):
        ax.text(
            bar.get_width() + span * 0.01,
            bar.get_y() + bar.get_height() / 2,
            fmt.format(value),
            va="center",
            fontsize=10,
        )
    ax.margins(x=0.15)
    return bars


__all__ = [
    "HOUSE_PALETTE",
    "set_house_style",
    "thousands",
    "currency",
    "labelled_barh",
]
