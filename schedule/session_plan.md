# Session Plan — ECBS5209 Data Visualization and Storytelling

MSc Business Analytics, CEU.

- **Teaching period:** 4 November–9 December 2026
- **Meeting pattern:** Wednesdays, 17:40–19:20 (six 100-minute sessions)
- **Sequence confirmed by the instructor on 4 November:** three Python/design sessions,
  followed by three Power BI sessions.
- **Schedule source:** [CEU TimeEdit](https://cloud.timeedit.net/at_ceu/web/schedulers/ri1o5k2187oZ54Q98QQ5Z66ltg10m4068n02733dkk74X3Yj605y2Y24Z17Q7Y9502225AE3B9gDQ8Z7C9Al3QB1uZ5275Et0Q7BF1C2B791D.phtml)

## Sessions

| # | Date | Focus |
| --- | --- | --- |
| 1 | 4 Nov 2026 | Python chart tour: line, bar and scatter plots; introduction to histograms, box, violin and strip plots; labels, notes and export. |
| 2 | 11 Nov 2026 | Comparisons and uncertainty: histograms, box plots and confidence-interval plots, including a supplied event-study example. |
| 3 | 18 Nov 2026 | Mapping in Python: geographical joins, choropleths, proportional symbols, projections and meaningful denominators. |
| 4 | 25 Nov 2026 | Power BI foundations: interface, importing data, field types, aggregation and basic charts. |
| 5 | 2 Dec 2026 | Power BI comparisons and filtering: tables, matrices, cards/KPIs, filters and slicers. |
| 6 | 9 Dec 2026 | Power BI dashboard building: layout, interactions, storytelling and checking filtered results. |

## Materials and preparation status

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

The Python examples and optional numerical checks have been executed. The Power BI guides
are written, but the Desktop walkthrough and student access route must be tested before
Session 4. The published real-data event-study estimates are downloaded and documented in the
[data README](../data/README.md). Optional references are listed in the
[notebook index](../notebooks/README.md).

## Data used in each session

1. SSA daily birth counts via FiveThirtyEight: weekday differences and the 2014 monthly-totals redesign.
2. Amazon boot/sandal prices and seasonality; Callaway–Sant’Anna published real-data estimates and 95% simultaneous bands.
3. OWID / Global Carbon Budget 2023 emissions with Natural Earth countries: totals versus per-person comparisons.
4–6. Amazon monthly sample spending by shipping state and category. Use the same table in all three Power BI workshops.

Download fixed source versions before class with `uv run python scripts/fetch_data.py` (about 330 MB on first run).
The [data README](../data/README.md) records source versions, selections and limitations.

## Session 1 introduction

Use the [LaTeX-compiled introduction](../presentations/session01/course-introduction.pdf).
It covers administration, assessment and a short motivation for visualisation. Begin with
“The purpose of visualization is insight, not pictures.” Attribution is retained in the
presenter notes and NOTICE.

The OLS example follows the scalar and matrix objectives with a scatterplot, then the same
observations with a fitted line. Keep data and scales unchanged. There are no residual
segments, square diagrams, error totals or matrix-algebra backup. The introduction does not
discuss AI; the syllabus and assignment guidance remain unchanged.

The synthetic hotel example reveals Simpson's paradox without changing observations or
scales. Cairo's Figure 3 prompts discussion of the audience and purpose of a dense graphic.
The Reddit links and four supplied images provide a short ungraded critique exercise.
The images cover prices/wages, an inverted firearm-murder time series, pool/skyscraper
comparisons and a county suicide-rate map. Choose among them within the introduction time.
Choose discussion depth to
leave time for basic Python charts, notes, export and the first redesign.

### Suggested pacing for the 100-minute class

- 15 minutes: administration and selected motivation examples; do not cover every opening example in depth.
- 35 minutes: line and bar plots, data aggregation and basic plotting syntax.
- 20 minutes: run the chart tour, including a scatterplot and four views of distributions.
  Compare box, violin and strip plots on the same 2014 daily-birth sample and scales.
- 10 minutes: recap labels, figure notes and export. Defer detailed rolling-average and
  annotation examples to the optional reference if time is tight.
- 20 minutes: the student redesign below, including a brief comparison of answers.

The tour introduces chart reading and available forms. Session 2 still develops distributional
comparison, binning/smoothing choices, and uncertainty in more depth.

Reserve the **final 20 minutes (approximately 19:00–19:20)** for the
[Session 1 exercise notebook](../notebooks/01-python-chart-tour/exercises.ipynb), after live
coding. It supplies data preparation and a pie of the 12 monthly birth totals in 2014.
Students copy and edit the chart cell, add labels and a figure note, and check the first and
last values. A line chart is the intended simple redesign; accept a justified alternative.
Use the last few minutes for a comparison of answers. The notebook's later optional tasks
are not part of this activity. The teaching notebook uses monthly daily means; the exercise explicitly keeps monthly totals and discusses month length.

## Audience, notes and fair presentation

These topics recur within the concrete chart tasks, rather than occupying a separate meeting.

- Session 1: reader's question; labels, units, data provenance and a concise figure note.
- Session 2: uncertainty versus variation; estimated quantity, units, reference period and
  interval meaning in the supplied event-study results. Students plot supplied estimates,
  rather than estimate an econometric model.
- Session 3: geography, join coverage, denominator, projection, missing areas and source note.
- Sessions 4–6: apply the same reasoning to Power BI aggregation, filtering and interaction.
  Keep titles and notes accurate under filtering and make the current selection visible.

The detailed reading remarks remain in [the instructor notes](../docs/live_coding_notes.md).
Earlier placements there are historical; this timetable supersedes them.

## Ungraded practice and project reviews

Keep short redesign/critique exercises within each 100-minute meeting. Each lecture now
has an exercise notebook: monthly births, distributions and uncertainty, mapping, then
three Power BI activities. Do not add graded quizzes.

Keep brief project reviews in Sessions 2–4: audience/question, chart/evidence, then
narrative/notes/verification. They use existing practice time. The
[project-workshop reference](../notebooks/reference/project-workshop.ipynb)
remains optional independent support.

## Assessment and access

- [Three individual figures](../assignments/chart-critique-redesign/): 25% combined, equally
  weighted. For each, answer an instructor-supplied question using supplied data; submit the
  figure and accompanying notes only. These are three assignments across the course, not
  one per lecture. Their datasets and questions are TBD.
- [Final Python data story](../assignments/final-data-story/): 75%, unchanged requirements.
- Power BI exercises remain ungraded. Confirm access for non-Windows users before Session 4.
- Submission dates and routes remain TBD; do not infer deadlines from teaching dates.
