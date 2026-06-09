"""Generate the course notebooks programmatically.

For each of the eight weeks this emits three notebooks from a single specification, so the
variants never drift apart:

  notebooks/live/        skeleton the instructor fills in live (plotting cells are TODO stubs)
  notebooks/completed/   fully developed reference (all cells filled, outputs cleared)
  notebooks/exercises/   practice tasks with empty answer cells

Edit the WEEKS specification below — never the generated .ipynb JSON — then run:

    uv run python scripts/build_notebooks.py

Every completed notebook follows the same pedagogical shape: motivating business question,
learning objectives, setup, data loading, a concept explanation, plots built step by step with
interpretation, "pause and predict", common mistakes, an AI co-pilot activity, a verification
checklist, and exercises. Each saves at least one figure to figures/.
"""

from __future__ import annotations

from pathlib import Path

import nbformat as nbf
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

ROOT = Path(__file__).resolve().parent.parent
NB = ROOT / "notebooks"

# Shared setup cell used by every notebook (imports + house style).
SETUP = """\
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from dataviz_course import load, save_figure, set_house_style

set_house_style()
"""

# Standard AI co-pilot + verification blocks, lightly customised per week via {topic}.
AI_COPILOT = """\
## AI co-pilot activity

Ask an AI assistant: *"{prompt}"* Paste its code into a new cell and run it.

Then **do not trust it yet** — work through the verification checklist below before you keep it.
"""

VERIFICATION = """\
## Verification checklist for AI output

Before relying on any chart or code an assistant gives you, confirm:

1. Does the chart actually answer *{question}*?
2. Are the axes, units, and scale correct and honest?
3. Is this the right chart type for the data?
4. Did the code run on **our** dataset (correct columns, no invented data)?
5. Were rows silently dropped, duplicated, or mis-aggregated?
6. Could the colour, ordering, or missing context mislead a reader?

If you cannot answer all six, fix it before moving on.
"""


def _objectives_md(items: list[str]) -> str:
    bullets = "\n".join(f"- {o}" for o in items)
    return f"## Learning objectives\n\nBy the end of this session you should be able to:\n\n{bullets}"


def _exercises_md(items: list[str]) -> str:
    body = "\n".join(f"{i}. {t}" for i, t in enumerate(items, 1))
    return f"## Exercises\n\n{body}"


def _header_md(week: dict, kind: str) -> str:
    suffix = {"live": " (live skeleton)", "completed": "", "exercises": " — Exercises"}[kind]
    return (
        f"# {week['title']}{suffix}\n\n"
        f"**Business question.** {week['question']}\n\n"
        f"*Datasets:* `{'`, `'.join(week['datasets'])}`  ·  "
        f"*Run `uv run python scripts/fetch_data.py` first if you have not.*"
    )


def _new_nb() -> nbf.NotebookNode:
    nb = new_notebook()
    nb.metadata = {
        "kernelspec": {"name": "python3", "display_name": "Python 3 (ipykernel)", "language": "python"},
        "language_info": {"name": "python", "version": "3.12"},
    }
    return nb


def build_completed(week: dict) -> nbf.NotebookNode:
    nb = _new_nb()
    cells = [
        new_markdown_cell(_header_md(week, "completed")),
        new_markdown_cell(_objectives_md(week["objectives"])),
        new_markdown_cell("## Setup"),
        new_code_cell(SETUP),
        new_markdown_cell(week["concept"]),
        new_markdown_cell("## Load the data"),
        new_code_cell(week["load_code"]),
    ]
    for step in week["steps"]:
        cells.append(new_markdown_cell(f"### {step['title']}\n\n{step['md']}"))
        cells.append(new_code_cell(step["code"]))
    cells.append(new_markdown_cell(week["pause"]))
    cells.append(new_markdown_cell(week["mistakes"]))
    cells.append(new_markdown_cell(AI_COPILOT.format(prompt=week["ai_prompt"])))
    cells.append(new_markdown_cell(VERIFICATION.format(question=week["short_question"])))
    cells.append(new_markdown_cell(_exercises_md(week["exercises"])))
    nb.cells = cells
    return nb


def build_live(week: dict) -> nbf.NotebookNode:
    nb = _new_nb()
    cells = [
        new_markdown_cell(_header_md(week, "live")),
        new_markdown_cell(_objectives_md(week["objectives"])),
        new_markdown_cell("## Setup"),
        new_code_cell(SETUP),
        new_markdown_cell(week["concept"]),
        new_markdown_cell("## Load the data"),
        new_code_cell(week["load_code"]),
    ]
    for step in week["steps"]:
        cells.append(new_markdown_cell(f"### {step['title']}\n\n{step['md']}"))
        cells.append(new_code_cell(f"# TODO (live): build {step['title'].lower()}\n"))
    cells.append(new_markdown_cell(week["pause"]))
    cells.append(new_markdown_cell(week["mistakes"]))
    cells.append(new_markdown_cell(AI_COPILOT.format(prompt=week["ai_prompt"])))
    cells.append(new_markdown_cell(VERIFICATION.format(question=week["short_question"])))
    cells.append(new_markdown_cell(_exercises_md(week["exercises"])))
    nb.cells = cells
    return nb


