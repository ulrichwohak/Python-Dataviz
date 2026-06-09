# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

Course material and environment for **"Data Visualisation with Python"** — an MSc Business Analytics course at CEU, taught through live coding (one Jupyter notebook per lecture).

**Current state: functional phantom/prototype repository.** The uv project, deterministic synthetic datasets, generated notebooks, dashboard, validation scripts, and CI workflow are scaffolded. The authoritative blueprint is the untracked file **`course repo.md`**: read it before substantive structural changes, since it defines the conventions this repo follows (it was written for a sibling course and is reused here).

This is initially a **phantom/test** repository: its job is to validate the technical workflow (uv setup, notebook design, plotting, dashboards, live-coding format) before real datasets and final content are chosen. **All datasets must be synthetic/fake**, generated deterministically from a random seed by repository scripts — never real or confidential data, and no live downloads inside notebooks.

## Environment & commands

`uv` only. Never use `pip`, `%pip`, `!pip`, `pipenv`, `Pipfile`, or `conda` (the sole allowed mention is a warning telling students not to use them). Target Python 3.12. Required files once bootstrapped: `.python-version`, `pyproject.toml`, `uv.lock`.

Student/instructor entry point:
```bash
uv sync
uv run jupyter lab
```

Target acceptance sequence (these scripts do not exist yet — create them per `course repo.md`):
```bash
uv lock --check
uv sync --locked
uv run python scripts/fetch_data.py        # prepares local data; no downloads in this prototype
uv run python scripts/check_no_pip.py      # rejects pip/conda instructions in student-facing files
uv run python scripts/check_notebooks.py   # validates notebook JSON, kernelspec, imports, syntax, local data refs
uv run ruff check .
```
For documentation-only changes, at minimum run `uv run python scripts/check_no_pip.py`.

CI (GitHub Actions with `astral-sh/setup-uv`) runs the same five-command sequence. Add CI only after the core project, lectures, and scripts exist, or early runs will fail.

## Key conventions (from `course repo.md`)

- **Self-contained materials.** Students clone, `uv sync`, fetch data via scripts, and work entirely from local files. Required materials live in the repo; never link students to upstream notebooks as required reading. Credit external sources in `README.md` / `NOTICE.md`.
- **Data policy.** No `pd.read_csv("https://...")` in notebooks. Data preparation goes through `scripts/fetch_data.py`; for this prototype it generates synthetic local files and performs no downloads. `data/raw/` and `data/processed/` stay git-ignored except `.gitkeep`. Notebooks read local paths.
- **Notebook standards.** Valid JSON; `Python 3 (ipykernel)` kernelspec; executable top-to-bottom; clear stale/large outputs; no package-install cells. Generate notebooks programmatically (e.g. an `nbformat` builder) rather than hand-editing JSON, and verify by headless execution (`uv run --with jupyter jupyter nbconvert --to notebook --execute`).
- **Homework is build-on-demand.** Do not create homework by default — ask the instructor which delivery format they want first. (The guide documents a stand-alone "debug repository" model used by another course; treat it as reference, not a default for this one.)
- **Schedule.** Put unknown institutional dates as explicit placeholders like `READING_WEEK_TBD`; do not guess.

## Development workflow

Use the GitHub **issue → branch → pull request → merge** flow for new changes; do not commit directly to `main`. Keep PRs small (roughly one per lecture or support area). This local prototype was scaffolded in one working tree, but future changes should be split by support area or lecture.

Interact with GitHub via the `gh` CLI. The personal access token lives in **`.secrets.md`**.

## Secrets

`.secrets.md` contains a GitHub PAT and **must never be committed**. There is currently **no `.gitignore`**, so `.secrets.md` is unprotected — create a `.gitignore` covering `.secrets.md`, `.venv/`, `data/raw/*` (keeping `.gitkeep`), and scratch output as part of the foundation work. Keep local planning notes (and `course repo.md` itself) untracked unless the instructor asks to commit them.
