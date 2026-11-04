# CLAUDE.md

This file provides guidance to coding agents working in this repository.

## What this repository is

This is the production course repository for **ECBS5209 — Data Visualization and
Storytelling**, an MSc Business Analytics elective at CEU.

The 2026 course has **six 100-minute sessions**, meeting Wednesdays from 17:40 to 19:20 on
4, 11, 18, and 25 November and 2 and 9 December. Its intellectual centre is visual design,
storytelling, critique, and reproducible implementation in Python. Keep all course-facing
material aligned with this structure and schedule.

The local untracked file `course repo.md` documents inherited repository conventions. Read it
before substantive structural changes, but treat the current README,
[`docs/course_outline.md`](docs/course_outline.md), and
[`schedule/session_plan.md`](schedule/session_plan.md) as authoritative where its example
schedule conflicts with the six-session course.

## Recording and carrying forward teaching decisions

[`docs/live_coding_notes.md`](docs/live_coding_notes.md) records the instructor's reading
remarks, teaching rationale, examples, and outstanding proposals. Read the relevant section
before developing material. Keep detailed plans there and durable guidance here; do not create
a competing harness file. Check `NOTICE.md` for source attribution and reuse restrictions.

The instructor wants reading remarks incorporated into course preparation, not lost in chat.
Record each agreed idea in its appropriate session and distinguish a proposal from implemented
material. When implementation is requested, update the affected plan, teaching materials, and
provenance together. Check the actual code or artifact before claiming an example exists.
Fit additions into the six sessions; do not silently introduce extra assessments or deployments.

## Course architecture

Each scheduled lecture has one folder under `notebooks/`, containing a fully written
`lecture.ipynb` and `exercises.ipynb`. There are no separate live/completed variants.
Use the exact schedule titles in headings and paths. Edit `scripts/real_data_content.py` and
`scripts/lecture_content.py`, then regenerate
with `scripts/build_notebooks.py`. Do not hand-edit notebook JSON.

The confirmed timetable is now three Python/design sessions and three Power BI sessions:
1. basic line, bar and scatter charts, a short histogram/box/violin/strip tour, labels, notes and export;
2. histograms, box plots and confidence intervals, including supplied event-study results;
3. dedicated mapping: joins, choropleths, proportional symbols, projections and denominators;
4. Power BI foundations and basic charts;
5. Power BI tables, matrices, cards/KPIs, filters and slicers;
6. Power BI dashboard/report layout, interactions, storytelling and verification.

Use `schedule/session_plan.md` and `notebooks/README.md` as the current timetable and
material index. All six teaching/exercise pairs are implemented. Power BI notebooks are
Desktop workshop guides with optional Python checks, not Python implementations of the
Power BI lessons. Native Desktop walkthrough verification and student access remain pending.
Design/annotation, Python interactivity and project-workshop references are optional.
Short project reviews remain in Sessions 2–4. Keep advanced DAX,
complex models and platform administration out of scope. Distinguish Desktop report pages
from Service dashboards. Assessed deliverables remain Python-centred.

The primary course introduction is `presentations/session01/course-introduction.pdf`, compiled
from `course-introduction.tex` with XeLaTeX using `scripts/build_introduction_pdf.py`.
Use real LaTeX mathematics. Preserve the scalar and matrix OLS objectives and visual example;
the matrix-algebra backup slide has been removed at the instructor's request.
The old PowerPoint and JS sources are historical, not the current deliverable.
Whenever schedule, assessment, tools or policies change, update the LaTeX source, presenter
notes, PDF exports and syllabus together. Run `uv run python scripts/check_intro_sync.py`.

Use in-class redesign activities: supply working code that produces a deliberately unsuitable
chart for a stated audience and question. Students diagnose the mismatch, keep the underlying
data and calculation consistent, redesign, and explain their choices. Accept defensible
alternatives; the instructor reference is one possible solution, not the only valid chart.

The two assessment components live in `assignments/`: three equally weighted individual
figures worth 25% combined and a 75% final Python data story. Mark each figure out of 100;
their average contributes 25% of the course grade. For each figure assignment, the instructor
supplies data and a question; students design a figure from scratch in Python and submit only
the figure with notes. There are three assignments across the course, not one per lecture.
Their datasets, questions and deadlines remain TBD. Do not require code,
a redesign or a separate rationale. The figure-assignment folder retains the earlier name
`chart-critique-redesign` for stable links; old starter/reflection files are ungraded practice.
The final project's requirements and weight remain unchanged. Exercises are formative,
not additional graded quizzes. The confirmed three-Python/three-Power-BI timetable is recorded
in `docs/live_coding_notes.md` and now governs the schedule, syllabus and introduction.