def build_exercises(week: dict) -> nbf.NotebookNode:
    nb = _new_nb()
    cells = [
        new_markdown_cell(_header_md(week, "exercises")),
        new_markdown_cell(_objectives_md(week["objectives"])),
        new_markdown_cell("## Setup"),
        new_code_cell(SETUP),
        new_code_cell(week["load_code"]),
    ]
    for i, task in enumerate(week["exercises"], 1):
        cells.append(new_markdown_cell(f"### Exercise {i}\n\n{task}"))
        cells.append(new_code_cell("# Your answer here\n"))
    nb.cells = cells
    return nb


# ============================================================================================
# Per-week content
# ============================================================================================
WEEKS: list[dict] = [
    # ---------------------------------------------------------------- Week 1
    {
        "num": 1,
        "slug": "intro_to_visualisation",
        "title": "Week 1 — Introduction to Visualisation",
        "question": "Is our business growing, and where does the revenue come from?",
        "short_question": "is the business growing, and where does revenue come from",
        "datasets": ["sales"],
        "objectives": [
            "Explain why we visualise data instead of reading tables.",
            "Identify the anatomy of a chart (axes, marks, encodings, labels).",
            "Build a first line chart and bar chart with matplotlib.",
            "Choose between a line and a bar chart for a given question.",
        ],
        "concept": (
            "## Why visualise?\n\n"
            "A table of 7,000 weekly sales rows hides the story; a single line shows the trend at "
            "a glance. Every chart **encodes** data values as visual properties — position, length, "
            "colour. Good charts pick encodings the eye reads accurately: *position* and *length* "
            "are read best, which is why lines and bars dominate business reporting."
        ),
        "load_code": 'sales = load("sales")\nsales.head()',
        "steps": [
            {
                "title": "A line chart for trend over time",
                "md": "We sum revenue across all regions and channels to one number per week, then "
                      "plot it over time. **Position** along the x-axis encodes time; position on "
                      "the y-axis encodes revenue.",
                "code": (
                    'weekly = sales.groupby("date", as_index=False)["revenue"].sum()\n\n'
                    "fig, ax = plt.subplots()\n"
                    'ax.plot(weekly["date"], weekly["revenue"], color="#4C72B0")\n'
                    'ax.set_title("Total weekly revenue is trending up")\n'
                    'ax.set_xlabel("Week")\n'
                    'ax.set_ylabel("Revenue (€)")\n'
                    "fig.autofmt_xdate()\n"
                    "plt.show()"
                ),
            },
            {
                "title": "A bar chart for comparing categories",
                "md": "To compare *categories* (regions) rather than a trend, length-encoded bars "
                      "are clearer than a line. We sort the bars so the ranking is obvious, and "
                      "save the figure to `figures/`.",
                "code": (
                    'by_region = sales.groupby("region")["revenue"].sum().sort_values()\n\n'
                    "fig, ax = plt.subplots()\n"
                    "ax.barh(by_region.index, by_region.values, color=\"#4C72B0\")\n"
                    'ax.set_title("Total revenue by region")\n'
                    'ax.set_xlabel("Revenue (€)")\n'
                    'save_figure(fig, "week01_revenue_by_region")\n'
                    "plt.show()"
                ),
            },
        ],
        "pause": (
            "## Pause and predict\n\n"
            "Before running the next cell, predict: which region will have the **highest** total "
            "revenue, and roughly how does the weekly line behave near the end of each year? "
            "Write your guess down, then check it against the charts above."
        ),
        "mistakes": (
            "## Common mistakes\n\n"
            "- **Unsorted bars.** Leaving regions in data order makes the ranking hard to read — "
            "always sort categorical bars by value.\n"
            "- **Truncated y-axis.** Starting a bar chart's axis above zero exaggerates differences.\n"
            "- **Line chart for unordered categories.** A line implies continuity; never use one to "
            "compare regions."
        ),
        "ai_prompt": "Plot total revenue by product_category from a pandas DataFrame called sales",
        "exercises": [
            "Plot total weekly `units_sold` over time. How does its shape compare to the revenue line?",
            "Make a sorted bar chart of total revenue by `channel`. Which channel leads?",
            "The revenue line is noisy. Add a 4-week rolling mean as a second line and label both.",
        ],
    },
    # ---------------------------------------------------------------- Week 2
    {
        "num": 2,
        "slug": "data_for_visualisation",
        "title": "Week 2 — Data for Visualisation",
        "question": "How do we reshape raw transactions into something we can chart?",
        "short_question": "how revenue is distributed across categories and months",
        "datasets": ["transactions", "customers"],
        "objectives": [
            "Describe tidy data and why charting libraries expect it.",
            "Aggregate and reshape with groupby and pivot_table.",
            "Detect and handle missing values before plotting.",
            "Turn a transaction log into a monthly category trend.",
        ],
        "concept": (
            "## Tidy data\n\n"
            "Most plotting bugs are really *data shape* bugs. **Tidy data** means one row per "
            "observation and one column per variable. `groupby` collapses rows to a summary; "
            "`pivot_table` reshapes long data into a grid (e.g. month × category) that maps "
            "directly onto a multi-series chart. Missing values must be handled *before* plotting, "
            "or they silently distort it."
        ),
        "load_code": (
            'transactions = load("transactions")\n'
            'customers = load("customers")\n'
            "transactions.head()"
        ),
        "steps": [
            {
                "title": "Aggregate with groupby",
                "md": "Collapse the transaction log to total revenue per product category — one "
                      "number per group.",
                "code": (
                    'by_cat = (transactions.groupby("product_category", as_index=False)["revenue"]\n'
                    '          .sum().sort_values("revenue"))\n\n'
                    "fig, ax = plt.subplots()\n"
                    'ax.barh(by_cat["product_category"], by_cat["revenue"], color="#55A868")\n'
                    'ax.set_title("Revenue by product category")\n'
                    'ax.set_xlabel("Revenue (€)")\n'
                    "plt.show()"
                ),
            },
            {
                "title": "Reshape with pivot_table",
                "md": "Derive a `month` column, then pivot to month × category so each category "
                      "becomes its own line.",
                "code": (
                    "tx = transactions.copy()\n"
                    'tx["month"] = tx["date"].dt.to_period("M").dt.to_timestamp()\n'
                    'pivot = tx.pivot_table(index="month", columns="product_category",\n'
                    '                       values="revenue", aggfunc="sum")\n\n'
                    "fig, ax = plt.subplots()\n"
                    "pivot.plot(ax=ax)\n"
                    'ax.set_title("Monthly revenue by category")\n'
                    'ax.set_ylabel("Revenue (€)")\n'
                    'save_figure(fig, "week02_monthly_by_category")\n'
                    "plt.show()"
                ),
            },
            {
                "title": "Handle missing values",
                "md": "`income` has missing entries. Count them, then drop those rows *only for "
                      "this chart* — and say so in the title so the reader knows.",
                "code": (
                    'print("Missing income values:", customers["income"].isna().sum())\n'
                    'clean = customers.dropna(subset=["income"])\n\n'
                    "fig, ax = plt.subplots()\n"
                    'ax.hist(clean["income"], bins=40, color="#DD8452")\n'
                    'ax.set_title("Customer income (rows with missing income dropped)")\n'
                    'ax.set_xlabel("Income (€)")\n'
                    "plt.show()"
                ),
            },
        ],
        "pause": (
            "## Pause and predict\n\n"
            "Before plotting the pivot: will the four category lines move together or diverge? "
            "Which category do you expect on top? Then check whether dropping missing incomes "
            "changed the *shape* of the income distribution or just its count."
        ),
        "mistakes": (
            "## Common mistakes\n\n"
            "- **Plotting before aggregating.** Passing 8,000 raw rows to a line plot yields a "
            "spiky mess; summarise first.\n"
            "- **`mean` vs `sum`.** `pivot_table` defaults to `mean`; pick the aggregation on "
            "purpose.\n"
            "- **Silent NaNs.** Some plots drop missing values without telling you — always count "
            "them yourself first."
        ),
        "ai_prompt": "Pivot a transactions DataFrame to a month-by-channel table of total revenue",
        "exercises": [
            "Build a month × `channel` pivot of total revenue and plot it. (Hint: join `customers` "
            "to get each transaction's region or channel if needed, or use `product_category`.)",
            "Compute the share of revenue that comes with a non-zero `discount`. Visualise it.",
            "Replace missing `income` with the segment median instead of dropping it. Does the "
            "histogram change?",
        ],
    },
    # ---------------------------------------------------------------- Week 3
    {
        "num": 3,
        "slug": "core_business_charts",
        "title": "Week 3 — Core Business Charts",
        "question": "How do channels and regions contribute to revenue over time?",
        "short_question": "how channels and regions contribute to revenue",
        "datasets": ["sales"],
        "objectives": [
            "Build multi-series line charts for time trends.",
            "Compare groups with grouped and stacked bar charts.",
            "Know when stacking helps and when it misleads.",
            "Use small multiples to compare many series fairly.",
        ],
        "concept": (
            "## The core four\n\n"
            "Most business reporting is line charts (trend), grouped bars (compare levels), "
            "stacked bars (compose a total), and small multiples (compare many series without "
            "overplotting). Each answers a different question; choosing wrongly is the most common "
            "charting error in industry."
        ),
        "load_code": 'sales = load("sales")\nsales = sales.dropna(subset=["revenue"])\nsales.head()',
        "steps": [
            {
                "title": "Multi-series line by channel",
                "md": "Aggregate to monthly revenue per channel and draw one line each.",
                "code": (
                    'm = sales.assign(month=sales["date"].dt.to_period("M").dt.to_timestamp())\n'
                    'by_channel = m.pivot_table(index="month", columns="channel",\n'
                    '                           values="revenue", aggfunc="sum")\n\n'
                    "fig, ax = plt.subplots()\n"
                    "by_channel.plot(ax=ax)\n"
                    'ax.set_title("Monthly revenue by channel")\n'
                    'ax.set_ylabel("Revenue (€)")\n'
                    "plt.show()"
                ),
            },
            {
                "title": "Grouped vs stacked bars",
                "md": "Grouped bars compare regions *within* a channel; stacked bars show how "
                      "channels compose each region's total. Same data, different question.",
                "code": (
                    'grp = sales.groupby(["region", "channel"])["revenue"].sum().unstack()\n\n'
                    "fig, axes = plt.subplots(1, 2, figsize=(12, 5))\n"
                    'grp.plot(kind="bar", ax=axes[0])\n'
                    'axes[0].set_title("Grouped: compare regions")\n'
                    'grp.plot(kind="bar", stacked=True, ax=axes[1])\n'
                    'axes[1].set_title("Stacked: compose the total")\n'
                    "for a in axes:\n"
                    '    a.set_ylabel("Revenue (€)")\n'
                    "    a.tick_params(axis=\"x\", rotation=0)\n"
                    'save_figure(fig, "week03_grouped_vs_stacked")\n'
                    "plt.show()"
                ),
            },
            {
                "title": "Small multiples",
                "md": "When series overlap too much, give each its own panel. Seaborn's `relplot` "
                      "with `col=` builds the grid for us.",
                "code": (
                    "import seaborn as sns\n\n"
                    'monthly = (sales.assign(month=sales["date"].dt.to_period("M").dt.to_timestamp())\n'
                    '           .groupby(["month", "product_category"], as_index=False)["revenue"].sum())\n'
                    'g = sns.relplot(data=monthly, x="month", y="revenue", col="product_category",\n'
                    '                col_wrap=2, kind="line", height=2.8)\n'
                    'g.set_axis_labels("Month", "Revenue (€)")\n'
                    "plt.show()"
                ),
            },
        ],
        "pause": (
            "## Pause and predict\n\n"
            "Look at the grouped bars: which region depends most on the Partner channel? Predict, "
            "then read it off the stacked version. Which of the two made your answer easier?"
        ),
        "mistakes": (
            "## Common mistakes\n\n"
            "- **Stacking to compare.** Stacked bars hide individual series lengths above the "
            "first; use grouped bars to compare.\n"
            "- **Spaghetti charts.** Too many overlapping lines — switch to small multiples.\n"
            "- **Inconsistent axes across panels.** Small multiples must share a y-scale to be "
            "comparable (seaborn does this by default)."
        ),
        "ai_prompt": "Make a stacked bar chart of revenue by region and channel from a sales DataFrame",
        "exercises": [
            "Re-make the channel line chart as `units_sold` instead of revenue. Does the channel "
            "ranking change?",
            "Build a grouped bar of revenue by `product_category` and `channel`.",
            "Add the `campaign_indicator` as a colour to the monthly line and see if campaign "
            "weeks stand out.",
        ],
    },
    # ---------------------------------------------------------------- Week 4
    {
        "num": 4,
        "slug": "distributions_and_comparisons",
        "title": "Week 4 — Distributions and Comparisons",
        "question": "How do performance and satisfaction differ across departments?",
        "short_question": "how performance and satisfaction differ across departments",
        "datasets": ["operations", "customers"],
        "objectives": [
            "Read a histogram: centre, spread, skew, outliers.",
            "Compare groups with box plots and violin plots.",
            "Recognise right-skew and tame it with a log scale.",
            "Choose the right distributional chart for an audience.",
        ],
        "concept": (
            "## Beyond the average\n\n"
            "A single mean hides the story. **Histograms** show one distribution's shape; "
            "**box plots** compare many groups compactly (median, quartiles, outliers); "
            "**violin plots** add the full density, revealing bimodality a box hides. Skewed "
            "variables like income often need a **log scale** to be readable."
        ),
        "load_code": 'ops = load("operations")\ncustomers = load("customers")\nops.head()',
        "steps": [
            {
                "title": "A histogram for one distribution",
                "md": "Look at the shape of monthly performance — where is it centred and is it "
                      "symmetric?",
                "code": (
                    "fig, ax = plt.subplots()\n"
                    'ax.hist(ops["monthly_performance"], bins=30, color="#4C72B0")\n'
                    'ax.set_title("Distribution of monthly performance")\n'
                    'ax.set_xlabel("Performance score")\n'
                    'ax.set_ylabel("Employees")\n'
                    "plt.show()"
                ),
            },
            {
                "title": "Box and violin plots for group comparison",
                "md": "Compare departments. The box plot is compact; the violin shows the full "
                      "density. Note the outliers the box plot flags.",
                "code": (
                    "import seaborn as sns\n\n"
                    "fig, axes = plt.subplots(1, 2, figsize=(13, 5))\n"
                    'sns.boxplot(data=ops, x="department", y="monthly_performance", ax=axes[0])\n'
                    'axes[0].set_title("Performance by department (box)")\n'
                    'sns.violinplot(data=ops.dropna(subset=["satisfaction_score"]),\n'
                    '               x="department", y="satisfaction_score", ax=axes[1])\n'
                    'axes[1].set_title("Satisfaction by department (violin)")\n'
                    "for a in axes:\n"
                    "    a.tick_params(axis=\"x\", rotation=20)\n"
                    'save_figure(fig, "week04_dept_distributions")\n'
                    "plt.show()"
                ),
            },
            {
                "title": "Taming skew with a log scale",
                "md": "Customer income is strongly right-skewed. A log scale spreads the bulk out "
                      "so the distribution becomes readable.",
                "code": (
                    'inc = customers["income"].dropna()\n\n'
                    "fig, axes = plt.subplots(1, 2, figsize=(12, 4))\n"
                    'axes[0].hist(inc, bins=40, color="#DD8452")\n'
                    'axes[0].set_title("Income (raw, right-skewed)")\n'
                    "axes[1].hist(np.log10(inc), bins=40, color=\"#DD8452\")\n"
                    'axes[1].set_title("Income (log10 scale)")\n'
                    'axes[1].set_xlabel("log10(income)")\n'
                    "plt.show()"
                ),
            },
        ],
        "pause": (
            "## Pause and predict\n\n"
            "Which department do you expect to have the highest *median* performance, and which "
            "the widest spread? Predict before reading the box plot. Where would a single bar "
            "chart of means have misled you?"
        ),
        "mistakes": (
            "## Common mistakes\n\n"
            "- **Bar chart of means for distributions.** It hides spread and outliers entirely.\n"
            "- **Too few or too many histogram bins.** Both distort shape; try a few bin counts.\n"
            "- **Ignoring skew.** Reporting a mean income on a right-skewed variable overstates "
            "the typical customer; prefer the median or a log scale."
        ),
        "ai_prompt": "Compare training_hours across departments with a box plot from an ops DataFrame",
        "exercises": [
            "Plot the distribution of `tenure`. Is it skewed? Add a log scale if it helps.",
            "Make a violin plot of `training_hours` by department.",
            "Overlay the histogram of `customer_lifetime_value` for each segment (use transparency).",
        ],
    },
    # ---------------------------------------------------------------- Week 5
    {
        "num": 5,
        "slug": "visual_design_and_storytelling",
        "title": "Week 5 — Visual Design and Storytelling",
        "question": "How do we turn a correct chart into a persuasive one?",
        "short_question": "which region leads and by how much",
        "datasets": ["sales"],
        "objectives": [
            "Apply decluttering: remove non-data ink.",
            "Use colour to direct attention to one message.",
            "Annotate a chart so it states its own conclusion.",
            "Redesign a default chart into a story chart.",
        ],
        "concept": (
            "## From correct to compelling\n\n"
            "A chart can be accurate yet say nothing. Storytelling design means: a title that "
            "states the *takeaway* (not just the variable), colour that **highlights one thing** "
            "and greys the rest, direct labels instead of legends, and the removal of gridlines "
            "and borders that compete with the data."
        ),
        "load_code": 'sales = load("sales")\nby_region = sales.groupby("region")["revenue"].sum().sort_values()\nby_region',
        "steps": [
            {
                "title": "The default chart",
                "md": "Here is the chart most people would produce: technically fine, but it makes "
                      "the reader do the work.",
                "code": (
                    "fig, ax = plt.subplots()\n"
                    'by_region.plot(kind="bar", ax=ax, color="#4C72B0")\n'
                    'ax.set_title("Revenue by region")\n'
                    "ax.tick_params(axis=\"x\", rotation=0)\n"
                    "plt.show()"
                ),
            },
            {
                "title": "The redesigned story chart",
                "md": "Sort, switch to horizontal bars, grey everything except the leader, label "
                      "the values directly, and write the conclusion in the title.",
                "code": (
                    "leader = by_region.idxmax()\n"
                    'colors = ["#C44E52" if r == leader else "#B0B0B0" for r in by_region.index]\n\n'
                    "fig, ax = plt.subplots()\n"
                    "bars = ax.barh(by_region.index, by_region.values, color=colors)\n"
                    "for bar, value in zip(bars, by_region.values, strict=True):\n"
                    '    ax.text(value, bar.get_y() + bar.get_height() / 2, f"  €{value:,.0f}",\n'
                    '            va="center", fontsize=9)\n'
                    'ax.set_title(f"{leader} is our top-earning region")\n'
                    'ax.set_xlabel("Total revenue (€)")\n'
                    "ax.margins(x=0.18)\n"
                    'save_figure(fig, "week05_story_chart")\n'
                    "plt.show()"
                ),
            },
        ],
        "pause": (
            "## Pause and predict\n\n"
            "Cover the titles. Which version lets a busy executive get the message in two seconds? "
            "What exactly did the redesign change — and did any of it distort the data?"
        ),
        "mistakes": (
            "## Common mistakes\n\n"
            "- **Rainbow colour.** Giving every bar its own colour signals 'all equally "
            "important' — the opposite of a story.\n"
            "- **Title that names the axis.** 'Revenue by region' wastes the most-read text; state "
            "the finding instead.\n"
            "- **Decoration over clarity.** 3-D bars, shadows, and heavy gridlines add ink, not "
            "information."
        ),
        "ai_prompt": "Restyle a matplotlib bar chart to highlight a single category and grey the rest",
        "exercises": [
            "Redesign the weekly revenue line from Week 1 to highlight the holiday peak with an "
            "annotation.",
            "Take the channel bar chart and apply the grey-plus-highlight treatment to the Online "
            "channel.",
            "Write three alternative takeaway titles for the region chart, each emphasising a "
            "different message.",
        ],
    },
    # ---------------------------------------------------------------- Week 6
    {
        "num": 6,
        "slug": "geospatial_visualisation",
        "title": "Week 6 — Geospatial Visualisation",
        "question": "Which regions punch above their weight in sales per capita?",
        "short_question": "which regions lead on sales per capita",
        "datasets": ["regions", "stores"],
        "objectives": [
            "Load vector geometries with geopandas.",
            "Build a choropleth and read its classification.",
            "Understand CRS and why we reproject before measuring area.",
            "Overlay point data (stores) on a region map.",
        ],
        "concept": (
            "## Maps are charts too\n\n"
            "A **choropleth** shades regions by a value — powerful, but sensitive to how you "
            "classify the colour bins and to area distortion. Geometries carry a **coordinate "
            "reference system (CRS)**: latitude/longitude (EPSG:4326) is fine for plotting but "
            "wrong for measuring distance or area, so we reproject to a projected CRS first."
        ),
        "load_code": 'regions = load("regions")\nstores = load("stores")\nregions[["region_name", "population", "sales_per_capita"]]',
        "steps": [
            {
                "title": "A choropleth of sales per capita",
                "md": "Shade each region by `sales_per_capita` and label the regions at their "
                      "centroids.",
                "code": (
                    "fig, ax = plt.subplots(figsize=(7, 6))\n"
                    'regions.plot(column="sales_per_capita", cmap="YlGnBu", legend=True,\n'
                    '             edgecolor="white", ax=ax)\n'
                    "for _, r in regions.iterrows():\n"
                    "    ax.annotate(r[\"region_name\"], xy=(r.geometry.centroid.x, r.geometry.centroid.y),\n"
                    '                ha="center", fontsize=9)\n'
                    'ax.set_title("Sales per capita by region")\n'
                    "ax.set_axis_off()\n"
                    "plt.show()"
                ),
            },
            {
                "title": "Reproject before measuring",
                "md": "Areas computed in degrees are meaningless. Reproject to EPSG:3035 (a "
                      "metre-based European CRS) and compute area in km².",
                "code": (
                    "projected = regions.to_crs(epsg=3035)\n"
                    'projected["area_km2"] = (projected.geometry.area / 1e6).round(1)\n'
                    'print(projected[["region_name", "area_km2"]].to_string(index=False))'
                ),
            },
            {
                "title": "Overlay store points",
                "md": "Draw the regions in a neutral grey, then plot stores as points sized by "
                      "monthly revenue.",
                "code": (
                    "fig, ax = plt.subplots(figsize=(7, 6))\n"
                    'regions.plot(color="#EAEAEA", edgecolor="white", ax=ax)\n'
                    'stores.plot(ax=ax, color="#C44E52", alpha=0.7,\n'
                    '            markersize=stores["monthly_revenue"] / 2500)\n'
                    'ax.set_title("Stores sized by monthly revenue")\n'
                    "ax.set_axis_off()\n"
                    'save_figure(fig, "week06_store_map")\n'
                    "plt.show()"
                ),
            },
        ],
        "pause": (
            "## Pause and predict\n\n"
            "Before plotting: do you expect the most *populous* region to also have the highest "
            "*sales per capita*? They measure different things — watch whether the map confirms "
            "or breaks your intuition."
        ),
        "mistakes": (
            "## Common mistakes\n\n"
            "- **Mapping totals, not rates.** A choropleth of total sales mostly maps population; "
            "use a per-capita rate.\n"
            "- **Measuring area in degrees.** Always reproject to a projected CRS first.\n"
            "- **Too many colour classes.** More than ~6 bins are hard to distinguish; pick a "
            "classification scheme deliberately."
        ),
        "ai_prompt": "Make a choropleth of average_income from a geopandas GeoDataFrame called regions",
        "exercises": [
            "Make a choropleth of `average_income` instead of sales per capita. Does the pattern "
            "match?",
            "Count the number of stores per region (spatial or attribute join) and add it as a "
            "label.",
            "Colour the store points by their `region_id` instead of sizing them by revenue.",
        ],
    },
    # ---------------------------------------------------------------- Week 7
    {
        "num": 7,
        "slug": "interactive_visualisation_and_dashboards",
        "title": "Week 7 — Interactive Visualisation and Dashboards",
        "question": "How do we let stakeholders explore the numbers themselves?",
        "short_question": "how revenue moves over time and across regions",
        "datasets": ["dashboard"],
        "objectives": [
            "Build interactive charts with plotly express.",
            "Add hover, zoom, and legend filtering for exploration.",
            "Understand when interactivity helps and when it distracts.",
            "See how a notebook chart becomes a Streamlit dashboard.",
        ],
        "concept": (
            "## From static to interactive\n\n"
            "Static charts make one point; **interactive** charts let a stakeholder ask their own "
            "follow-up questions — hover for exact values, zoom into a period, toggle series. "
            "`plotly` builds these with little code. When several charts and filters belong "
            "together, a **dashboard** (we use Streamlit) is the natural home — see "
            "`dashboards/app.py`."
        ),
        "load_code": 'dash = load("dashboard")\ndash.head()',
        "steps": [
            {
                "title": "An interactive line with plotly",
                "md": "Total monthly revenue, with hover tooltips and zoom for free.",
                "code": (
                    "import plotly.express as px\n\n"
                    'monthly = dash.groupby("month", as_index=False)["revenue"].sum()\n'
                    'fig = px.line(monthly, x="month", y="revenue",\n'
                    '              title="Monthly revenue (hover and zoom)")\n'
                    "fig"
                ),
            },
            {
                "title": "An interactive bar with a colour dimension",
                "md": "Revenue by region; click legend entries to filter, hover for values.",
                "code": (
                    'region_rev = dash.groupby("region", as_index=False)["revenue"].sum()\n'
                    'fig = px.bar(region_rev, x="region", y="revenue", color="region",\n'
                    '             title="Revenue by region")\n'
                    "fig"
                ),
            },
            {
                "title": "A static export for the report",
                "md": "Dashboards live in the browser, but reports need a static image — so we "
                      "also save a matplotlib version to `figures/`.",
                "code": (
                    'monthly_region = dash.pivot_table(index="month", columns="region",\n'
                    '                                  values="revenue", aggfunc="sum")\n\n'
                    "fig, ax = plt.subplots()\n"
                    "monthly_region.plot(ax=ax)\n"
                    'ax.set_title("Monthly revenue by region")\n'
                    'ax.set_ylabel("Revenue (€)")\n'
                    'save_figure(fig, "week07_monthly_by_region")\n'
                    "plt.show()"
                ),
            },
        ],
        "pause": (
            "## Pause and predict\n\n"
            "Interactivity is not free — it needs a browser and can hide the headline. For this "
            "month's board summary, would you send the interactive plotly chart or the saved "
            "static image? Why?"
        ),
        "mistakes": (
            "## Common mistakes\n\n"
            "- **Interactivity for its own sake.** If the message is one number, a static chart is "
            "clearer and more portable.\n"
            "- **No default view.** An interactive chart should already tell the story before the "
            "user touches it.\n"
            "- **Shipping a notebook as a dashboard.** Use a real app (Streamlit) so non-coders "
            "can use it — see the next note."
        ),
        "ai_prompt": "Build a plotly express line chart of revenue over month grouped by channel",
        "exercises": [
            "Make a plotly line of revenue by `month` and `channel` (use `color='channel'`).",
            "Add `units_sold` as the bar height and `revenue` as hover data to the region bar.",
            "Open `dashboards/app.py`, run it with `uv run streamlit run dashboards/app.py`, and "
            "add one new filter.",
        ],
    },
    # ---------------------------------------------------------------- Week 8
    {
        "num": 8,
        "slug": "project_workshop_and_peer_review",
        "title": "Week 8 — Project Workshop and Peer Review",
        "question": "Can you carry one question from data to a polished, honest chart?",
        "short_question": "which customer segment is most valuable",
        "datasets": ["customers"],
        "objectives": [
            "Run the full workflow end to end on a fresh question.",
            "Produce one decision-ready chart with a takeaway title.",
            "Apply the verification checklist to your own work.",
            "Give and receive structured peer feedback.",
        ],
        "concept": (
            "## Putting it together\n\n"
            "This session is a workshop: pick a question, prepare the data, build *one* polished "
            "chart that answers it, and defend it against the verification checklist. Then review "
            "a peer's chart using the rubric below. The skill is no longer drawing charts — it is "
            "judging whether a chart earns the claim in its title."
        ),
        "load_code": (
            'customers = load("customers")\n'
            'segment_summary = (customers.groupby("segment", as_index=False)\n'
            '                   .agg(customers=("customer_id", "count"),\n'
            '                        avg_clv=("customer_lifetime_value", "mean"),\n'
            '                        avg_churn=("churn_probability", "mean")))\n'
            "segment_summary"
        ),
        "steps": [
            {
                "title": "One decision-ready chart",
                "md": "Average lifetime value by segment, ordered Value → Premium, with the "
                      "Premium bar highlighted and values labelled.",
                "code": (
                    'order = ["Value", "Mainstream", "Premium"]\n'
                    'summary = segment_summary.set_index("segment").loc[order]\n'
                    'colors = ["#B0B0B0", "#B0B0B0", "#55A868"]\n\n'
                    "fig, ax = plt.subplots()\n"
                    'bars = ax.bar(summary.index, summary["avg_clv"], color=colors)\n'
                    'for bar, value in zip(bars, summary["avg_clv"], strict=True):\n'
                    "    ax.text(bar.get_x() + bar.get_width() / 2, value, f\"€{value:,.0f}\",\n"
                    '            ha="center", va="bottom", fontsize=10)\n'
                    'ax.set_title("Premium customers are worth the most over their lifetime")\n'
                    'ax.set_ylabel("Average lifetime value (€)")\n'
                    "ax.margins(y=0.15)\n"
                    'save_figure(fig, "week08_clv_by_segment")\n'
                    "plt.show()"
                ),
            },
        ],
        "pause": (
            "## Pause and predict\n\n"
            "Your title claims Premium customers are worth the most. Is that claim safe? Premium "
            "is also the smallest segment — does *average* CLV alone justify a strategy decision, "
            "or do you need the segment sizes and churn next to it?"
        ),
        "mistakes": (
            "## Common mistakes\n\n"
            "- **Title over-claims.** Make sure the data supports the sentence in the title.\n"
            "- **One metric, big decision.** Average CLV ignores segment size and churn; show what "
            "the decision actually needs.\n"
            "- **Skipping your own verification.** Run the checklist on your *own* chart, not just "
            "on AI output.\n\n"
            "## Peer-review rubric\n\n"
            "Score a peer's chart 1–5 on each: (a) right chart for the question, (b) honest axes "
            "and scale, (c) title states a supported takeaway, (d) clutter removed, (e) a reader "
            "could act on it. Give one concrete improvement."
        ),
        "ai_prompt": "Critique this chart: does the title's claim follow from average CLV by segment alone?",
        "exercises": [
            "Add segment size as a second panel (or a secondary annotation) so the CLV chart is not "
            "read in isolation.",
            "Pick a different question from any dataset and produce one decision-ready chart for it.",
            "Swap charts with a peer and complete the peer-review rubric on theirs.",
        ],
    },
]


def main() -> int:
    counts = {"live": 0, "completed": 0, "exercises": 0}
    for week in WEEKS:
        base = f"week{week['num']:02d}_{week['slug']}"
        targets = {
            NB / "live" / f"{base}.ipynb": build_live(week),
            NB / "completed" / f"{base}_completed.ipynb": build_completed(week),
            NB / "exercises" / f"week{week['num']:02d}_exercises.ipynb": build_exercises(week),
        }
        for path, nb in targets.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            nbf.write(nb, path)
            counts[path.parent.name] += 1

    total = sum(counts.values())
    print(f"Wrote {total} notebooks: " + ", ".join(f"{k}={v}" for k, v in counts.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
