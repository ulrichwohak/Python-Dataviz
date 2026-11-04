# Data Visualization and Storytelling

Course materials and a reproducible Python environment for **ECBS5209 — Data Visualization
and Storytelling**, an elective in the **MSc Business Analytics** programme at **CEU
(Central European University)**.

- **Teaching period:** 4 November–9 December 2026
- **Meeting time:** Wednesdays, 17:40–19:20
- **Format:** three Python/design sessions and three Power BI workshops, with critique and practice
- **Primary tools:** pandas, matplotlib, seaborn, and Power BI; optional Plotly/Streamlit

The current syllabus is available as a
[`Word document`](Data-Visualization-and-Storytelling-Syllabus.docx) and as
[`Markdown`](Data-Visualization-and-Storytelling-Syllabus.md).

## Course overview

The course teaches students to turn data into clear, honest, and purposeful visual stories.
The starting point is not a chart menu or a software interface: it is an audience, a question,
and the decision the visualisation should support. Students learn how perception, visual
encoding, comparison, hierarchy, annotation, and narrative affect what a reader notices and
understands. They then implement and refine those decisions in Python.

Audience adaptation runs throughout the course: students consider the reader's knowledge,
purpose, and viewing context when choosing detail, terminology, emphasis, and visual style.
An academic-paper figure and a management slide can present the same evidence differently,
while preserving the information needed for a fair interpretation.

The first three sessions cover basic Python charts, comparisons and uncertainty, then mapping.
The final three sessions cover Power BI foundations, comparisons/filtering, and dashboard
building. Design, audience, notes and verification recur throughout. Assessed work remains in
Python. See [`workshops/power-bi/`](workshops/power-bi/) for the Power BI plan and resources;
Plotly and Streamlit remain optional companions.

## How sessions are organised

Each dated lecture has one folder containing `lecture.ipynb` and `exercises.ipynb`.
The teaching notebooks contain fully written examples; there are no separate skeleton or
completed versions. For Power BI, the teaching notebook is a step-by-step Desktop workshop
guide, with optional Python checks.

Use the [notebook index](notebooks/README.md) to open either notebook for each lecture.
Design/annotation, Python interactivity and project-workshop references live separately in
[`notebooks/reference/`](notebooks/reference/); they are not extra scheduled lectures.

The six-session progression is:

1. Python chart tour: line, bar and scatter plots, plus histograms, box, violin and strip
   plots; labels, figure notes and export;
2. comparisons and uncertainty: histograms, box plots and confidence-interval plots;
3. mapping in Python: joins, choropleths, proportional symbols and projections;
4. Power BI foundations: importing data, field types, aggregation and basic charts;
5. Power BI comparisons and filtering: tables, matrices, cards/KPIs, filters and slicers; and
6. Power BI dashboard building: layout, interactions, storytelling and verification.

Short project reviews are integrated into Sessions 2–4 instead of a standalone project class.

See the [`course outline`](docs/course_outline.md) for content and the
[`dated session plan`](schedule/session_plan.md) for meeting dates and materials.

Start with the [**course introduction**](presentations/session01/course-introduction.pdf)
compiled from [LaTeX](presentations/session01/course-introduction.tex). It covers administration,
assessment, classroom redesign exercises, and the motivation for visualisation. The OLS,
Simpson's-paradox, and Cairo examples support that introduction. The local instructor deck
includes a copyrighted textbook figure and is not published to GitHub.

In-class [redesign activities](docs/redesign-activities.md) start from a deliberately weak
chart and a clear reader's question. Students change the visual form, verify the underlying
numbers, and explain why the revision serves that reader better.

For the final 20 minutes of the first class, open the
[monthly-births exercise](notebooks/01-python-chart-tour/exercises.ipynb). Run the supplied
pie chart, then edit the plotting code to answer the researcher's question. The data preparation
is provided. Later tasks in that notebook are optional.

## Assessment

- **Individual figure — 25%.** Design a figure from scratch in Python using instructor-supplied
  data and a question. Submit only the figure with its accompanying notes, not code or a rationale.
- **Final Python data story — 75%.** A coherent, reproducible story built around a small set of
  related visualisations and a concise stakeholder-facing explanation.

Full briefs live in [`assignments/`](assignments/). The Power BI workshops do not add a graded
item or replace either Python deliverable.

## Repository materials

- [`src/dataviz_course/`](src/dataviz_course/) — data generation, plotting helpers, and small
  utilities.