## Environment and commands

Use `uv` only. Never add `pip`, `%pip`, `!pip`, `pipenv`, `Pipfile`, or `conda` instructions to
student-facing files; a warning not to use those tools is the sole allowed exception. Target
Python 3.12 and preserve `.python-version`, `pyproject.toml`, and `uv.lock`.

Student/instructor entry point:

```bash
uv sync
uv run python scripts/fetch_data.py
uv run jupyter lab
```

Acceptance sequence:

```bash
uv lock --check
uv sync --locked
uv run python scripts/fetch_data.py
uv run python scripts/check_no_pip.py
uv run python scripts/check_notebooks.py
uv run ruff check .
```

For documentation-only changes, at minimum run `uv run python scripts/check_no_pip.py`.

The shared `.vscode/settings.json` preserves the repository-root notebook working directory
and disables automatic completion and inline suggestions for live coding, including Python
and notebook overrides. Keep manual completion, documentation and AI chat available; this
is an editor preference, not a change to the course AI policy. Only this settings file is
tracked under `.vscode/`; other local editor files remain ignored.

## Data and notebook policy

- Current scheduled teaching data are public real datasets downloaded in pinned versions by
  `scripts/fetch_data.py`. Sources: SSA births, donated Amazon purchases, OWID CO₂/Natural Earth,
  and published real-data event-study results. Preserve selection rules and limitations.
  Only OLS/Simpson mathematical illustrations remain explicitly synthetic.
- Notebooks must not download data. They read local files from `data/raw/` and
  `data/processed/`.
- Use direct library calls in teaching notebooks: `pd.read_csv(...)` (with explicit date
  parsing where needed), `gpd.read_file(...)` for geographic data, and `fig.savefig(...)`.
  Do not use the course-specific `load` or `save_figure` wrappers. Keep file paths visible
  and relative to the repository root; data preparation creates the `figures/` directory.
- If future data sources change, update the preparation script and `data/README.md` together,
  document provenance and licensing, and keep downloaded data ignored unless the repository
  explicitly requires otherwise.
- Notebooks must remain valid JSON, use the `Python 3 (ipykernel)` kernelspec, execute from the
  repository root, and contain no package-install cells.
- The first Markdown cell of every notebook must briefly describe the data's source,
  subject, what each row represents and its main contents. Keep the language concrete;
  explicitly identify synthetic data. Descriptions are generated from `scripts/real_data_content.py`.
- Clear stale or large outputs before committing. Verify generated notebooks with the
  repository checks and, when changing substantive content, headless execution.
- Assume students know basic Python syntax. Do not explain import aliases, equality,
  loops, f-strings or built-ins such as `len` in lecture comments. Use concise comments
  for library-specific operations such as `parse_dates`, grouping, plotting controls,
  exports and analytical choices. Avoid narrating obvious lines or repeating explanations.
  Preserve useful comments in the notebook generators without changing the analysis or
  filling in student exercise answers.
- Teach transformations step by step: use meaningful intermediate variables instead of
  dense method chains or calculations hidden inside plotting calls. Separate preparation,
  inspection and plotting into short cells when this helps live coding. Show small previews
  at important transitions; do not split every familiar expression into trivial microsteps.
  Apply this to lectures, supplied exercise code and optional references without supplying
  exercise solutions. Introduce unfamiliar pandas concepts before relying on them:
  Lecture 1 explains date columns, a DatetimeIndex, date selection and monthly resampling.

## Teaching and content conventions

- Treat graphics as **communication**: help a particular audience understand evidence
  faithfully, rather than merely produce attractive pictures. Compare what the author intended
  with what a reader actually understood, and revise both clarity and evidential accuracy.
- Begin examples with an audience, question, and intended use—not a chart type or library call.
- Distinguish **purpose from message**. A figure can explain a finding, support scrutiny,
  reveal a pattern, motivate a hypothesis, or invite curiosity. Exploratory figures need not
  start with a predetermined conclusion. Give a presentation figure one primary job, not
  necessarily one variable; retain context that materially changes its interpretation.
