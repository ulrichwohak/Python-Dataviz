"""Prevent instructor-only files from entering the published course tree.

Checks the Git index, not local ignored files. Run before committing and in CI.
"""

import subprocess
from pathlib import PurePosixPath

PRIVATE_FILES = {
    "CLAUDE.md", "AGENTS.md", ".secrets.md", "course repo.md",
    "docs/live_coding_notes.md", "docs/redesign-activities.md",
    "scripts/build_intro_presenter.py", "scripts/build_introduction.mjs",
    "scripts/build_introduction_pdf.py", "scripts/check_intro_sync.py",
    "scripts/build_notebooks.py", "scripts/lecture_content.py",
    "scripts/real_data_content.py", "scripts/chart_tour.py", "scripts/redesign_activities.py",
}
PUBLIC_SLIDES = {
    "presentations/session01/README.md",
    "presentations/session01/course-introduction.pdf",
}


def private_path(name: str) -> bool:
    parts = PurePosixPath(name).parts
    return (
        name in PRIVATE_FILES
        or name.startswith(("instructor/", "textbook/", "scripts/notebook_sources/"))
        or (name.startswith("presentations/") and name not in PUBLIC_SLIDES)
        or any(part.lower() in {"solutions", "grading", "instructor"} for part in parts)
        or "presenter" in PurePosixPath(name).name.lower()
    )


def main() -> int:
    tracked = subprocess.check_output(["git", "ls-files", "-z"], text=True).split("\0")
    forbidden = sorted(name for name in tracked if name and private_path(name))
    if forbidden:
        print("Instructor-only files must not be published:")
        print("\n".join(forbidden))
        return 1
    print("check_student_files: OK (no instructor-only paths tracked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
