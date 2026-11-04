# Final data-story project

Copy this folder and rename it for your submission. Replace the prompts below with your own
content; do not delete the reproduction information a marker needs.

Read the full [final-project brief](../assignments/final-data-story/) before starting.

## Audience, decision, and question

- **Audience:** `Who needs this analysis?`
- **Decision or discussion:** `What should the story help them decide or understand?`
- **Central question:** `Write one answerable question.`

## Executive summary

In one short paragraph, state the main finding, the evidence that supports it, and its practical
implication. Write this last, after verification.

## Project structure

```text
your-project/
├── README.md
├── story.md
├── ai-disclosure.md
├── contribution-statement.md
├── notebooks/          # or Python scripts; keep the execution order obvious
├── data/
│   └── README.md
└── figures/
```

Use [`story-template.md`](story-template.md) to plan the narrative. Complete
[`ai-disclosure.md`](ai-disclosure.md), [`contribution-statement.md`](contribution-statement.md),
and [`data/README.md`](data/README.md). Keep only final assessed figures in `figures/`.

## Reproduce the analysis

From the course-repository root, synchronise the locked environment. If you use the course's
course data, prepare it with the second command:

```bash
uv sync --locked
uv run python scripts/fetch_data.py
# Replace this line with the command that runs your project.
```

If you use an approved external dataset, replace the `fetch_data.py` step with your documented
local preparation command. The marker must be able to reproduce the input without a private
credential or an undocumented manual download.

If you submit notebooks, list their execution order and confirm that each runs from top to bottom
with the course kernel. Do not require private credentials or manual edits to reproduce the
assessed output.

## Data source and limitations

Summarise the source, observation unit, coverage, and most important limitations here. Put the
full provenance and data dictionary in [`data/README.md`](data/README.md).

## Verification summary

List the most consequential checks you performed. Include at least one direct numerical check for
each final chart and identify any issue you found and corrected.
