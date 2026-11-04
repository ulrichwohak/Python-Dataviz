# Live-Coding Notes (Instructor)

The current timetable is in [the session plan](../schedule/session_plan.md).
Each numbered folder now contains one fully written `lecture.ipynb` and an
`exercises.ipynb`; use [the notebook index](../notebooks/README.md).
Older placements recorded below are historical, not additional scheduled lectures.
The goal is to make visual and analytical decisions observable, not simply type plotting code.

## Confirmed revision on 4 November 2026

The instructor approved three Python/design sessions (basic charts; comparisons and
uncertainty; dedicated mapping), followed by three Power BI sessions (foundations;
comparisons/filtering; dashboard building). This supersedes earlier session placements below.
Figure notes begin in Session 1 and recur throughout; event-study results belong to Session 2,
mapping to Session 3, and Power BI begins in Session 4. Short project reviews remain in 2–4.

The introduction is now a LaTeX-compiled PDF with native mathematics. Keep the scalar and
matrix objectives in the motivation, but remove the separate matrix-algebra backup slide.
The introductory slides do not discuss AI; the instructor explicitly kept the existing AI
guidance elsewhere unchanged. Reserve the final 20 minutes of Session 1 for the monthly-births
exercise notebook, with its supplied pie chart and editable plotting cell.
The twelve scheduled notebooks are implemented, including published real-data event-study
results, dedicated mapping and three Power BI workshop guides. Design, Python interactivity
and project support remain optional references. Python examples have been executed; the
Power BI Desktop walkthrough and student access route still need testing.

## Before class

```bash
uv sync
uv run python scripts/fetch_data.py
uv run jupyter lab
```

Open the lecture's `lecture.ipynb`. Its examples are fully written so students can revisit
them after class. Decide which examples can be shortened if discussion runs long.
Check local data and the writable figures folder before teaching.

## Session 1 chart tour