- Adapt to the audience's knowledge, task, medium, and accessibility needs. Contrast an
  academic-paper figure with a management presentation using the same evidence. Change
  emphasis and explanation, not the underlying facts or necessary uncertainty; avoid
  stereotypes that academics need dense charts or business audiences cannot handle nuance.
- Use descriptive plots to motivate research questions. Separate the observed pattern, a
  possible explanation, and evidence needed to test it. Be transparent about whether a
  hypothesis preceded inspection of the data or arose from it. Identify raw observations,
  summaries, and fitted lines; do not call all three "raw data" or treat an exploratory pattern
  as independent confirmation of the hypothesis it inspired.
- Treat **figure notes as part of the visualisation**, not an afterthought. Distinguish the
  title, annotation, figure note, source credit, and alternative text. Include what the reader
  needs to interpret the figure: units, sample, period, aggregation or denominator, material
  exclusions, uncertainty, and provenance as relevant. Keep notes concise, legible, accurate
  against the code, and attached to exported figures.
- Present statistical results fairly: state the quantity estimated, units, comparison or
  reference category, and uncertainty where relevant. Explain what intervals represent;
  distinguish uncertainty about an estimate from variation among observations. Do not invent
  intervals, imply causation from association, or equate an interval including zero with proof
  of no effect. Preserve material limitations when simplifying a chart.
- Make design and storytelling cumulative across all six sessions. Each session should include
  critique, an explicit design decision, implementation, interpretation, and verification.
- Treat Cairo's *The Functional Art* as the primary conceptual influence and Munzner's
  *Visualization Analysis and Design* as a supporting analytical framework. Link to legitimate
  publisher records and preserve attribution in `NOTICE.md`; do not commit or redistribute
  local textbook PDFs.
- Preserve the course's **use AI, then verify** policy and AI-attribution sections.
- Do not invent institutional dates, policies, submission deadlines, datasets, learning
  outcomes, or citations. Use `TBD` where authoritative information is absent.

## Agreed examples and development status

This is the local state checked on **4 November 2026**, not a claim that materials have been
published remotely. Recheck artifacts and update this record as work progresses. The detailed
sequences and safeguards are in `docs/live_coding_notes.md`.

| Topic | Placement and current state |
| --- | --- |
| Course administration | Primary introduction contains the roadmap, 25%/75% assessment, classroom routine, materials and contact information. No AI slide or discussion; other AI guidance is unchanged, as explicitly confirmed by the instructor. |
| OLS: equations made visible | Primary introduction includes scalar and matrix objectives, 100 synthetic observations with visible scatter, and the same observations with an estimated OLS line. Fixed seed and identical scales across the reveal. No residual segments, squares, area totals or matrix-algebra backup. |
| Cairo's Figure 3 | Primary local introduction contains the figure, enlarged detail, and critique prompts. |
| Supplied chart critiques | Slides 19–22 show four original screenshots with student questions and instructor-only explanations: prices/wages, firearm murders, pool/skyscrapers and county suicide rates. Preserve full images, source labels and verification limits. Screenshots stay local-only. Use selected examples within the existing introduction time. |
| Pooled versus within-country relationships | Primary introduction contains a two-slide reveal using generated synthetic hotel data. |
| In-class redesign practice | Session 1 uses the final 20 minutes for `notebooks/01-python-chart-tour/exercises.ipynb`; it preserves the pie-to-time-chart task using real 2014 monthly birth totals. Every later lecture has a matching exercise notebook. Ungraded practice; three equally weighted figure assignments make up 25%, each requiring an original figure with notes only. |
| First-session chart tour | The Session 1 teaching notebook includes runnable scatter, histogram, box, violin and strip examples after line/bar exploration. Reuse the same 365 dates from the real 2014 SSA births file. Explain smoothing, width normalisation and jitter; keep the final 20-minute exercise. Longer annotation examples are optional. |
| Same evidence, different audiences | Cross-course principle recorded; academic/management comparisons woven into chart tasks and project reviews. |
| Figure and visualisation notes | Introduce in Session 1, develop through Sessions 2–3 and project reviews, apply to the Session 6 dashboard; notes are required in the chart and mapping exercises. |
| Event-study estimates and uncertainty | Session 2 plots published Callaway–Sant’Anna real-data estimates and 95% simultaneous bands. Year -1 is estimated, not a zero normalisation. Source output is documented in data/README.md. |
| Live-updating figure | Optional extension proposed outside the three Power BI workshops; no live-stream app or public deployment implemented. |

