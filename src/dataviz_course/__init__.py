"""Helper package for the *Data Visualisation with Python* course.

Re-exports the most commonly used helpers so notebooks can simply do::

    from dataviz_course import load, set_house_style, save_figure
"""

from __future__ import annotations

from . import plotting, synthetic_data, utils
from .loaders import available, load
from .plotting import HOUSE_PALETTE, set_house_style
from .utils import DATA_PROCESSED, DATA_RAW, FIGURES, REPO_ROOT, SEED, save_figure

__version__ = "0.1.0"

__all__ = [
    "plotting",
    "synthetic_data",
    "utils",
    "load",
    "available",
    "set_house_style",
    "HOUSE_PALETTE",
    "save_figure",
    "REPO_ROOT",
    "DATA_RAW",
    "DATA_PROCESSED",
    "FIGURES",
    "SEED",
    "__version__",
]
