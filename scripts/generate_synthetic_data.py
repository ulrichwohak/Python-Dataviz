"""Generate archived prototype data in separate legacy-synthetic subfolders.

Current teaching data: use scripts/fetch_data.py instead. Legacy outputs must not
overwrite the published real-data event-study results used in Session 2.

Usage:
    uv run python scripts/generate_synthetic_data.py [--seed N]

Deterministic: the same seed always produces identical files.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Make `src/` importable when run as a plain script (not only as an installed package).
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from dataviz_course.synthetic_data import generate_all  # noqa: E402
from dataviz_course.utils import SEED  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=SEED, help=f"random seed (default: {SEED})")
    args = parser.parse_args()

    written = generate_all(
        seed=args.seed,
        raw_dir=ROOT / "data/raw/legacy-synthetic",
        processed_dir=ROOT / "data/processed/legacy-synthetic",
    )
    print(f"Generated {len(written)} datasets (seed={args.seed}):")
    for name, path in written.items():
        rel = path.relative_to(path.parents[2]) if len(path.parents) >= 3 else path
        print(f"  - {name:13s} -> {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
