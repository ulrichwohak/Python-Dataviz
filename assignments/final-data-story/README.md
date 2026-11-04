# Graded item 2: Final Python data story

| Field | Value |
| --- | --- |
| Weight | 75% |
| Mode | Individual or team of up to three students |
| Due date | `TBD` |
| Submission route | `TBD` |

## The task

Create a concise, evidence-led data story for a defined stakeholder. The story should answer one
important question through **three to five coherent visualisations**, not present a gallery of
unrelated charts. Use Python for data preparation, analysis, and every assessed visualisation.

Your reader should be able to understand:

1. the decision or problem at stake;
2. the evidence and progression across the charts;
3. the principal finding and its practical implication; and
4. the limits of what the evidence can support.

Start from a copy of [`project_template/`](../../project_template/).

## Scope and data

You may use the course's documented public datasets or another dataset approved by the instructor. An
external dataset must be lawful to use, non-confidential, documented, and available to the
marker without a private credential. Keep all analysis inputs local. If redistribution is not
allowed, include a reproducible preparation script and precise source instructions instead of
the restricted file.

Use a question narrow enough to answer well. Three strong charts are sufficient. A fourth or
fifth chart should add a genuinely different piece of evidence, not repeat the same comparison.
An interactive element is optional and should be included only when it helps the audience ask a
meaningful follow-up question.

## Required deliverables

Submit one project folder containing:

1. `README.md`: audience, question, one-paragraph executive summary, data source, limitations,
   and exact reproduction commands;
2. one or more `.py` files or notebooks containing all preparation, checks, and chart code,
   runnable from top to bottom in the course environment;
3. `story.md`: the stakeholder-facing narrative, with the three to five final charts in their
   intended reading order and concise text connecting the evidence;
4. `figures/`: legible exports of all assessed charts;
5. `data/README.md`: provenance, licence or terms, grain, key fields, transformations, and any
   data file that may lawfully be shared;
6. `ai-disclosure.md`: material AI use and verification evidence, or an explicit statement that
   no material AI assistance was used; and
7. `contribution-statement.md`: required for every submission. Individuals identify the work as
   individual; teams name each member's specific contributions and confirm that every member can
   explain the complete submission.

The marker must not need to edit paths, click through manual data-cleaning steps, or reconstruct
missing calculations to reproduce the story.

## Story and design requirements

- Open with the stakeholder's question, not with a description of the dataset.
- Give each chart a distinct role in the sequence: establish context, reveal a pattern, test an
  explanation, compare alternatives, or support the implication.
- Use titles that communicate evidence without overstating it.
- Make scales, denominators, time windows, units, filters, uncertainty, and missing data clear.
- Use visual hierarchy and annotation to guide attention while preserving relevant context.
- Design for accessibility: sufficient contrast, readable type, and redundant cues whenever
  colour carries meaning.
- Distinguish description from causal explanation. Do not make a causal claim from descriptive
  evidence alone.

## Reproducibility and verification

Before submission, run the complete project in a fresh process and recreate every assessed
figure. At minimum, document checks of:

- row counts and the unit of observation before and after major transformations;
- joins, duplicate keys, missing values, and filters relevant to the claims;
- displayed totals, percentages, rankings, date ranges, and category order;
- agreement between narrative claims and the values encoded in each chart; and
- colour, contrast, labels, and legibility at normal viewing size.

AI tools are permitted under the course's **use, then verify** policy. You remain responsible for
every line, aggregation, encoding, and claim. The Power BI workshops are ungraded: a Power
BI file may be included as supplementary work, but it cannot replace the Python story or improve
an otherwise incomplete Python submission.

## Suggested process

The following checkpoints are formative rather than additional graded items:

1. Write a one-sentence audience, decision, and question.
2. Audit the data and draft a claim–evidence storyboard.
3. Prototype more views than you intend to keep.
4. Select three to five charts and arrange them in a deliberate sequence.
5. Test the draft on a peer who has not seen the analysis.
6. Revise, verify, rerun, and export the final story.

## Rubric (100 points)

| Criterion | Points | Full-credit evidence |
| --- | ---: | --- |
| Audience, question, and narrative structure | 20 | Defines a consequential, appropriately scoped stakeholder question; develops a coherent evidence sequence; gives every chart a clear role and connects it to the central takeaway. |
| Analytic correctness and evidential integrity | 20 | Uses sound transformations and comparisons; verifies joins, filters, denominators, dates, and displayed values; treats missingness and uncertainty transparently; avoids claims the data cannot support. |
| Visual selection and design | 25 | Chooses effective forms and encodings; applies hierarchy, ordering, scale, colour, typography, and annotation purposefully; charts are consistent, accessible, legible, and free of avoidable clutter or distortion. |
| Stakeholder communication and synthesis | 15 | Titles and prose explain what matters in plain language; the conclusion synthesises evidence across charts; implications are useful and limitations are candid. |
| Reproducible Python workflow and data documentation | 15 | The project runs from top to bottom in the course environment; paths are portable; code is readable; inputs, provenance, transformations, and reproduction commands are complete. |
| Responsible AI use and contribution transparency | 5 | Discloses material AI assistance and concrete verification, or states none was used; contribution statement is specific and complete, and all team members can explain the submission. |
| **Total** | **100** | |

A polished story built on a materially wrong calculation cannot demonstrate full achievement in
analytic correctness, visual design, or stakeholder communication. A story that cannot be
reproduced cannot earn full reproducibility credit.
