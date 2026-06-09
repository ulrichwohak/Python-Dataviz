"""Reject legacy package-management instructions in student-facing files.

The course environment is managed with `uv` only. This check fails if it finds `pip`,
`%pip`, `!pip`, `pipenv`, `Pipfile`, or `conda` install instructions in Markdown, notebooks,
or docs — except where they appear in an explicit "do not use these" warning.

Usage:
    uv run python scripts/check_no_pip.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Files we scan: student-facing prose and notebooks. We skip this script and the env lockfiles.
SCAN_GLOBS = [
    "README.md",
    "NOTICE.md",
    "**/*.ipynb",
    "assignments/**/*.md",
    "dashboards/**/*.md",
    "data/README.md",
    "docs/**/*.md",
    "project_template/**/*.md",
    "schedule/**/*.md",
]
SKIP_DIRS = {".git", ".venv", "__pycache__", ".ipynb_checkpoints"}

# Patterns that indicate forbidden tooling.
PATTERNS = [
    re.compile(r"%pip\b"),
    re.compile(r"!pip\b"),
    re.compile(r"\bpip install\b"),
    re.compile(r"\bpipenv\b"),
    re.compile(r"\bPipfile\b"),
    re.compile(r"\bconda (install|create|env)\b"),
]

# A line is allowed if it is clearly telling the reader NOT to use these tools.
ALLOW = re.compile(
    r"do not|don't|never|avoid|instead of|rather than|not use|"
    r"no [\w-]*install|forbidden|not allowed|the only exception",
    re.I,
)

# Markdown emphasis / code formatting we strip before testing, so `**not**` still reads as "not".
MARKDOWN = re.compile(r"[*_`]")


def _iter_lines(path: Path):
    if path.suffix == ".ipynb":
        nb = json.loads(path.read_text(encoding="utf-8"))
        for cell in nb.get("cells", []):
            yield from "".join(cell.get("source", [])).splitlines()
    else:
        yield from path.read_text(encoding="utf-8").splitlines()


def main() -> int:
    violations: list[str] = []
    seen: set[Path] = set()
    for pattern in SCAN_GLOBS:
        for path in ROOT.glob(pattern):
            if path in seen or any(part in SKIP_DIRS for part in path.parts):
                continue
            seen.add(path)
            for lineno, line in enumerate(_iter_lines(path), start=1):
                plain = MARKDOWN.sub("", line)
                if ALLOW.search(plain):
                    continue
                if any(p.search(plain) for p in PATTERNS):
                    rel = path.relative_to(ROOT)
                    violations.append(f"{rel}:{lineno}: {line.strip()}")

    if violations:
        print("Forbidden package-management instructions found:")
        for v in violations:
            print(f"  {v}")
        print("\nThe course environment uses `uv` only. Remove the lines above.")
        return 1
    print(f"check_no_pip: OK ({len(seen)} files scanned, no pip/conda/pipenv instructions).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