### Session 1 opening and examples

- Open with **“The purpose of visualization is insight, not pictures.”** Credit Ben
  Shneiderman, **quoted in Cairo**, printed p. xx; preserve the fuller attribution in
  `NOTICE.md`. Use Cairo's **“We understand *because* we see.”**, printed p. xv, after the OLS
  reveal, retaining the emphasis on *because*. Verify quotations and distinguish printed page
  numbers from PDF page numbers. Do not turn unverified reading fragments into attributed quotes.
- Use `presentations/session01/course-introduction.pdf` for the course introduction. Typeset
  the scalar objective and its matrix counterpart in LaTeX. Do not restore the deleted
  matrix-algebra backup or add a derivation. Show a plain scatterplot and then the same points
  with the fitted line, keeping the scales fixed. Do not restore residual segments, square
  diagrams or total-area labels. If explaining residuals verbally, they compare observed and
  predicted `y` at the same `x`, not perpendicular distances to the line.
- The same primary local introduction contains the Cairo discussion; earlier example decks
  are archived under `presentations/archive/2026-11-03/`.
  Figure 3 is Cairo's **Época magazine** graphic (printed p. xix), not an academic-paper figure.
  Its horizontal axis shows GDP levels, not growth; its chronological path is not a regression
  line. Compare a focused academic claim with historical exploration: ask what each layer adds
  or obscures, rather than declaring density inherently bad. Presidency colours are not causal
  evidence. Preserve attribution and the deck's local-only status.
- The hotel example illustrates Simpson's paradox with fictional countries A, B, and C. Reveal
  groups without changing points or scales: the positive pooled slope coexists with negative
  within-country slopes. Separate country intercepts and a common slope work for this
  constructed example, not necessarily for arbitrary data. Neither fit establishes causality.
  Keep data generation in `scripts/fetch_data.py` and document construction in `data/README.md`.
- Editable slide sources live beside the decks. When revising them, preserve data-backed chart sources,
  verify numerical claims against the generated data, and render the resulting slides for review.

### Planned extensions

- **Event study:** the supplied results are implemented in Lecture 2. Preserve the
  published simultaneous confidence bands, estimated pre-treatment contrasts,
  real-data provenance and log-employment units. Do not turn the plotting lesson into an
  econometrics assessment.
- **Live updates:** the current `dashboards/app.py` filters a prepared, cached CSV; it is not
  a live data feed. The proposed separate demonstration generates synthetic readings at regular
  intervals, maintains a bounded history, and offers pause/resume and reset. Show observation
  timestamps and stale data clearly. Distinguish new observations from a chart refresh, and
  a simulation from a real feed or replay. Discuss scale stability and avoid silent clipping.
  Run locally first; an active browser-session simulation is not an always-on shared collector.
  Hosting remains a possible later step, not an authorised deployment or required assignment.
  Retain this as optional material outside the confirmed Power BI workshops.

## Reading coverage and reuse

- The local *Functional Art* PDF is a **72-page excerpt, not the complete book**. It contains
  front matter/introduction, Chapter 1, the John Grimwade profile, and the index, with omitted
  material between them. Check actual coverage before assigning readings or claiming to have
  consulted a chapter; the presence of a chapter in the contents or index is not evidence that
  its text is available. Do not assume other local textbook PDFs are complete without checking.
- Arnheim's *Visual Thinking* was requested as additional background. No authorised full-text
  download has been obtained for this repository. Use legitimate publisher or library access;
  do not claim a local copy exists or cite unread passages.
- Local textbook PDFs, extracts, and the extended deck containing Figure 3 are not public course
  assets. Preserve their ignore rules, source credits, and reuse restrictions; do not infer
  redistribution permission from a file being downloadable or available locally.

## Development workflow

Use the GitHub issue → branch → pull request → merge flow for requested repository changes; do
not commit directly to `main`. Keep changes reviewable and do not commit, push, open a pull
request, or modify remote state unless the instructor asks.

Interact with GitHub via the `gh` CLI. The personal access token, if present, lives in
`.secrets.md` and must never be displayed or committed.

## Local-only files

The ignore rules protect `.secrets.md`, `course repo.md`, local textbook PDFs, the local syllabus
build helper, virtual environments, generated data, generated figures, and scratch output. Do
not weaken those protections without explicit instructor direction.
