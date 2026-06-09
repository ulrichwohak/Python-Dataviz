# Data Visualisation with Python

Course material and reproducible environment for **Data Visualisation with Python**, an
elective in the **MSc Business Analytics** programme at **CEU (Central European University)**.

> **Status: phantom / prototype repository.** This repository validates the technical
> structure, notebook design, `uv` setup, plotting workflow, dashboard workflow, and
> live-coding format *before* final datasets and final course content are chosen.
> **Every dataset here is synthetic**, generated deterministically by repository scripts.
> No real or confidential data is used.

- **Programme:** MSc Business Analytics, CEU
- **Format:** 8 weekly sessions, taught through live coding
- **Term dates:** `TERM_DATES_TBD` (see [`schedule/session_plan.md`](schedule/session_plan.md))

## Course overview

The course teaches students to turn business data into clear, honest, and persuasive
visualisations in Python. It moves from the grammar of a single chart to multi-panel
comparisons, geospatial maps, interactive figures, and a shareable dashboard. Students are
beginner-to-intermediate Python programmers; the emphasis is on judgement — choosing the
right chart, reading it correctly, and avoiding common distortions — as much as on syntax.

## How sessions are organised

Each weekly session is one Jupyter notebook, developed live in class. For every week the
repository provides three notebooks:

| Folder | Purpose |
| --- | --- |
| [`notebooks/live/`](notebooks/live/) | Skeleton the instructor fills in during the live session. |
| [`notebooks/completed/`](notebooks/completed/) | Fully developed reference notebook (post-class). |
| [`notebooks/exercises/`](notebooks/exercises/) | Practice tasks students attempt on their own. |

The eight weeks are: (1) intro to visualisation, (2) data for visualisation, (3) core
business charts, (4) distributions and comparisons, (5) visual design and storytelling,
(6) geospatial visualisation, (7) interactive visualisation and dashboards, and
(8) project workshop and peer review. See [`docs/course_outline.md`](docs/course_outline.md).

## Repository materials

- [`src/dataviz_course/`](src/dataviz_course/) — installable helpers: synthetic-data generation, reusable plotting, and small utilities.
- [`scripts/`](scripts/) — generate the datasets, (re)build the notebooks, and run repository checks.
- [`data/`](data/) — generated datasets land here (git-ignored; regenerate with the script). See [`data/README.md`](data/README.md).
- [`dashboards/`](dashboards/) — a Streamlit dashboard built on the prepared dataset.
- [`docs/`](docs/) — course outline, AI policy, and live-coding notes.
- [`project_template/`](project_template/) — starting point for the final student project.

## Getting started

Install [`uv`](https://docs.astral.sh/uv/), then:

```bash
uv sync                                          # create the environment from uv.lock
uv run python scripts/fetch_data.py             # prepare the synthetic datasets
uv run jupyter lab                               # open the notebooks
```

> Do **not** use `pip`, `%pip`, `!pip`, `pipenv`, or `conda` for the course environment.
> The environment is managed with `uv` only.

## Learning outcomes

By the end of the course, students should be able to:

- Choose an appropriate chart type for a given business question and audience.
- Build and refine plots with matplotlib, seaborn, and plotly.
- Prepare and reshape data into a tidy form suited to visualisation.
- Read distributions, comparisons, and relationships critically, and spot misleading charts.
- Produce a simple geospatial map and an interactive dashboard.
- Communicate a data story with clear annotation and visual design.

## Pedagogical position on AI / LLMs

AI coding assistants are permitted and actively discussed: most notebooks include an
"AI co-pilot" activity and a verification checklist for critically reviewing AI-generated
charts and code. The course position is **use AI, then verify** — students are responsible
for understanding and checking anything an assistant produces. See
[`docs/ai_policy.md`](docs/ai_policy.md) for the full policy.

## Attribution and licensing

Licensed under the MIT License — see [`LICENSE`](LICENSE). All data is synthetic; any
external materials adapted in future are credited in [`NOTICE.md`](NOTICE.md).

**AI attribution (repository creation):** the initial structure and prototype content of
this repository were drafted with the assistance of an AI coding tool and then reviewed by
the instructor. This statement concerns how the repository was built, not student coursework.
