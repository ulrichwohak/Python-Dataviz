# Data Visualization and Storytelling (ECBS5209)

**Academic year** 2026-2027 · **Term** Fall · **Host unit** Department of Economics<br>
**Course level** 7 · **US credits** 1 · **ECTS credits** 2<br>
**Instructor** Ulrich Wohak, PhD · [wohaku@ceu.edu](mailto:wohaku@ceu.edu)<br>
**Meetings** Wednesdays, 17:40-19:20 · 4 November-9 December 2026 (6 sessions) · Room TBD<br>
**Course repository** [github.com/ulrichwohak/Python-Dataviz](https://github.com/ulrichwohak/Python-Dataviz)

---

## Background and overall aim

**Content.** This course teaches students to turn data into clear, honest, and purposeful
visual communication. It combines visual perception, chart selection, information design,
story structure, critique, and reproducible implementation in Python. Students move from
framing an audience and question to building, revising, and presenting a coherent data
story.

**Relevance.** Producing a chart is easy; producing the right chart for a particular reader,
decision, and body of evidence is not. Analysts must decide what deserves attention, select
an encoding that supports accurate comparison, expose uncertainty and limitations, and
guide readers without distorting the data. These skills matter in business analysis,
economics, finance, public policy, consulting, and data journalism.

**Approach.** The course treats visualization as both an analytical tool and a form of
communication. Alberto Cairo's principle that form should follow function provides the main
design and storytelling perspective. Tamara Munzner's what-why-how framework supplies a
systematic vocabulary for relating data, tasks, and visual encodings. Python is the main
implementation environment. The final three sessions cover Power BI foundations, comparisons and filtering, then dashboard building.

## Course prerequisites and technical requirements

Prerequisites:

- ECBS5293 Data Science 1: Setting up Data Science Projects.
- ECBS5294 Data Science 2.
- ECBS5208 Coding 1: Introduction to Python.

Students should already be comfortable with basic Python, pandas, Jupyter notebooks, file
paths, data aggregation, and Git-based course repositories. This course does not reteach
introductory programming.

Students must bring a laptop to every session. Before Session 1, they should install `uv`,
clone the course repository, and run:

```bash
uv sync
uv run python scripts/fetch_data.py
uv run jupyter lab
```

The supported environment is Python 3.12 managed by `uv`. Students should not install
packages from inside course notebooks.

## Waiting list handling

Priority is given to students in Department of Economics programs for which the course is a
required or designated elective component. Other students who meet the prerequisites are
admitted from the waiting list on a first-come, first-served basis, subject to program
priorities and available places.

## Learning outcomes

By the end of the course, students will be able to:

- Frame a visualization in terms of its audience, decision, question, and intended use.
- Distinguish exploratory visualization from explanatory presentation and move responsibly
  between the two.
- Describe data and analytical tasks before choosing a chart, using a practical
  what-why-how framework.
- Select effective marks, channels, scales, chart forms, and layouts for comparison, change,
  distribution, relationship, and spatial context.
- Apply perceptual principles, visual hierarchy, colour, typography, annotation, and
  small-multiple design to direct attention without distorting evidence.
- Identify misleading axes, inappropriate aggregation, inaccessible colour choices,
  unsupported emphasis, and other common visualization failures.
- Build and refine static visualizations with pandas, matplotlib, and seaborn.
- Build basic Power BI charts and a one-page interactive report, verifying its calculations,
  filters, layout, and design.
  Optional Python material introduces Plotly and Streamlit for interactive delivery.
- Communicate uncertainty, missingness, data limitations, and the boundary between
  description and causal explanation.
- Build a coherent, reproducible data story and explain every visual and technical decision.
- Critique visual work constructively and revise it in response to evidence and feedback.
- Use AI assistance critically, test generated code and chart recommendations, and disclose
  material assistance.

## Learning activities and teaching methods

The course consists of six interactive 100-minute sessions taught through explanation,
live coding, visual critique, prediction questions, short redesign exercises, and peer
discussion. Each session starts with a communication problem rather than a plotting
command. Students first identify the audience, task, and evidence; they then implement and
revise an appropriate visual form.

Each lecture's numbered folder contains a teaching notebook with fully written examples
and an ungraded exercise notebook. In Sessions 4–6, these are Power BI Desktop workshop
guides with optional Python checks. Design/annotation, Python interactivity and project
references remain optional support outside the six-lecture sequence.

The course uses public real data: US birth counts, donated Amazon purchase histories,
country CO₂ estimates and published minimum-wage event-study results. A preparation script
downloads fixed source versions and creates local files. We discuss sampling limitations,
units and uncertainty; only introductory mathematical illustrations remain synthetic.
In-class redesign exercises start
from a working but unsuitable visualisation for a stated audience and question. Students
identify the problem, change the visual form, verify the numbers, and explain their choices.
Session exercises are formative and are not graded.

Sessions 4–6 provide a compact Power BI sequence: foundations and basic charts; tables,
matrices, cards/KPIs, filters and slicers; then dashboard layout, interactions and storytelling.
Students apply design principles and verify calculations against a Python reference. Short
project reviews take place in Sessions 2–4. Plotly, Streamlit and the project-workshop notebooks
remain optional support. Graded work remains Python-centered.

## Assessment

Grading is based on a total score out of 100, in line with CEU Department of Economics and
Business grading guidelines. In particular:

- The median student can expect to receive a B+.
- Probably no more than one third of students can expect to receive an A or A-.
- The passing grade is 50%.

The final grade is based on two assessment components:

| Component | Weight | Detail |
| --- | ---: | --- |
| Three individual figures | 25% combined | Three equally weighted assignments. For each, submit an original figure answering the instructor's question using supplied data, with accompanying notes only. |
| Final Python data story | 75% | A coherent stakeholder-facing story using 3-5 visualizations, reproducible code, documented data, interpretation, limitations, and verification. Individual work or teams of up to three. |

### Individual figures

There are three individual figure assignments across the course, not one per lecture.
For each, the instructor supplies data and a question. Students design a figure from scratch
in Python that answers that question for the intended reader. Submit only the figure with
its accompanying notes, not code, a separate rationale or other supporting files.

The figure and notes must stand on their own. Include readable labels and units, and explain
the data source, sample, aggregation, filters, uncertainty and limitations where relevant.
Include any material AI assistance and verification briefly in the notes. The datasets,
questions and deadlines for all three assignments are TBD and will be announced later.
In-class redesign remains ungraded practice.

Each figure assignment is scored out of 100 using the same rubric. The three scores have
equal weight: their average contributes 25% of the final course grade.

| Criterion | Points |
| --- | ---: |
| Answer to the question | 20 |
| Analytic correctness | 20 |
| Encoding and design decisions | 25 |
| Communication and accessibility | 15 |
| Figure notes and transparency | 20 |

The rubric assesses the figure and notes only. Code quality and a separate rationale are not
assessed. Keep working code locally to verify your result.

### Final Python data story

Students develop an evidence-based narrative for a defined stakeholder. The submission must
contain a clear question, documented and appropriately prepared data, approximately three to
five connected visualizations, concise written interpretation, limitations, and code that
runs from the course environment. Static visualizations are sufficient. Plotly or Streamlit
may be used when interaction materially helps the audience answer a task; technical novelty
does not substitute for a clear story.

The project may be completed individually or in a team of up to three. Team submissions must
include a contribution statement identifying each member's work. All members must be able to
explain the complete narrative, evidence, and implementation.

The project is scored out of 100:

| Criterion | Points |
| --- | ---: |
| Audience, question, and narrative structure | 20 |
| Analytic correctness and evidential integrity | 20 |
| Visual selection and design | 25 |
| Stakeholder communication and synthesis | 15 |
| Reproducible Python workflow and data documentation | 15 |
| Responsible AI use and contribution transparency | 5 |

Submission channels and due dates are TBD. Detailed briefs and rubrics are provided in the
course repository.

## AI and assistance policy

The course position is **use AI, then verify**. AI coding assistants may be used to explore
alternatives, explain errors, suggest implementation steps, or critique a draft. They may
not replace the student's responsibility to address the analytical question, inspect the
data, judge the visual encoding, verify the code, or defend the conclusion.

Students must:

- Run and inspect all submitted code in the course environment.
- Check column names, filters, aggregations, joins, scales, units, labels, and exported
  figures against the underlying data.
- Reject recommendations that are misleading, inaccessible, irrelevant to the audience, or
  unsupported by the evidence.
- Disclose material AI assistance in graded work, naming the tool, the purpose, and the
  verification performed.
- Be able to explain every submitted line of code, visual choice, and conclusion.

Undisclosed or unverified AI output is not evidence of understanding and may receive no
credit for the affected criterion.

## Course contents and schedule

### Session 1 - 4 November · Python chart tour

- Short course motivation: visualization as a tool for understanding and communication.
- Line, bar and scatter plots for concrete questions.
- A first tour of histograms, box plots, violin plots and strip plots.
- Labels, titles, units, figure notes and export.
- Audience, chart choice and verification throughout live coding.
- Ungraded practice: redesign a chart to make its intended comparison clearer.

### Session 2 - 11 November · Comparisons and uncertainty

- Histograms and box plots for distributions and comparisons.
- Confidence-interval plots and the distinction between variation and uncertainty.
- A supplied event-study example: estimates, intervals, reference period and labels.
- Annotation and figure notes that preserve necessary context.
- Short project review: audience, question and evidence.

### Session 3 - 18 November · Mapping in Python

- Geographical joins and checks for unmatched regions.
- Choropleths and proportional symbols.
- Coordinate reference systems and projections.
- Meaningful denominators: rates versus totals, legends and missing areas.
- Short project review: chart choice, notes and interpretation.

### Session 4 - 25 November · Power BI foundations

- Interface, importing data and inspecting field types.
- Row meaning, aggregation and basic charts.
- Titles, units, sorting and readable formatting.
- Ungraded chart redesign and verification against a Python reference.
- Short project review: narrative, notes and revision priorities.

### Session 5 - 2 December · Power BI comparisons and filtering

- Tables and matrices for exact comparisons.
- Cards and KPIs, with meaningful targets where supplied.
- Visual, page and report filters; slicers and visible selection state.
- Check totals and comparisons under different filters.
- Save the report for the dashboard session.

### Session 6 - 9 December · Power BI dashboard building

- Layout, visual hierarchy and storytelling for a defined audience.
- Combine charts and summary indicators with deliberate interactions.
- Check filtered results, titles, notes and the default view.
- Peer critique and revision of the dashboard-style report.
- Distinguish Desktop reports from Service dashboards. Cloud publication, advanced DAX
  and platform administration are outside scope.

## Course materials, software, and reproducibility

All required Python materials are stored in the course repository. The standard workflow is:

```bash
uv sync
uv run python scripts/fetch_data.py
uv run jupyter lab
```

Core tools are Python 3.12, pandas, matplotlib, seaborn, Plotly, Streamlit, JupyterLab, and
`uv`. Geopandas supports the dedicated Python mapping session. Notebooks read local data and
do not download datasets during execution.

Students will receive Power BI setup instructions before Session 4. Power BI Desktop
requires a supported Windows environment;
the availability and access details of any institutional virtual environment are TBD. No
student should make a platform purchase for this course.

## Readings and further material

There is no required textbook purchase. Selected chapter recommendations will accompany
individual sessions.

Primary reference:

- Cairo, Alberto. *The Functional Art: An Introduction to Information Graphics and
  Visualization*. New Riders, 2013. Especially the discussions of function, audience,
  visual cognition, complexity, narrative structure, and interaction.

Secondary analytical reference:

- Munzner, Tamara. *Visualization Analysis and Design*. A K Peters/CRC Press, 2015. Especially the
  what-why-how framework, marks and channels, rules of thumb, colour, multiple views,
  interaction, and validation.

Further optional reading:

- Cairo, Alberto. *How Charts Lie*. W. W. Norton, 2019.
- Knaflic, Cole Nussbaumer. *Storytelling with Data*. Wiley, 2015.
- Tufte, Edward R. *The Visual Display of Quantitative Information*. Graphics Press, 2001.
- Official documentation for pandas, matplotlib, seaborn, Plotly, and Streamlit.

The course repository does not distribute copyrighted textbooks. Bibliographic and source
attribution is recorded in `NOTICE.md`.

## Contact details

Ulrich Wohak, PhD - instructor. [wohaku@ceu.edu](mailto:wohaku@ceu.edu). Office hours TBD.