The materials slide links to [Todd Jones's dataset catalogue](https://github.com/toddrjones/datasets).
Invite students to explore a topic and identify a question a figure could answer. It is a
catalogue of external sources, whose access and reuse terms differ, not a new assignment.
The real-data replacement was requested and implemented on 4 November 2026. Session 1 uses
SSA daily births; Session 2 uses Amazon purchases and published Callaway–Sant’Anna employment
estimates; Session 3 uses OWID emissions/Natural Earth; Power BI uses Amazon monthly aggregates.
`fetch_data.py` downloads fixed versions (about 330 MB once) and records filtering/counts.
Keep the voluntary-sample limitation and the event-study authors' illustrative-use warning.
The Census API now requires a key, so it is not a dependency; uncertainty uses the published
real-data event-study bands. No synthetic event-study fallback remains.

The instructor requested a broader first look at chart types, including violin plots.
The Session 1 teaching notebook includes the runnable tour after the
line/bar exploration. Run these supplied cells and discuss the result rather than spending
the whole class typing plot formatting.

Use a scatterplot for two numerical variables, a histogram for overall frequencies, a box
plot for group summaries, a violin for smoothed distribution shape, and a strip plot for
individual observations. The distribution examples use the same real 2014 dates,
weekday order and birth-count scales. Print group counts and missing-value exclusions first.

Explain the violin's width and smoothing, then show the strip plot to distinguish observed
points from the estimated shape. The fixed maximum violin width does not compare group
sizes. Jitter moves dots only sideways, not on the birth-count axis. These are distributions, not
confidence intervals. The second session returns to comparison and uncertainty in depth.

Budget 20 minutes for the tour within the 100-minute session. Use selected introductory
examples and treat the longer annotation/audience sections as optional references. Preserve
the final 20-minute redesign. See the suggested pacing in the session plan.

## Supplied critique examples in the introduction

On 4 November 2026 the instructor supplied four images for slides 19–22. Keep the images
unchanged and let students identify the issues before using the presenter-note explanations:

- Prices and wages: unequal comparison periods and triangle sizes that do not reflect the labels.
- Florida firearm murders: an inverted numerical axis, a broad title and a policy annotation
  that does not establish causality.
- Pool and skyscrapers: the meaning of “bigger”, length versus height, and uneven numeric
  intervals at similarly spaced ticks.
- County suicide rates: missing data versus low values, colour accessibility, omitted
  data period/source and uncertainty in small populations.

Treat these as alternatives within the existing introduction time, not extra required work.
Keep the final 20-minute redesign. Two images concern deaths; allow a student to discuss
one of the other examples instead. Do not authenticate social-media accounts or infer
underlying data accuracy from a screenshot. Sources and reuse limits are in NOTICE.md.

## Graphics as communication

**Instructor reading note recorded 3 November 2026:**

> essential to understanding the state of graphics as a form of communication.

This is the fragment supplied by the instructor, with whitespace normalised. Its source and
page have not been verified; retain it as a reading note rather than an attributed slide quote.

Use **graphics as communication** as the course's framing. A chart's scales, grouping, labels,
colour, and accompanying notes shape how its reader interprets the evidence. Ask what students
want the reader to understand, then ask a peer what they actually understand from the figure.
Use any mismatch to guide revision, while checking that the intended message is itself justified.
Understanding may mean recognising uncertainty or finding a worthwhile question, not agreeing
with the author. Introduce this alongside the opening quotation in Session 1 and reuse it in
critique and peer review. This refines the existing course philosophy rather than adding a topic.

## Why make this figure?

**Instructor request recorded 3 November 2026:** develop the question of why a visualisation
is made, including its relationship to the surrounding text and its ability to create curiosity.

Distinguish **purpose** (what the reader should be able to do) from **message** (the finding
the evidence supports). An exploratory figure can have a clear purpose before we know its
message. Revise any proposed message when the evidence changes; uncertainty or an absence of
a clear pattern can itself be the important finding.

Use these overlapping roles as discussion prompts, not an exhaustive classification:

- **Explain:** make a finding or idea understandable. The OLS opening connects an equation to a scatterplot and fitted line; it does not establish an empirical claim about a dataset.
- **Enable scrutiny:** let readers assess a statement in the text by inspecting the relevant
  comparison, variation, exceptions, and uncertainty. Ask what might weaken the statement.
- **Enable discovery:** help readers investigate a question or notice patterns without
  prescribing a conclusion. A comparison worth investigating need not already be a result.
- **Motivate an investigation:** show the observation, contrast, or puzzle that makes a
  hypothesis worth examining. Separate the visible pattern from its possible explanation.
- **Invite curiosity:** draw attention to a meaningful question or unexpected pattern, then
  provide the context needed to investigate it. Do not manufacture surprise through hidden
  baselines, omitted uncertainty, or misleading labels.

For each figure, complete: **“For [reader], this figure helps them [understand, compare,
check, or investigate something specific].”** Then identify the supported takeaway or open
question. Ask why a figure helps more than a sentence or table, and what would be lost if it
were removed. Give the figure a primary job; retain secondary details when they help readers
perform that job or judge the evidence fairly. One primary job need not mean only one variable.

In **Session 1**, apply these questions to Cairo's Figure 3: which details help readers assess
the GDP–inequality claim, and which help them investigate historical change? This sharpens
the existing discussion rather than adding another activity. In **Session 4**, ask how each
figure contributes to the written argument. Reuse the removal test in **Session 4** project review.
The project template includes the same prompts; no new graded deliverable is introduced.

Conceptual support: [Brehmer and Munzner (2013)](https://www.cs.ubc.ca/labs/imager/tr/2013/MultiLevelTaskTypology/)
distinguish why a visualisation task is performed from how it is performed. The prompts above
are our teaching adaptation, not a reproduction of their task typology.

## A descriptive figure can motivate a hypothesis

**Instructor request recorded 3 November 2026:** discuss introductory figures that show the
data behind a research question or make the intuition for a hypothesis visible before the
formal analysis. Treat this as a distinct contribution a figure can make to an academic paper.

A project can begin with a hypothesis from theory or earlier work, then use a descriptive
figure to illustrate the relevant phenomenon. Alternatively, a pattern noticed in the data
can suggest a new hypothesis. Describe which happened; the order of a paper's presentation
need not be the order of discovery.

Use three short prompts alongside an existing chart:

1. **What do we see?** Describe the measured pattern, including the sample and comparison.
2. **What might explain it?** State a hypothesis and a plausible alternative explanation.
3. **What would we need to check?** Identify evidence or a comparison that could distinguish
   the explanations. A motivating pattern alone does not establish the proposed mechanism.

Use “raw observations” only when the marks represent those observations. Means, bins,
smoothing, and fitted lines are summaries or model results; identify them and disclose
important filters or transformations. Prefer a simple descriptive view that makes the
question understandable, rather than requiring every observation on every introductory chart.
Retain variation and relevant groups when their omission would change the interpretation.

In **Session 1**, reuse the hotel example: its pooled association can motivate asking whether
distance and price are also related within countries. The grouped view shows why that question
requires a different comparison. These data were deliberately constructed to demonstrate a
reversal; do not present the exercise as an empirical discovery about hotels. In **Session 4**,
use the prompts when writing the opening of the data story. No new figure or assessment is
required, and the current slide deck and notebooks remain unchanged by this teaching note.

Be transparent when the data suggested the hypothesis. Re-describing or fitting a model to
that same pattern does not supply independent confirmation. This distinction between
generating and testing hypotheses follows [Nosek et al. (2018), *The preregistration revolution*](https://doi.org/10.1073/pnas.1708274114).
This is a brief interpretation safeguard, not a new unit on research design.

## Audience adaptation throughout the course

**Instructor request recorded 3 November 2026:** make customisation for the target audience
a recurring principle. In particular, compare visualisations for an academic paper with
those used by a business analyst presenting to managers. This should inform every session,
not become an isolated lesson about cosmetic styles.

Every current notebook already names an audience, question, and decision. Deepen that brief
with these questions before choosing a chart or polishing its appearance:

- Who will read it, and what subject knowledge, statistical knowledge, and chart familiarity
  can we reasonably expect? Check rather than infer from a job title.
- What must the reader understand, compare, investigate, or decide?
- Will they read a paper at their own pace, watch a projected presentation, or explore a
  dashboard? How much reading time and supporting explanation will they have?
- What terminology, labels, text size, colour choices, and alternative descriptions make
  the figure accessible in that context?
- Which definitions, comparisons, uncertainty, and limitations must accompany the figure
  so this reader can judge the claim fairly?

### Planned exercise: same evidence, two audiences

Integrate this into **Session 4's existing redesign activity**. Start from one checked course
result and give students two concrete briefs:

- **Academic-paper figure:** a reader familiar with the statistical method needs to evaluate
  the finding without the author present. Make the measured quantity, units, comparison,
  uncertainty, and method clear in the figure and caption. Choose terminology that fits this
  specified reader and check legibility at the final publication size.
- **Management-presentation slide:** a manager knows the business context and needs to judge
  whether the result warrants further investigation. Give the supported takeaway visual
  priority, explain technical terms, use readable projected text, and annotate the comparison
  relevant to that discussion. Keep material uncertainty and limitations visible. Supporting
  methodological detail can accompany the slide in notes or an appendix.

Hold the underlying result fixed so students can explain what they changed for the audience:
title, terminology, annotations, amount and placement of detail, layout, and delivery format.
If the brief requires a different measure or analysis, identify that as a change of question,
not merely a restyling. Both versions must convey the same evidential strength.

These are specified teaching scenarios, not rules that academics prefer dense charts or that
managers cannot read statistics. Ask students to justify choices from the brief. Technical
audiences also need clear design; decision-makers also need uncertainty. Do not make one
version seem more convincing by hiding results or qualifications.

Use the existing Figure 3 discussion to introduce this idea in Session 1. Revisit it when
explaining uncertainty in Session 2, writing and reviewing notes in Session 4, and applying
the same principles to Power BI charts and dashboards in Sessions 5–6. In peer review, ask readers to state the intended message
and identify what they still need to know. Then ask what they would change for another audience.

**Development status:** recorded across the course plan and reflected in the project-template
brief. The paired academic/management example is still to be built into the notebook materials.
No additional graded deliverable or assessment change is introduced.

## A useful rhythm for a 100-minute session

- **Frame (10 minutes):** audience, question, intended decision, and a weak or ambiguous chart
  to critique.
- **Build (30 minutes):** prepare the data and create the simplest defensible chart in small,
  testable steps.
- **Critique (15 minutes):** ask what the chart makes easy or difficult to see; check encodings,
  scales, omissions, and uncertainty.
- **Redesign (25 minutes):** improve hierarchy, colour, annotation, layout, or interaction one
  deliberate choice at a time.
- **Practise and verify (15 minutes):** students complete a focused exercise, including one
  claim supported by the visual evidence.
- **Close (5 minutes):** name the transferable design principle and connect it to the graded
  work.

Adjust this rhythm to the session, but preserve time for critique and interpretation. A finished
chart without a clear purpose and an interpretation checked against the evidence is not the
learning objective.

## Session 1: Reddit chart critique

**Implemented on 4 November 2026:** the introductory slide deck now includes clickable links
to [r/dataisugly](https://www.reddit.com/r/dataisugly/) and
[r/dataisbeautiful](https://www.reddit.com/r/dataisbeautiful/) after the discussion of purpose,
audience and context. In pairs, students choose a chart, explain what they learn, identify
what is clear or potentially misleading, and suggest one concrete improvement.

Keep this as an ungraded activity within the existing introduction discussion time. The
community name does not establish a chart's quality. Preview the changing feeds before class;
use the preceding Cairo figure with the same prompts if live browsing is unavailable.
No Reddit posts or images are reproduced in the deck.

## Session 1 opening: seeing least squares

Use the [course introduction](../presentations/session01/course-introduction.pdf) before coding.
It combines administration with three motivation examples, then introduces redesign practice.
The presenter notes contain prompts and attribution. The editable source is
`presentations/session01/course-introduction.tex`; students need only the PDF.

- Begin with “The purpose of visualization is insight, not pictures.” Credit Ben Shneiderman,
  quoted in Cairo, printed p. xx, in the presenter notes. Cover administration briefly.
- Show the scalar and matrix objectives. Ask what they ask us to minimise, without calculation.
- Show 100 synthetic observations with noticeable scatter around an upward trend.
- Add the fitted line on the next slide, leaving points and scales unchanged. There is one
  chart on each slide. Do not show residual segments, square diagrams or error totals.
- Explain verbally that OLS minimises squared vertical differences between observations and
  predictions at the same x. Do not call these perpendicular distances.
- Finish with Cairo's quote, preserving italics on *because*. Ask what the picture clarified.

This is an intuitive introduction, not a proof or derivation. The line is estimated from the
displayed points: its intercept is approximately 0.6632 and slope 0.5595. The fixed-seed
construction is documented in `NOTICE.md`. Blue points and a contrasting line follow the
instructor's visual reference. The matrix-algebra backup remains removed.

After the live coding, reserve the final 20 minutes for
[the Python chart-tour exercise](../notebooks/01-python-chart-tour/exercises.ipynb).
Students run the supplied pie chart, copy and modify the plotting cell, then check their
chart against the printed totals. Data preparation stays unchanged. The teaching notebook demonstrates weekly totals with a line chart. Allow a few minutes to compare answers; later optional notebook
tasks are outside this activity.

## Session 1 discussion: Cairo's Figure 3

**Instructor request recorded 3 November 2026:** use this information-rich graphic to open a
discussion about focus. The instructor's critique is that years, presidencies, and historical
commentary compete with a single GDP–inequality message. For a focused academic argument,
each figure should make its main finding easy to identify. Contrast that brief with Cairo's
interest in a combination of presentation and exploration, rather than announcing that the
graphic is intrinsically bad.

The source is **Figure 3, printed p. xix** (PDF page 20) of *The Functional Art*. It is Cairo's
graphic for **Época magazine**, not a research-paper figure. The surrounding discussion is on
pp. xvi–xx. GDP levels are on the horizontal axis and Gini inequality on the vertical axis;
years run from 1981 to 2010, with a connecting path and presidency colours. Do not describe
the horizontal axis as a GDP growth rate or the path as a fitted regression line.

Use the local instructor deck `presentations/session01/course-introduction.pdf`:
the course administration is followed by a compact OLS example, a Simpson's-paradox reveal,
and the Figure 3 discussion. It embeds the original
figure and an enlarged chart detail; both retain their source credit. This deck and the
extracted images under `textbook/extracts/` are ignored by Git. The earlier demonstration decks
are superseded and kept in `presentations/archive/2026-11-03/`. The earlier discussion source is
[`cairo-figure3.mjs`](../presentations/session01/cairo-figure3.mjs); it requires those local
images to build the extended version.

Discussion sequence:

1. Show the full figure before giving a verdict. Ask students to state its main message in
   one sentence and compare their answers.
2. Enlarge the chart. Identify what position, chronology, colour and text contribute. Which
   layers help answer the intended question, and which impose unnecessary reading effort?
3. Compare two briefs: communicate one academic finding about the GDP–inequality
   relationship; or let readers explore the relationship's history. For each, what should
   be kept, removed, or separated into another view? What would simplification conceal?

Do not presume all extra context is irrelevant: dates can expose changes across periods
that an unlabelled scatterplot would hide. Presidency labels supply historical context, not
evidence of a causal government effect. Cairo's descriptive interpretation is the subject of
critique; the source data and historical claims have not been independently reanalysed here.
The exercise concerns design and reading, not estimating a correlation or testing economics.
Use the full-resolution local crop if the dense labels need closer inspection.

Bridge to the audience–question brief: detail is useful when it serves the reader's task.
Also point out the source line and explanatory text as a preview of the figure-note topic.
This is an in-class discussion, not an additional graded assignment.

## Session 1 reveal: pooled and within-country relationships

**Instructor request recorded 3 November 2026:** show how an upward-sloping pooled regression
can coexist with downward-sloping relationships in every country. This is a continuous-data
illustration of Simpson's paradox. Use slides 14–15 of the local introduction deck before the
Figure 3 discussion and the audience–question brief.

1. Show all hotels in one colour and a single fitted line. Ask what association students see
   and whether they expect it to hold within every country. The pooled slope is +10.8 EUR/km.
2. Reveal country colours, distinct marker shapes, and separate fitted lines. Keep every
   observation, both axis ranges, and the pooled line fixed. Every country slope is -8 EUR/km.
   Ask students to explain the reversal before naming it.
3. Explain that the countries with higher average distances also have higher average prices.
   These between-country differences outweigh the negative relationships within countries.
   A joint model with separate country intercepts and a common slope gives -8 EUR/km too.

The 24 hotels and countries A, B, and C are entirely fictional. The slide source
[`simpson-reveal.mjs`](../presentations/session01/simpson-reveal.mjs) uses the local
`data/raw/simpson_hotels.csv`, prepared by `scripts/fetch_data.py`. See the
[data construction](../data/README.md#session-1-hotel-illustration). The country slopes are
equal by construction, so separate intercepts suffice here. Do not imply that this guarantees
equal slopes in other data or that either regression alone establishes causation.

**Design lesson:** group information can be essential evidence, not clutter. A single polished
line can hide the relationship relevant to the reader's question. Ask which comparison the
reader needs before choosing what to simplify. Both associations describe the constructed data;
which one matters depends on the question. No regression derivation or additional assessment
is introduced. The original editable charts use the deck's existing style.

Conceptual reference: Kievit et al. (2013),
[Simpson's paradox in psychological science: a practical guide](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00513/full).
The course example uses original constructed data and does not reproduce their figure.

## Statistical results, uncertainty, and fair presentation

**Instructor request recorded 3 November 2026:** teach how to visualise statistical results,
using an event study to make uncertainty visible. Main placement: **Session 2**, following
the existing example of department means with bootstrap intervals. Introduce the general
principle in Session 1, develop the accompanying note in Session 4, and revisit it in
Session 4 project review.

**Course-wide principle:** a figure should include the information readers need to judge its
claim fairly. One clear message is compatible with uncertainty and qualifications. Remove
distractions, not evidence that might weaken or change the conclusion. This connects directly
to the discussion of how much context Cairo's Figure 3 should include.

### Planned event-study example

Use a simple policy-event setting to show estimates at successive periods before and after
an intervention. Explain the outcome and the groups being compared before showing the plot.
The focus is reading and designing the figure, not deriving an estimator.

1. Show estimates alone and ask students to describe the apparent pattern.
2. Keep the estimates and scales fixed; add uncertainty intervals. Ask which earlier claims
   now need qualification. Do not hide periods because their estimates are imprecise.
3. Add or check time relative to the event, the event marker, the zero line, outcome units,
   and the reference period used for comparisons. For the implemented published example, pre-treatment changes use successive periods,
   whereas post-treatment effects use the last pre-treatment year. Year -1 is estimated,
   not a normalised reference zero.
4. Write a concise figure note identifying the sample, comparison group, model, and interval
   method. State the confidence level and whether intervals cover each estimate separately
   (**pointwise**) or the displayed path jointly (**simultaneous**). If standard errors account
   for related observations within groups, name those groups (the clustering level).
5. Revise the takeaway so that it reflects both the estimated magnitudes and their precision.
   Transfer the same questions to a coefficient plot or a plot of model predictions.

Implemented with the published `summary(mw.dyn)` output from Callaway and Sant’Anna's
real-data example: log teen employment, 500 counties in 2003–2007, minimum-wage increases,
no covariates and never-treated comparisons. Preserve the published 95% simultaneous
bands and rounded estimates. This is an illustrative application, not a definitive policy
finding. Cohort composition varies by event time.

### Interpretation safeguards

- A confidence interval describes uncertainty about an estimated quantity, not the spread
  of individual observations. Explain separately any interval for a future observation.
  See [NIST's explanation of confidence limits](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm).
- An interval crossing zero is not proof of no effect. Before-event estimates close to zero
  do not establish that the groups would have followed the same trend without treatment.
  The chart alone cannot establish causality. Distinguish evidence about individual periods
  from evidence about the whole path; see
  [Roth et al. (2023), especially §§4.4 and 4.6](https://jonathandroth.github.io/assets/files/DiD_Review_Paper.pdf).
- Uncertainty intervals do not automatically account for every source of bias or model
  uncertainty. Keep assumptions and important limitations visible in the note and discussion.

### Fair-presentation check for any figure

Ask: what is measured, for whom, in which units and time window, and compared with what?
Which observations, filters, denominators, or transformations determine the result? Is it
observed data, a summary, or a model estimate? What uncertainty and limitations matter for
the claim? Would omitted periods, groups, or results change the reader's judgment? Put the
essential information in the figure and its note; use supporting material for further detail.

**Development status:** implemented in Session 2 and its exercise, using published real-data estimates. The preparation script extracts and validates the table from pinned source HTML. Assessment requirements are unchanged.

## Figure and visualisation notes

**Instructor request recorded 3 November 2026:** explicitly teach how to write figure and
visualisation notes as an integral part of visual communication. Main placement: **Session 4,
Design and storytelling**, alongside titles and annotations. Introduce the purpose briefly
in Session 1 and revisit it during Session 4 project review and Session 6 dashboard critique.

Planned discussion:

- Distinguish the jobs of the text around a chart: the title establishes the subject or
  supported takeaway; an annotation points to a particular feature; a figure note explains
  how to read the evidence; a source line identifies its provenance. Alt text supplies an
  accessible description and serves a different purpose from a methodological note.
- Select the context the reader actually needs: definitions and units, population/sample,
  time and geographic coverage, aggregation and denominators, filters or exclusions, and
  what any uncertainty interval represents. Include limitations that affect interpretation.
- Name the actual data source and relevant transformations; disclose synthetic data. Check
  the wording against the code rather than writing a generic disclaimer.
- Keep notes concise and readable at the final display or print size. Essential context must
  travel with the exported figure. A caveat in small print cannot rescue a misleading title.
- Revisit Session 2's supplied event-study figure: the note must explain the comparison,
  reference period, and uncertainty intervals, not merely name the data source.

Planned exercise: show an existing course chart without its note and ask what a reader cannot
know from the image alone. Students draft a short note, check it against the data preparation,
and exchange the chart with a peer who has not seen the notebook. Revise any ambiguous or
unnecessary wording. This can form part of the existing redesign activity rather than a new
assignment.

**Development status:** recorded in the course outline and session plan; the dedicated
notebook example/exercise is still to be developed. No assessment weights or requirements
have changed.

## During class

- **Begin with purpose.** Name the audience and question before choosing a chart form. Revisit
  the reader's knowledge, intended use, and viewing context when making design choices.
- **Build visibly.** Start with a plain chart and improve it incrementally so each design choice
  has an observable effect.
- **Ask students to predict.** Pause before aggregation, chart selection, filtering, scale
  changes, and annotation.
- **Invite critique before giving the rule.** Let students identify what a weak version hides,
  exaggerates, or makes unnecessarily difficult to compare.
- **Interpret every output.** Ask for a sentence that states the claim, evidence, and an
  important limitation.
- **Use the AI activity as a verification demonstration.** Check generated code, transformations,
  encodings, and claims aloud; do not present generation as the end of the task.

## Session 5 proposal: a figure that updates as data arrive

**Instructor request recorded 3 November 2026:** show regularly generated observations
arriving in a live-updating chart, potentially delivered through a website.

**Current state:** `dashboards/app.py` reads a prepared, cached CSV. Its region selector
changes the displayed view; it does not collect new observations or refresh on a timer.
The course environment currently has Streamlit 1.58.0 with `st.fragment(run_every=...)`.

### Proposed classroom demonstration

Use a small, separate Streamlit app with a Plotly line chart. The audience is someone
monitoring a simulated room temperature and asking whether it is rising, falling, or stable.

- Generate one synthetic reading approximately every two seconds while the session is active.
  Show its actual observation timestamp and temperature in degrees Celsius. Clearly label
  the source as a simulation; do not present a recording as a real-time external feed.
- Retain the most recent 60 readings and state that window on the figure. Update the existing
  view rather than accumulating new charts. Keep the stored history bounded as well.
- Provide pause/resume and reset controls. In this first demonstration, pause stops both
  simulation and automatic chart updates. Explain that this differs from pausing only the
  display of an independently running sensor.
- Show the time of the latest observation. An old last value must not look like a fresh
  measurement. A chart refresh and a new observation are different events.
- Compare automatic vertical rescaling with a stable scale: which makes changes easier to
  judge over time? If values exceed a chosen range, make this visible rather than clipping
  silently. Discuss whether motion helps the monitoring task or distracts the reader.

Explain the mechanism in plain language: obtain a reading, add it to recent history, then
redraw the chart. Streamlit's timed fragment supplies the refresh mechanism, while session
state retains the history. This is periodic updating, not a guarantee of exact timing.
Each browser session initially runs its own simulation; a shared live source would need a
shared data store or service. A real source could later replace the generator with periodic
requests to an API, subject to its permissions and update rate.

### Hosting and course scope

Run locally first. Streamlit Community Cloud is a possible later hosting route for a shareable
website, after checking repository access, dependency installation, and data handling. The
browser view alone is not an always-on data collector: timed fragments run while a session
is active, and hosted apps can sleep. Continuous collection while nobody views the page
requires a separately running collector and persistent storage.

Keep this as optional instructor material outside the three confirmed Power BI workshops,
not another full application or a required deployment assignment. A later implementation should
document the simulation and checks alongside the course's data-generation tooling.

**Development status:** proposal recorded; no live-stream app, notebook changes, external
data connection, or public deployment has been implemented.

Technical references: [timed fragments](https://docs.streamlit.io/develop/api-reference/execution-flow/st.fragment),
[Community Cloud deployment](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy),
and [hosting limits and hibernation](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app).

## Sessions 5–6 Power BI and optional Python material

**Instructor decision, 4 November 2026:** use the final two sessions for Power BI, preserving
Sessions 1–4. The [workshop guides](../workshops/power-bi/) cover introduction/basic charts on
2 December and dashboard building on 9 December. They compress the practical sequence in the
[2024–25 syllabus](https://ceu.studyguide.timeedit.net/modules/ECBS5209?year=2024): interface,
charts, tables/KPIs, filters/slicers, interactivity and a dashboard demonstration. Apply the
earlier design/storytelling concepts rather than reteaching them here.

Keep one prepared dataset throughout. Show why field types and sum/average/count matter,
then build a line, bars, a table and summary cards. In the second class, combine the views,
add two slicers and deliberate interactions, check filtered totals and revise after critique.
Explain Desktop report versus Service dashboard terminology. Avoid advanced DAX, complex
modelling and platform administration. Access for non-Windows students remains to be confirmed.

Replace the standalone project class with short reviews in Sessions 2–4 (5, 5 and 10 minutes
of existing practice time). Review audience/question, chart/evidence, then narrative, notes
and verification. The unnumbered interactivity and project references remain optional
support, with clear labels and unchanged paths. The assessment format was subsequently revised
as recorded below; its 25%/75% weights remain unchanged.

## Individual figure assessment

**Instructor decision, 4 November 2026:** change only the 25% item. The instructor supplies
the data and question, and students design an original figure in Python. Accept only the
figure with its accompanying notes, without code, a separate rationale or other supporting
files. Redesign stays ungraded in-class practice. Preserve the 75% final project, including
its code, narrative, team option and other deliverables.

The revised rubric retains 20 points for answering the question, 20 for analytic correctness,
25 for design and 15 for communication/accessibility. The former code/rationale allocation
becomes 20 points for figure notes and transparency. Verification is still necessary, but
unsubmitted code is not graded. Put brief AI attribution in the notes. The actual dataset,
question, file format, submission route and deadline are still to be specified.

## Previous course materials and three-session Power BI proposal

**Evidence checked on 4 November 2026:**

- The earlier supplied `year=2024` link is the **2024/25** course, taught by Bence Arato.
  [Syllabus](https://ceu.studyguide.timeedit.net/modules/ECBS5209?year=2024);
  [Moodle course](https://ceulearning.ceu.edu/course/view.php?id=17664).
- The actual previous academic year is **2025/26**, taught by Francesca Conselvan.
  [Syllabus](https://ceu.studyguide.timeedit.net/modules/ECBS5209?year=2025);
  [Moodle course](https://ceulearning.ceu.edu/course/view.php?id=19132).
- Both syllabi state that teaching materials are distributed through CEU Learning. Both
  course pages require authenticated/enrolled access. The instructor confirms that we do
  not have the necessary enrolment. No original slides, exercise datasets or `.pbix` files
  have been accessed. No matching originals were found in the teaching workspace, Downloads
  or Desktop; Documents could not be searched because of filesystem permissions.
- The 2025/26 syllabus lists interface/data import and a first chart; core charts; tables
  and KPIs; filters/slicers; dashboard interactivity and storytelling; then final-assessment
  discussion. This verifies advertised topics, not exactly what was taught or which files
  students used. The local Power BI workshop guides are new material, not last year's files.
- Access or a copy would have to come from the previous instructor or CEU's Moodle
  administrator. The 2025/26 syllabus lists `conselvanf@ceu.edu` and programme coordinator
  `dashd@ceu.edu`. No contact has been made on the instructor's behalf.

**New instructor preference:** three non-Power-BI lectures followed by three Power BI
lectures. Preserve a dedicated Python mapping session and basic Python charting in Session 1.
**Confirmed by the instructor in the subsequent slide review on 4 November.** The schedule,
syllabus and introductory roadmap now use this allocation. It is not a claim about recovered material:

| Date | Proposed session | Core work |
| --- | --- | --- |
| 4 November | Basic charts and visual communication in Python | Short introduction; line, bar and scatter plots; labels, export and figure notes; one redesign exercise. |
| 11 November | Comparisons, statistical results and uncertainty in Python | Histogram and box plot; estimates with confidence intervals; one supplied event-study example; annotations and fair comparisons. |
| 18 November | Mapping in Python | Geographic data and joins; choropleth and proportional-symbol maps; projections, rates versus totals, legends and missing areas. |
| 25 November | Power BI introduction and charts | Interface, import and field types; lines/bars; aggregation and formatting. |
| 2 December | Power BI tables, KPIs and filtering | Tables/matrices and cards; filters, slicers, selection state and checking totals. |
| 9 December | Power BI dashboard/report building | A focused interactive report; layout, interactions, storytelling, validation and peer critique. |

Design, audience and notes recur in every session. Use prepared data/estimates to keep Session 2
focused on plotting rather than statistical estimation. Extra chart variants, extended OLS
derivations, Plotly/Streamlit and live updates stay optional. The gain is more Power BI practice;
the trade-off is less breadth and repetition in Python. Each class remains 100 minutes.
The active schedule, syllabus and introductory PDF now reflect this allocation. Notebook
consolidation and the remaining examples are still to prepare. The 25% assessment policy is unchanged.

## Notebook conventions

- Kernel: `Python 3 (ipykernel)`; environment managed by `uv` and locked in `uv.lock`.
- Read data from local `data/raw/` and `data/processed/` paths only; never download data in a
  notebook cell.
- Use `pd.read_csv(...)` with explicit paths and date parsing, or `gpd.read_file(...)` for
  geographic data. Save with `fig.savefig(...)`, showing the filename and export options.
  Do not hide these operations behind the course-specific `load` or `save_figure` helpers.
- Set the notebook kernel's working folder to the repository root so the relative paths
  resolve correctly. `scripts/fetch_data.py` prepares the data and creates `figures/`.
- Do not add package-install cells. The shared environment is the reproducible baseline.
- Save pedagogically useful figures to `figures/`; generated figures are ignored by Git.
- Release the teaching notebook only after checking that it runs from the repository root and
  that its written interpretation matches its output.

## Rebuilding and checking notebooks

The six teaching/exercise pairs and three optional references are generated programmatically:

```bash
uv run python scripts/build_notebooks.py
uv run python scripts/check_notebooks.py
```

Edit cells in `scripts/lecture_content.py`, `scripts/chart_tour.py`, or
`scripts/notebook_sources/`. `scripts/build_notebooks.py` controls the six-folder mapping.
Rebuild and execute changed examples; do not hand-edit notebook JSON.
