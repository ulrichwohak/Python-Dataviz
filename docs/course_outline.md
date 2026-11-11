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

**Motivating a research question:** a simple descriptive figure can reveal a puzzle or
illustrate why a hypothesis is worth investigating. Distinguish the observed pattern, its
possible explanations, and the evidence needed to examine them.

**Design for the actual audience:** identify what readers know, what they need to understand
or decide, and how they will encounter the figure. Adapt content, terminology, visual emphasis,
and level of detail as well as appearance. Compare an academic-paper figure with a management
presentation, using explicit reader briefs rather than treating either as a fixed style.
Both versions must preserve the evidence and qualifications needed for a fair interpretation.

The notebooks use public real data downloaded in fixed versions by
[`scripts/fetch_data.py`](../scripts/fetch_data.py): SSA births, donated Amazon purchases,
OWID / Global Carbon Budget emissions and NOAA monthly state temperatures. Footwear OLS estimates are prepared from these observed purchases and temperatures.
Notebooks read local files. Source notes distinguish administrative counts, convenience
samples and statistical estimates; see the [data README](../data/README.md).

## Session sequence

| Session | Focus | Practical work |
| --- | --- | --- |
| 1. Python chart tour | Purpose and audience through concrete chart choices | Line, bar and scatter plots; first look at histograms, box, violin and strip plots; labels, notes, export and redesign |
| 2. Comparisons and uncertainty | Distribution, variation and uncertainty | Cumulative price distributions, a calendar-label scatterplot reveal, and OLS coefficient intervals |
| 3. Mapping in Python | Spatial comparison and meaningful denominators | Geographical joins, choropleths, proportional symbols and projections |
| 4. Power BI foundations | Correct quantities and readable basic charts | Interface, import, field types, aggregation and chart construction |
| 5. Power BI comparisons and filtering | Exact comparisons and transparent selections | Tables, matrices, cards/KPIs, filters and slicers |
| 6. Power BI dashboard building | Layout, interaction and storytelling | Build a dashboard-style report and check filtered results |

This is the confirmed three-Python/three-Power-BI sequence. The twelve scheduled notebooks now match these six titles and numbers. The
[notebook index](../notebooks/README.md) links each teaching notebook and exercise.
Optional references sit outside the numbered sequence.

Concrete dates and notebook links are in
[`schedule/session_plan.md`](../schedule/session_plan.md).

Session 2 opens with collected visualisations and Week 1 birth-chart redesigns in the
[presentation](../presentations/session02/README.md). Compare monthly totals, month-to-month
changes and births per day before turning to the footwear data. The notebook investigates
budget shares through cumulative distributions, calendar patterns through scatterplots,
and uncertainty through OLS coefficient intervals. The final exercise asks you to redesign
a chart comparing seasonal purchasing patterns.

The [course introduction](../presentations/session01/course-introduction.pdf) covers
administration, assessment and examples of visual reasoning.

Figure notes are part of each visualisation: identify units, sample, period, aggregation,
source and relevant limitations. Statistical-result charts also need a clear explanation
of the estimated quantity and uncertainty. Mapping adds geographical coverage, projection,
missing areas and denominators. Apply the same principles in Power BI.

## Power BI in Sessions 4–6

The [Power BI material map](../workshops/power-bi/) places foundations and basic charts in
Session 4, tables/matrices/cards and filtering in Session 5, and dashboard building in
Session 6. Each class has a teaching and exercise notebook.

Use one prepared table. Advanced DAX, complex models and platform administration remain
outside scope. Distinguish a Desktop report page from a Service dashboard; no Service
publication is required. Access arrangements will be announced before Session 4.

Session 2 closes with a redesign of seasonal footwear charts and comparison of figures. Short project
reviews remain in Sessions 3–4. The former project-workshop notebooks and
Plotly/Streamlit remain optional support. Both assessed deliverables remain Python-centred.

## In-class redesign practice

In each [exercise notebook](../notebooks/README.md), evaluate a supplied chart against
a reader's question, develop an alternative and check the underlying calculation.
The exercises cover time trends, distributions and intervals, mapping, and Power BI comparisons. Their purpose is
to practise visual reasoning, not merely to replace colours or imitate a single model answer.

## Assessment

| Item | Weight | Evidence of learning |
| --- | ---: | --- |
| [Three individual figures](../assignments/chart-critique-redesign/) | 25% combined | Three equally weighted assignments, each answering an instructor-supplied question using supplied data; correct analysis, effective design and self-contained notes; figure and notes only |
| [Final Python data story](../assignments/final-data-story/) | 75% | Narrative coherence; analytical relevance; visual design; technical implementation; verification; limitations; reproducibility |

The average of the three figure scores contributes 25%. Their datasets, questions and deadlines
are TBD. Weekly notebook exercises are formative practice. They support the assessments but are not
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
