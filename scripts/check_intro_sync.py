"""Flag course-input changes since the introductory deck was last reviewed.

Run normally to check. Use --record-reviewed ONLY after revising, exporting and visually
reviewing the deck and its PDFs. Hashes detect staleness, not semantic agreement.
"""

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RECORD = ROOT / "presentations/session01/course-introduction.inputs.json"
SOURCES = [
    "Data-Visualization-and-Storytelling-Syllabus.md",
    "README.md",
    "schedule/session_plan.md",
    "docs/course_outline.md",
    "docs/ai_policy.md",
    "docs/redesign-activities.md",
    "assignments/chart-critique-redesign/README.md",
    "assignments/final-data-story/README.md",
    "workshops/power-bi/README.md",
    "workshops/power-bi/session05-introduction.md",
    "workshops/power-bi/session06-dashboard.md",
    "scripts/build_notebooks.py",
    "scripts/lecture_content.py",
    "scripts/real_data_content.py",
    "scripts/fetch_data.py",
    "data/README.md",
    "notebooks/README.md",
    "presentations/session01/course-introduction.tex",
    "presentations/session01/course-introduction-notes.json",
    "presentations/session01/local-critique-images/prices-and-wages.png",
    "presentations/session01/local-critique-images/florida-firearm-murders.png",
    "presentations/session01/local-critique-images/pool-and-skyscrapers.png",
    "presentations/session01/local-critique-images/county-suicide-rates.png",
    "presentations/session01/ols-opening.mjs",
    "scripts/build_introduction_pdf.py",
    "scripts/build_intro_presenter.py",
]
OUTPUTS = [
    "presentations/session01/course-introduction.pdf",
    "presentations/session01/course-introduction-presenter.pdf",
]


def digest(name: str) -> str:
    return hashlib.sha256((ROOT / name).read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record-reviewed", action="store_true")
    args = parser.parse_args()
    missing = [name for name in SOURCES + OUTPUTS if not (ROOT / name).is_file()]
    if missing:
        print("Missing introduction inputs/exports (local instructor build required):")
        print("\n".join(missing))
        return 1
    current = {name: digest(name) for name in SOURCES + OUTPUTS}
    if args.record_reviewed:
        RECORD.write_text(json.dumps(current, indent=2) + "\n")
        print("Recorded reviewed inputs and exports. This is not a content audit.")
        return 0
    if not RECORD.exists():
        print("No reviewed introduction snapshot. Rebuild, review, then record it.")
        return 1
    previous = json.loads(RECORD.read_text())
    changed = sorted(name for name in set(current) | set(previous)
                     if current.get(name) != previous.get(name))
    if changed:
        print("Introduction needs review after changes to:")
        print("\n".join(changed))
        return 1
    print("Introduction inputs and exports match the last reviewed snapshot.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
