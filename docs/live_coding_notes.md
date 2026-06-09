# Live-Coding Notes (Instructor)

Each session is built live from the matching skeleton in [`notebooks/live/`](../notebooks/live/).
The fully developed version in [`notebooks/completed/`](../notebooks/completed/) is the
post-class reference and the source of truth for what each session should reach.

## Before class

```bash
uv sync
uv run python scripts/fetch_data.py                # ensure data/ is populated
uv run jupyter lab
```

Open the week's `live/` notebook. Keep the `completed/` notebook nearby as your map.

## During class

- **Start from the business question.** Motivate the chart before writing code.
- **Build plots incrementally.** Show the plain plot first, then improve it (labels, colour,
  annotation). The diff is the lesson.
- **Use the "pause and predict" prompts.** Ask students to predict the chart before running.
- **Surface the common mistakes** in each completed notebook on purpose, then fix them.
- **Run the AI co-pilot activity** live: prompt an assistant, then apply the verification
  checklist out loud so students see the *verify* half, not just the *generate* half.

## Notebook conventions

- Kernel: `Python 3 (ipykernel)`; environment is `uv`-managed (`.venv`).
- Read data from local `data/raw` / `data/processed` paths only — never download in a cell.
- No package-install cells (`%pip` / `!pip`); the environment is fixed by `uv.lock`.
- Save at least one figure per session to `figures/` (git-ignored; regenerated on run).

## Rebuilding the notebooks

The notebooks are generated programmatically so the three variants stay in sync:

```bash
uv run python scripts/build_notebooks.py
```

Edit cell content in [`scripts/build_notebooks.py`](../scripts/build_notebooks.py), not the
notebook JSON, then rebuild. Validate with `scripts/check_notebooks.py`.
