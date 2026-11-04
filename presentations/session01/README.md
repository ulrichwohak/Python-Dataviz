# Course introduction

Use **[course-introduction.pdf](course-introduction.pdf)** for projection.
It is compiled from [LaTeX](course-introduction.tex), with selectable text, native mathematics
and vector charts. The [presenter PDF](course-introduction-presenter.pdf) contains slide
thumbnails, teaching notes and source credits.

There are 23 main slides and one setup/access backup. The matrix-algebra backup has been
removed. Keep motivation concise to leave time for line, bar and scatter plots in the first class.
The teaching notebook also supplies a short histogram, box, violin and strip-plot tour.

## Content

- Course administration, outcomes and the confirmed six-session timetable:
  three Python sessions (basics; comparisons/uncertainty; mapping) and three Power BI sessions
  (foundations; comparisons/filtering; dashboard building).
- Three equally weighted individual figures with notes only (25% combined), and the
  unchanged 75% final Python data story. Data, questions and deadlines remain TBD.
- Materials and tools. The introductory slides do not discuss AI.
- A clickable [Todd Jones dataset catalogue](https://github.com/toddrjones/datasets)
  link on the materials slide invites students to explore real data sources.
- Properly typeset scalar and matrix OLS objectives, followed by 100 synthetic observations
  with visible scatter and the same points with their estimated line. No residual segments,
  square diagrams or area totals.
- Synthetic pooled/within-country slope reversal and Cairo's Figure 3 discussion.
- Audience, context and figure notes. The first ungraded redesign stays in the exercise
  notebook for the final 20 minutes, without a separate slide.
- Clickable [r/dataisugly](https://www.reddit.com/r/dataisugly/) and
  [r/dataisbeautiful](https://www.reddit.com/r/dataisbeautiful/) links for a short ungraded critique.
- Four instructor-supplied critique images on slides 19–22: prices/wages, a firearm-murder
  time series, a pool/skyscraper comparison and a county suicide-rate map. Students see
  short questions; the presenter notes contain the critique and verification limits.
- Backup: Python setup and Power BI access before Session 4.

Judge Reddit charts independently of their community label. Preview the feeds before class;
the supplied images work offline. Choose examples within the existing introduction time,
keeping the final 20-minute exercise. Assessment dates and the Power BI access route remain TBD.

Pause on “Today: a chart tour in Python” for live coding and the runnable chart tour.
Then open [the Session 1 exercise notebook](../../notebooks/01-python-chart-tour/exercises.ipynb)
directly, without returning to the slides.
Its supplied pie-chart cell is the starting point; students change the plotting code while
retaining the data. The later optional activities are outside this 20-minute exercise.

## Rebuilding and keeping it current

The primary sources are `course-introduction.tex` and `course-introduction-notes.json`.
`scripts/build_introduction_pdf.py` generates the fixed-seed OLS illustration and reads
the mathematical hotel illustration from a local course CSV,
compiles twice with XeLaTeX, checks for overflow/missing glyphs, renders slides, and creates
the presenter PDF. It requires the instructor's LaTeX installation (Beamer, PGFPlots,
fontspec, unicode-math), Arial/Menlo fonts, Poppler and the bundled document Python
runtime with pypdf, Pillow and reportlab. Students need only the PDF, not authoring tools.

Run the build script with that Python runtime and a **fresh temporary build directory**.
Use `--xelatex /path/to/xelatex` if needed. Generated data, the local Cairo extracts and the
four original screenshots in `local-critique-images/` must
already exist; the builder does not download anything. Review all slide and presenter pages,
then copy the two verified PDFs here. Update the syllabus and schedule alongside changes.

Finally run:

```bash
uv run python scripts/check_intro_sync.py --record-reviewed
uv run python scripts/check_intro_sync.py
```

The snapshot detects changed sources/outputs, not agreement of meaning. Record it only after
reviewing the content and exports.

## Earlier versions and rights

The pre-LaTeX PowerPoint is retained under
`presentations/archive/2026-11-04-pre-latex/` as a historical copy. The old
`course-introduction.mjs` and `scripts/build_introduction.mjs` are also historical sources;
they do not build the current PDF. Do not use or update them as the active introduction.

The Cairo Figure 3 extracts and the supplied screenshots remain local teaching assets.
Screenshots retain their full content and aspect ratios; no source data have been verified
from the images alone. Both PDFs and the
historical PowerPoint stay Git-ignored and are not authorised for public redistribution.
Keep source credits and ignore rules intact. See `NOTICE.md`.
