# Course Outline — ECBS5209 Data Visualization and Storytelling

**MSc Business Analytics, CEU · six Wednesdays · 17:40–19:20 · 4 November–9 December 2026**

## Course logic

This is a design and communication course implemented in Python. We treat graphics as a form
of communication: design choices shape what a reader notices, understands, and may misinterpret.
Evaluate a figure by the understanding it enables and how faithfully it represents the evidence.
Students repeatedly work through the same sequence:

1. identify the audience, question, and intended use;
2. understand the data and the comparisons that matter;
3. select and justify visual encodings;
4. implement the visualisation in reproducible Python;
5. critique what the chart reveals, hides, or risks distorting, including omitted uncertainty; and
6. revise the design and narrative after feedback and verification.

The course therefore does not treat design and storytelling as cosmetic topics saved for one
late session. They are practised from the first chart onward. Each teaching notebook provides
fully written examples or Power BI steps, explanations and numerical checks. A separate
exercise notebook supplies practice for that lecture.

**Fair presentation:** include the information readers need to judge the evidence. A clear
main message must remain compatible with uncertainty, relevant comparisons, and limitations.
Simplification should remove distractions, not qualifications that could change the conclusion.

**Purpose before message:** state what the figure should help its reader do. An explanatory
figure communicates a finding supported by the evidence; an exploratory figure enables a
question to be investigated without prescribing the answer. A figure accompanying a claim
should let readers assess that claim. Curiosity can invite this investigation, but essential
context must remain visible. Ask what the reader would lose if the figure were removed.
See the [purpose discussion](live_coding_notes.md#why-make-this-figure).

**Motivating a research question:** a simple descriptive figure can reveal a puzzle or
illustrate why a hypothesis is worth investigating. Distinguish the observed pattern, its
possible explanations, and the evidence needed to examine them. Introduce this in Session 1
and revisit it during the short project reviews in Sessions 2–4. See the
[teaching note](live_coding_notes.md#a-descriptive-figure-can-motivate-a-hypothesis).

**Design for the actual audience:** identify what readers know, what they need to understand
or decide, and how they will encounter the figure. Adapt content, terminology, visual emphasis,
and level of detail as well as appearance. Compare an academic-paper figure with a management
presentation, using explicit reader briefs rather than treating either as a fixed style.
Both versions must preserve the evidence and qualifications needed for a fair interpretation.
See the [teaching record](live_coding_notes.md#audience-adaptation-throughout-the-course).

The notebooks use public real data downloaded in fixed versions by
[`scripts/fetch_data.py`](../scripts/fetch_data.py): SSA births, donated Amazon purchases,
OWID / Global Carbon Budget emissions and published real event-study estimates.
Notebooks read local files. Source notes distinguish administrative counts, convenience
samples and statistical estimates; see the [data README](../data/README.md).

## Session sequence

| Session | Focus | Practical work |
| --- | --- | --- |
| 1. Python chart tour | Purpose and audience through concrete chart choices | Line, bar and scatter plots; first look at histograms, box, violin and strip plots; labels, notes, export and redesign |
| 2. Comparisons and uncertainty | Distribution, variation and uncertainty | Histograms, box plots and confidence-interval plots, including supplied event-study results |
| 3. Mapping in Python | Spatial comparison and meaningful denominators | Geographical joins, choropleths, proportional symbols and projections |
| 4. Power BI foundations | Correct quantities and readable basic charts | Interface, import, field types, aggregation and chart construction |
| 5. Power BI comparisons and filtering | Exact comparisons and transparent selections | Tables, matrices, cards/KPIs, filters and slicers |
| 6. Power BI dashboard building | Layout, interaction and storytelling | Build a dashboard-style report and check filtered results |

This is the confirmed three-Python/three-Power-BI sequence. The twelve scheduled notebooks now match these six titles and numbers. The
[notebook index](../notebooks/README.md) links each teaching notebook and exercise.
Optional references sit outside the numbered sequence.

Concrete dates and notebook links are in
[`schedule/session_plan.md`](../schedule/session_plan.md).

Session 1's [course introduction](../presentations/session01/course-introduction.pdf) begins with
Shneiderman's “The purpose of visualization is insight, not pictures,” quoted in Cairo
(printed p. xx). Course administration and expectations precede a short OLS reveal: scalar and matrix notation become visible as
a scatterplot followed by the same observations with an estimated OLS line. It introduces
visualisation as an aid to understanding before the audience–question brief. Matrix algebra
provides another representation of the same example, not a separate assessed topic.

Next reveal **Simpson's paradox** with fictional hotels: one positive pooled
slope becomes three negative within-country slopes when country membership is shown.
The data and axes stay fixed. This motivates visualisation as a way to expose important group
structure and decide which comparison answers the question. See the
[teaching sequence](live_coding_notes.md#session-1-reveal-pooled-and-within-country-relationships).

Then discuss Cairo's **Figure 3** (printed p. xix), comparing the demands of a focused
academic argument with historical exploration. Students critique the competing messages and
decide which context each purpose needs. See the
[discussion record](live_coding_notes.md#session-1-discussion-cairos-figure-3); the textbook
image is kept in a local instructor deck, not distributed in the repository.

Figure notes start with the first exported chart in Session 1. Session 2 adds uncertainty and
reference-period explanations; Session 3 adds geographical coverage, projection and denominator
information. Apply the same principles to Power BI and project review. See the
[teaching record](live_coding_notes.md#figure-and-visualisation-notes).

Session 2 includes supplied event-study estimates with confidence intervals. Keep attention on
how to display and explain them, rather than estimating a model. Include the reference period,
zero line, units and interval meaning. The published Callaway–Sant’Anna real-data example uses 95% simultaneous bands, documented in the data README. Do not normalise year -1 to zero; it is an estimated pre-treatment contrast in this output.

A possible optional Python extension is a **live-updating figure**: synthetic
observations arrive at regular intervals and a browser chart updates its recent history.
Use it to discuss timestamps, stable scales, pause controls, and the difference between a
live display and continuous data collection. Website hosting is a possible extension, not
a graded requirement. See the [proposal](live_coding_notes.md#session-5-proposal-a-figure-that-updates-as-data-arrive);
the app has not yet been built or deployed.

## Power BI in Sessions 4–6

The [Power BI material map](../workshops/power-bi/) places foundations and basic charts in
Session 4, tables/matrices/cards and filtering in Session 5, and dashboard building in
Session 6. The existing guides are newly authored resources, not recovered teaching files
from last year. Each class now has its own teaching and exercise notebook; the older guide links point to them.

Use one prepared table. Advanced DAX, complex models and platform administration remain
outside scope. Distinguish a Desktop report page from a Service dashboard; no Service
publication is required. Confirm access for non-Windows users before Session 4.

Short project reviews remain in Sessions 2–4. The former project-workshop notebooks and
Plotly/Streamlit remain optional support. Both assessed deliverables remain Python-centred.

## In-class redesign practice

Students receive an unsuitable chart, its executable code, and a specific audience and
question. They diagnose the mismatch, sketch an alternative, implement it, and check that
the redesign preserves the intended calculation. See [the activity guide](redesign-activities.md).
The exercises cover weekly trends, distributions and intervals, mapping, and Power BI comparisons. Their purpose is
to practise visual reasoning, not merely to replace colours or imitate a single model answer.

## Assessment

| Item | Weight | Evidence of learning |
| --- | ---: | --- |
| [Individual figure](../assignments/chart-critique-redesign/) | 25% | Original figure answering an instructor-supplied question using supplied data; correct analysis, effective design and self-contained notes; figure and notes only |
| [Final Python data story](../assignments/final-data-story/) | 75% | Narrative coherence; analytical relevance; visual design; technical implementation; verification; limitations; reproducibility |

Weekly notebook exercises are formative practice. They support the two graded items but are not
separate graded quizzes.

## Learning resources

The notebooks and in-class critique are the required technical materials. Two books provide the
course's conceptual vocabulary and optional/selective readings:

- Alberto Cairo, *The Functional Art: An Introduction to Information Graphics and
  Visualization* (New Riders, 2013). Cairo is the primary guide for function, audience,
  exploration and explanation, cognition, narrative, and the design process.
- Tamara Munzner, *Visualization Analysis and Design* (A K Peters/CRC Press, 2015). Munzner
  supports the course's what–why–how framing, marks and channels, colour, interaction, multiple
  views, and validation.

The publisher records are linked in [`NOTICE.md`](../NOTICE.md). No copyrighted textbook file
is distributed in this repository.

## Learning and verification practices

- **Audience throughout:** revisit the reader brief before each design choice and ask what
  would need to change for another audience or delivery format.
- **Critique before polish:** students articulate what works and what fails before changing code.
- **One decision at a time:** live coding makes the effect of each encoding or design choice visible.
- **Interpret, do not decorate:** every chart ends with a written claim and a check that the
  visual evidence supports it.
- **Use AI, then verify:** students may use AI assistants, but must test code, inspect
  transformations, check scales and encodings, and disclose material assistance. See the
  [`AI policy`](ai_policy.md).
- **Reproducible delivery:** notebooks read local data, run from the repository root, and use the
  locked `uv` environment.
