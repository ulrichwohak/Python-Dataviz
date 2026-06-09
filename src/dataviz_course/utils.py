"""Small, dependency-light utilities shared across scripts and notebooks.

Everything here is about *locating* and *saving* things in a way that works the same on
macOS, Windows, and Linux, and regardless of the working directory a notebook is launched
from. Plotting style and chart helpers live in :mod:`dataviz_course.plotting`.
"""

from __future__ import annotations

from pathlib import Path

# A single fixed seed makes every generated dataset reproducible across machines.
SEED = 42


def find_repo_root(start: Path | str | None = None) -> Path:
    """Return the repository root by walking up until ``pyproject.toml`` is found.

    Notebooks may be launched from anywhere (``notebooks/completed`` in Jupyter, the repo
    root in CI), so we resolve paths relative to the project rather than the CWD.
    """
    here = Path(start) if start is not None else Path.cwd()
    here = here.resolve()
    for candidate in (here, *here.parents):
        if (candidate / "pyproject.toml").exists():
            return candidate
    raise FileNotFoundError(
        "Could not locate the repository root (no pyproject.toml found above "
        f"{here}). Run from inside the Python-Dataviz repository."
    )


REPO_ROOT = find_repo_root(Path(__file__).parent)
DATA_RAW = REPO_ROOT / "data" / "raw"
DATA_PROCESSED = REPO_ROOT / "data" / "processed"
FIGURES = REPO_ROOT / "figures"


def ensure_data_dirs() -> None:
    """Create the data and figure output folders if they do not already exist."""
    for path in (DATA_RAW, DATA_PROCESSED, FIGURES):
        path.mkdir(parents=True, exist_ok=True)


def save_figure(fig, name: str, *, dpi: int = 150) -> Path:
    """Save a matplotlib figure into ``figures/`` and return the written path.

    ``name`` may include or omit an extension; ``.png`` is assumed when none is given.
    """
    FIGURES.mkdir(parents=True, exist_ok=True)
    target = FIGURES / (name if Path(name).suffix else f"{name}.png")
    fig.savefig(target, dpi=dpi, bbox_inches="tight")
    return target


__all__ = [
    "SEED",
    "REPO_ROOT",
    "DATA_RAW",
    "DATA_PROCESSED",
    "FIGURES",
    "find_repo_root",
    "ensure_data_dirs",
    "save_figure",
]