- [`scripts/`](scripts/) — prepare data, build notebooks, and run repository checks.
- [`data/`](data/) — local extracts of public real datasets. See [`data/README.md`](data/README.md).
- [`dashboards/`](dashboards/) — a small Streamlit example built on the prepared dataset.
- [`docs/`](docs/) — course outline, AI policy, and live-coding guidance.
- [`assignments/`](assignments/) — assessment briefs and starter materials.
- [`project_template/`](project_template/) — reproducible structure for the final data story.

## Getting started

Install [`uv`](https://docs.astral.sh/uv/), then run these commands from the repository root:

```bash
uv sync
uv run python scripts/fetch_data.py
uv run jupyter lab
```

> Do **not** use `pip`, `%pip`, `!pip`, `pipenv`, or `conda` for the course environment.
> The environment is managed with `uv` only.

Notebooks read local files created by `scripts/fetch_data.py`; they do not download data at
runtime. They use direct `pd.read_csv(...)` and `fig.savefig(...)` calls with paths relative
to the repository root. Set the notebook kernel's working folder to `Python-Dataviz`;
the data-preparation command also creates the `figures/` output folder.

The first data download is about **330 MB**, mostly the Amazon purchase-history source.
It needs an internet connection but no API key. Later runs reuse checksum-verified cached
files. Run it before class. A failed download stops with an error; there is no synthetic fallback.

## Data and questions

- **Session 1:** US daily births (SSA via FiveThirtyEight). Why do weekdays and weekends look
  different? Redesign a pie chart of 2014 monthly birth totals.
- **Session 2:** donated Amazon purchase histories. How do boot and sandal prices and seasons
  differ? Plot the authors' published real-data minimum-wage event-study estimates with their
  95% simultaneous confidence bands.
- **Session 3:** Our World in Data / Global Carbon Budget emissions and Natural Earth boundaries.
  How do total-emissions and per-person comparisons differ?
- **Sessions 4–6:** the same Amazon extract, aggregated by month, shipping state and category,
  for Power BI charts, filters and the final report page.

The Amazon sample is voluntary and restricted to seven categories, not representative company
sales. The event-study authors describe their application as illustrative. Source versions,
licences, exclusions and units are documented in the [data README](data/README.md).
Only the introductory OLS and Simpson's-paradox **mathematical illustrations** remain synthetic.
Explore additional sources in [Todd Jones's dataset catalogue](https://github.com/toddrjones/datasets).

In VS Code, open `Python-Dataviz` as the workspace folder and set **Jupyter: Notebook File
Root** to `${workspaceFolder}` in Workspace Settings. Restart an already-running notebook
kernel after changing the setting. Editor settings are local and ignored by Git, so each
student needs to set this once. In JupyterLab, check the working folder with `%pwd`; if it is
a lecture folder such as `notebooks/01-python-chart-tour`, run `%cd ../..` once before
running the notebook cells.

## Learning outcomes

By the end of the course, students should be able to:

- frame a visualisation around a specific audience, question, and communication purpose;
- select and justify effective visual encodings for comparisons, change, distributions,
  relationships, and uncertainty;
- identify misleading scales, encodings, and omissions and redesign weak charts;
- create accessible visual hierarchy with colour, typography, annotation, and layout;
- prepare data and implement publication-ready static visualisations in Python;
- build basic Power BI charts and a focused interactive report with verified filters;
- develop, critique, verify, and revise a reproducible data story; and
- explain the limitations and ethical implications of a visualisation.

## Course references

The course draws its main design and storytelling perspective from Alberto Cairo's
[*The Functional Art: An Introduction to Information Graphics and Visualization*](https://www.pearson.com/en-us/subject-catalog/p/functional-art-the-an-introduction-to-information-graphics-and-visualization/P200000008946/9780321834737)
(New Riders, 2013). Tamara Munzner's
[*Visualization Analysis and Design*](https://www.routledge.com/Visualization-Analysis-and-Design/Munzner/p/book/9781466508910)
(A K Peters/CRC Press, 2015) provides supporting concepts such as what–why–how, marks and
channels, interaction, and validation. Readings are selective; the notebooks are the required
technical materials. See [`NOTICE.md`](NOTICE.md) for attribution details.

## Pedagogical position on AI / LLMs

AI coding assistants are permitted and discussed. The course position is **use AI, then
verify**: students remain responsible for understanding, checking, and defending every chart,
interpretation, and line of code they submit. See [`docs/ai_policy.md`](docs/ai_policy.md).

## Attribution and licensing

Repository code and original course materials are licensed under the [MIT License](LICENSE).
Third-party books and their contents are not included under that licence. External sources are
credited in [`NOTICE.md`](NOTICE.md).

**AI attribution (repository creation):** the initial repository structure and portions of the
course material were drafted with an AI coding tool and then reviewed and revised by the
instructor. This statement concerns repository creation, not student coursework.
