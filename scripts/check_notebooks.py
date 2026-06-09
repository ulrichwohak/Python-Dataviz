"""Validate the course notebooks.

For every notebook under notebooks/ this checks:
  1. valid notebook JSON (parses with nbformat),
  2. the kernelspec is `python3` / "Python 3 (ipykernel)",
  3. no package-install cells (`%pip`, `!pip`, `conda install`),
  4. no live remote data reads (`read_csv("http...")`, `read_file("http...")`),
  5. code cells are syntactically valid Python (magics/shell lines stripped first),
  6. outputs are cleared (keeps diffs small and avoids committing large outputs).

Usage:
    uv run python scripts/check_notebooks.py
"""

from __future__ import annotations

import re
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK_DIR = ROOT / "notebooks"

INSTALL = re.compile(r"(%pip|!pip|\bpip install\b|conda (install|create|env))")
REMOTE_READ = re.compile(r"read_(csv|file|json|excel|parquet)\(\s*[\"']https?://")
MAGIC_OR_SHELL = re.compile(r"^\s*[%!]")


def _strip_magics(source: str) -> str:
    """Remove IPython line magics / shell lines so the cell can be compiled as plain Python."""
    lines = source.splitlines()
    if lines and lines[0].lstrip().startswith("%%"):
        return ""  # whole-cell magic; not Python, skip syntax check
    return "\n".join("" if MAGIC_OR_SHELL.match(ln) else ln for ln in lines)


def check_notebook(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        nb = nbformat.read(path, as_version=4)
    except Exception as exc:  # noqa: BLE001 - report any parse failure as an error
        return [f"invalid notebook JSON: {exc}"]

    kernel = nb.metadata.get("kernelspec", {}).get("name", "")
    if kernel != "python3":
        errors.append(f"kernelspec name is {kernel!r}, expected 'python3'")

    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue
        source = cell.source
        if INSTALL.search(source):
            errors.append(f"cell {i}: package-install command not allowed")
        if REMOTE_READ.search(source):
            errors.append(f"cell {i}: remote data read; use local data/ paths")
        if cell.get("outputs"):
            errors.append(f"cell {i}: outputs not cleared")
        if cell.get("execution_count") is not None:
            errors.append(f"cell {i}: execution_count not cleared")
        code = _strip_magics(source)
        try:
            compile(code, f"{path.name}:cell{i}", "exec")
        except SyntaxError as exc:
            errors.append(f"cell {i}: syntax error: {exc.msg} (line {exc.lineno})")
    return errors


def main() -> int:
    notebooks = sorted(NOTEBOOK_DIR.rglob("*.ipynb"))
    if not notebooks:
        print("check_notebooks: no notebooks found (run scripts/build_notebooks.py).")
        return 1

    failed = False
    for path in notebooks:
        errors = check_notebook(path)
        rel = path.relative_to(ROOT)
        if errors:
            failed = True
            print(f"FAIL {rel}")
            for e in errors:
                print(f"     - {e}")
        else:
            print(f"OK   {rel}")

    print(f"\n{len(notebooks)} notebooks checked.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
