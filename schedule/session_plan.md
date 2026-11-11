# Session Plan — ECBS5209 Data Visualization and Storytelling

MSc Business Analytics, CEU.

- **Teaching period:** 4 November–9 December 2026
- **Meeting pattern:** Wednesdays, 17:40–19:20 (six 100-minute sessions)
- **Sequence:** three Python/design sessions, followed by three Power BI sessions.
- **Schedule source:** [CEU TimeEdit](https://cloud.timeedit.net/at_ceu/web/schedulers/ri1o5k2187oZ54Q98QQ5Z66ltg10m4068n02733dkk74X3Yj605y2Y24Z17Q7Y9502225AE3B9gDQ8Z7C9Al3QB1uZ5275Et0Q7BF1C2B791D.phtml)

## Sessions

| # | Date | Focus |
| --- | --- | --- |
| 1 | 4 Nov 2026 | Python chart tour: line, bar and scatter plots; introduction to histograms, box, violin and strip plots; labels, notes and export. |
| 2 | 11 Nov 2026 | Comparisons and uncertainty: cumulative distributions, weather and calendar patterns in scatterplots, and OLS coefficient intervals. |
| 3 | 18 Nov 2026 | Mapping in Python: geographical joins, choropleths, proportional symbols, projections and meaningful denominators. |
| 4 | 25 Nov 2026 | Power BI foundations: interface, importing data, field types, aggregation and basic charts. |
| 5 | 2 Dec 2026 | Power BI comparisons and filtering: tables, matrices, cards/KPIs, filters and slicers. |
| 6 | 9 Dec 2026 | Power BI dashboard building: layout, interactions, storytelling and checking filtered results. |

## Lecture materials

Each folder now matches its meeting number and schedule title. Open the teaching notebook
for fully written examples or Power BI steps; open the exercise notebook for ungraded practice.

| Lecture | Teaching notebook | Exercise notebook |
| --- | --- | --- |
| 1 | [Python chart tour](../notebooks/01-python-chart-tour/lecture.ipynb) | [Monthly births](../notebooks/01-python-chart-tour/exercises.ipynb) |
| 2 | [Comparisons and uncertainty](../notebooks/02-comparisons-and-uncertainty/lecture.ipynb) | [Distributions and intervals](../notebooks/02-comparisons-and-uncertainty/exercises.ipynb) |
| 3 | [Mapping in Python](../notebooks/03-mapping-in-python/lecture.ipynb) | [Coverage and denominators](../notebooks/03-mapping-in-python/exercises.ipynb) |
| 4 | [Power BI foundations](../notebooks/04-power-bi-foundations/lecture.ipynb) | [Time and regional comparisons](../notebooks/04-power-bi-foundations/exercises.ipynb) |
| 5 | [Power BI comparisons and filtering](../notebooks/05-power-bi-comparisons-and-filtering/lecture.ipynb) | [Tables, cards and filters](../notebooks/05-power-bi-comparisons-and-filtering/exercises.ipynb) |
| 6 | [Power BI dashboard building](../notebooks/06-power-bi-dashboard-building/lecture.ipynb) | [Dashboard review](../notebooks/06-power-bi-dashboard-building/exercises.ipynb) |

Optional references are listed in the [notebook index](../notebooks/README.md).
Power BI access arrangements will be announced before Session 4.

## Data used in each session

1. SSA daily birth counts via FiveThirtyEight: weekday differences and the 2014 monthly-totals redesign.
2. Amazon boot/sandal budget shares, NOAA weather and calendar-month comparisons, then seasonal boot-price OLS coefficients with pointwise intervals.
3. OWID / Global Carbon Budget 2023 emissions with Natural Earth countries: totals versus per-person comparisons.
4–6. Amazon monthly sample spending by shipping state and category. Use the same table in all three Power BI workshops.

Download fixed source versions before class with `uv run python scripts/fetch_data.py` (about 330 MB on first run).
The [data README](../data/README.md) records source versions, selections and limitations.

## First class

Open the [course introduction (PDF)](../presentations/session01/course-introduction.pdf).
After live coding, use the [Session 1 exercise notebook](../notebooks/01-python-chart-tour/exercises.ipynb)
for an ungraded chart redesign. The notebook supplies the data and instructions.

## Session 2 opening: collected figures and week 1 redesigns

On 11 November, begin with **18 third-party visualisations** submitted for discussion, then
the **four student redesigns** of the 2014 monthly-births chart. All collected figures and
the birth-chart review appear in the classroom presentation. The
[lecture notebook](../notebooks/02-comparisons-and-uncertainty/lecture.ipynb) opens directly
with the three live-coding questions about footwear purchases. Student submissions and comments remain anonymous. This opening
replaces the single-figure vote for this meeting; the weekly routine is otherwise unchanged.

Use the [slides and interactive birth chart](../presentations/session02/README.md) for the
opening discussion. In the notebook, investigate budget shares, calendar patterns and
uncertainty about boot-price differences. The session ends with the seasonal-chart redesign
and a comparison of your figures.

## Audience, notes and fair presentation

These topics recur within the concrete chart tasks, rather than occupying a separate meeting.

- Session 1: reader's question; labels, units, data provenance and a concise figure note.
- Session 2: uncertainty versus variation; estimated quantity, units, reference period and
  threshold shares, calendar information and interval meaning in the footwear OLS results. Students plot prepared estimates for question 3,
  rather than estimate an econometric model.
- Session 3: geography, join coverage, denominator, projection, missing areas and source note.
- Sessions 4–6: apply the same reasoning to Power BI aggregation, filtering and interaction.
  Keep titles and notes accurate under filtering and make the current selection visible.

## Ungraded practice and project reviews

Each lecture has an exercise notebook. These activities provide practice and feedback,
not additional graded quizzes. Session 2 closes with the seasonal-chart redesign and comparison of figures. Short project reviews
in Sessions 3–4 cover the question,
evidence, figures and narrative. The [project-workshop reference](../notebooks/reference/project-workshop.ipynb)
is optional support.

## Assessment and access

- [Three individual figures](../assignments/chart-critique-redesign/): 25% combined, equally
  weighted. For each, answer an instructor-supplied question using supplied data; submit the
  figure and accompanying notes only. These are three assignments across the course, not
  one per lecture. Their datasets and questions are TBD.
- [Final Python data story](../assignments/final-data-story/): 75%, unchanged requirements.
- Power BI exercises remain ungraded. Access instructions for non-Windows users are TBD.
- Submission dates and routes will be announced separately.
