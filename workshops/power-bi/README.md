# Power BI in three sessions

Use the final three classes for a compact Power BI sequence:

| Session | Date | Teaching notebook | Exercise notebook |
| --- | --- | --- | --- |
| 4 | 25 November 2026 | [Power BI foundations](../../notebooks/04-power-bi-foundations/lecture.ipynb) | [Chart choices](../../notebooks/04-power-bi-foundations/exercises.ipynb) |
| 5 | 2 December 2026 | [Power BI comparisons and filtering](../../notebooks/05-power-bi-comparisons-and-filtering/lecture.ipynb) | [Tables, cards and filters](../../notebooks/05-power-bi-comparisons-and-filtering/exercises.ipynb) |
| 6 | 9 December 2026 | [Power BI dashboard building](../../notebooks/06-power-bi-dashboard-building/lecture.ipynb) | [Dashboard review](../../notebooks/06-power-bi-dashboard-building/exercises.ipynb) |

These are Markdown workshop guides: perform the steps in Desktop, using optional Python
cells only to check values. Each class saves and reuses `course_purchases.pbix`. The guides
are written and numerical checks have run; the native Desktop walkthrough still needs
testing on the confirmed student setup. The older guide URLs below redirect to these notebooks.

All classes run 17:40–19:20. Exercises are **ungraded practice**. The 25% individual
figure and 75% final data story remain Python deliverables. Only the figure and notes are
submitted for the 25% item; the final project's requirements remain unchanged.

## What we retain from the earlier course

These workshop guides are newly prepared course material, not recovered files from a previous
instructor. The actual teaching files for
[2025–26](https://ceulearning.ceu.edu/course/view.php?id=19132) and
[2024–25](https://ceulearning.ceu.edu/course/view.php?id=17664) are behind Moodle access controls
and have not been inspected. The instructor confirmed the three-session sequence on
4 November 2026; the [instructor notes](../../docs/live_coding_notes.md) record the decision.

The [2024–25 syllabus](https://ceu.studyguide.timeedit.net/modules/ECBS5209?year=2024)
used six sessions for interface basics, chart types, tables/KPIs, filters/slicers,
interactivity and a dashboard demonstration. We now allocate three classes to these topics.
Design, audience, notes and verification begin in the three Python sessions and recur here.

Use one prepared table and a small set of built-in visuals. Advanced DAX, multi-table
modelling, extensive Power Query transformations, gateways, refresh pipelines and workspace
administration are outside this short introduction. No cloud publication is required.

## Setup and access

[Power BI Desktop requires Windows](https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-get-the-desktop).
For macOS/Linux users, a Windows computer or an institutional virtual-lab route must be
confirmed and tested **before Session 4**. CEU access instructions and software version are
TBD. Students should not purchase a platform for this course.

From the course repository root, prepare the data and optional Python checking outputs:

```bash
uv run python scripts/fetch_data.py
uv run python workshops/power-bi/python_reference.py
```

Import `data/processed/amazon_monthly.csv` and name the table `dashboard`. These are real
donated purchase histories from Berke et al., Open e-commerce 1.0, restricted to seven
categories and 2018–2022. One row is a month × shipping state × category combination.
Sum `spending_usd`, `quantity` or `purchase_records` according to the question. A count of
aggregate rows is not an order or customer count. Missing states remain Unknown. This
voluntary sample is not representative of all shoppers or company revenue. See the
[data README](../../data/README.md) for provenance and exclusions.

The reference script writes two charts, `verification_totals.csv` and
`verification_filters.csv` to the ignored `output/` folder. These are checking aids, not
additional data tables to import into the report.

## Shared audience and question

A consumer researcher wants to know how monthly sample spending changed and which shipping
states contributed most. Start with all data, then investigate categories and date ranges.
Keep the default view understandable without clicking.

Session 5 demonstrates a KPI against an explicitly hypothetical USD 100,000 monthly target
for this selected sample. It lives on a separate page and is not valid for filtered
categories or states. No observed business targets are supplied.

The final page uses monthly spending, state totals, summary cards for spending and
items purchased, and category/date slicers. A table on a checking page helps reconcile exact
values. All filters must apply consistently to the intended visuals.

In everyday usage this is a dashboard. In Microsoft's terminology, our Desktop artifact is
a **report page**; a Power BI Service dashboard uses pinned tiles and has different filtering
behaviour. See [Microsoft's distinction](https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboards).
The classroom task is the interactive report, with no dependency on Service publishing.

Save your `.pbix` file locally after each class. No Power BI file is submitted for credit.
