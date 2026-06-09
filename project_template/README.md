# Project Template

A starting point for the final data-story project. Copy this folder, rename it, and build your
project inside it.

## Structure

```text
project_template/
├── README.md       # this file — replace with your project's README
├── notebooks/      # your analysis notebook(s)
├── data/           # your input data (synthetic or approved — see the AI/data policy)
└── figures/        # exported charts for your write-up
```

## What a good project does

1. **Asks one clear question** a stakeholder would care about.
2. **Prepares the data** into a tidy shape (Week 2 skills).
3. **Builds 2–4 charts** that answer the question, chosen deliberately (Weeks 3–6).
4. **Designs for the reader** — takeaway titles, decluttered, honest axes (Week 5).
5. **States a conclusion** the charts actually support.
6. **Passes the verification checklist** in [`docs/ai_policy.md`](../docs/ai_policy.md), including
   any AI-assisted parts.

## Environment

Use the course environment — `uv sync` at the repository root, then
`uv run jupyter lab`. Read data from local paths; do not download data inside notebooks.

## Submission

Delivery format is set by the instructor each term. Do not assume a format — check the course
schedule and announcements.
