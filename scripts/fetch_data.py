"""Prepare all local data files for the course.

This prototype repository has no external datasets to download. The standard course
entrypoint is still named ``fetch_data.py`` so future courses have one obvious place for data
preparation; here it delegates to deterministic synthetic-data generation and performs no
network calls.

Usage:
    uv run python scripts/fetch_data.py [--seed N]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Make `src/` importable when run as a plain script (not only as an installed package).
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from dataviz_course.synthetic_data import generate_all  # noqa: E402
from dataviz_course.utils import SEED  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=SEED, help=f"random seed (default: {SEED})")
    args = parser.parse_args()

    written = generate_all(seed=args.seed)
    print("No external downloads required for this prototype.")
    print(f"Generated {len(written)} synthetic datasets (seed={args.seed}):")
    for name, path in written.items():
        print(f"  - {name:13s} -> {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
