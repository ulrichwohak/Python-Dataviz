"""Build one teaching notebook and one exercise notebook for each scheduled lecture.

Edit real_data_content.py and lecture_content.py; then run this script.
Old variants are not recreated. Optional reference notebooks are outside the numbered sequence.
"""

import hashlib
from pathlib import Path

import nbformat
from lecture_content import (
    power_bi_comparisons,
    power_bi_dashboard,
    power_bi_exercises,
    power_bi_foundations,
)
from real_data_content import (
    chart_basics,
    chart_tour,
    comparison_exercises,
    comparisons,
    data_intro,
    first_exercise,
    mapping,
    mapping_exercises,
    notes_and_export,
    references,
)

ROOT = Path(__file__).resolve().parents[1]
SESSIONS = [
    ("01-python-chart-tour", "Python chart tour", "4 November 2026"),
    ("02-comparisons-and-uncertainty", "Comparisons and uncertainty", "11 November 2026"),
    ("03-mapping-in-python", "Mapping in Python", "18 November 2026"),
    ("04-power-bi-foundations", "Power BI foundations", "25 November 2026"),
    ("05-power-bi-comparisons-and-filtering", "Power BI comparisons and filtering", "2 December 2026"),
    ("06-power-bi-dashboard-building", "Power BI dashboard building", "9 December 2026"),
]
REFERENCES = ("design-and-annotation", "python-interactivity", "project-workshop")
LECTURE_DATA = [
    ("births",),
    ("amazon", "event_study_results"),
    ("countries", "co2"),
    ("dashboard",),
    ("dashboard",),
    ("dashboard",),
]
EXERCISE_DATA = [
    ("births",),
    ("amazon", "event_study_results"),
    ("countries", "co2"),
    ("dashboard",),
    ("dashboard",),
    ("dashboard",),
]
REFERENCE_DATA = {
    "design-and-annotation": ("births",),
    "python-interactivity": ("dashboard",),
    "project-workshop": ("amazon",),
}
FOOTER = {
    "cell_type": "markdown",
    "source": "Course AI use and disclosure requirements are in [the policy](../../docs/ai_policy.md). "
              "If you use assistance, verify the code, numbers and interpretation and disclose it as required.",
}


def notebook(cells, datasets):
    nb = nbformat.v4.new_notebook()
    nb.metadata = {
        "kernelspec": {"display_name": "Python 3 (ipykernel)", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.12"},
    }
    for i, cell in enumerate(cells):
        source = cell["source"]
        if i == 0:
            assert cell["cell_type"] == "markdown", "Start each notebook with Markdown."
            source += "\n\n" + data_intro(datasets)
        key = hashlib.sha256(f"{i}:{cell['cell_type']}:{source}".encode()).hexdigest()[:12]
        factory = nbformat.v4.new_code_cell if cell["cell_type"] == "code" else nbformat.v4.new_markdown_cell
        nb.cells.append(factory(source, id=key))
    nbformat.validate(nb)
    return nb


def main():
    lectures = [
        chart_basics() + chart_tour() + notes_and_export(),
        comparisons(), mapping(), power_bi_foundations(),
        power_bi_comparisons(), power_bi_dashboard(),
    ]
    exercises = [
        first_exercise(),
        comparison_exercises(), mapping_exercises(),
        power_bi_exercises(4), power_bi_exercises(5), power_bi_exercises(6),
    ]
    for i, (folder, title, date) in enumerate(SESSIONS):
        destination = ROOT / "notebooks" / folder
        destination.mkdir(parents=True, exist_ok=True)
        for name, body, datasets in [
            ("lecture", lectures[i], LECTURE_DATA[i]),
            ("exercises", exercises[i], EXERCISE_DATA[i]),
        ]:
            if i == 0 and name == "exercises":
                cells = body + [FOOTER]
            else:
                heading = title if name == "lecture" else f"{title} — Exercises"
                setup = ("Run Python cells from the repository root. Prepare local data with "
                         "`uv run python scripts/fetch_data.py`. Paths are relative to that root."
                         if i < 3 else "Follow the steps in Power BI Desktop. This notebook is a workshop guide.")
                cells = [{"cell_type": "markdown",
                          "source": f"# {heading}\n\n{date} · Lecture {i + 1}\n\n{setup}"}]
                cells += body + [FOOTER]
            nbformat.write(notebook(cells, datasets), destination / f"{name}.ipynb")
    reference_dir = ROOT / "notebooks/reference"
    reference_dir.mkdir(exist_ok=True)
    for slug in REFERENCES:
        nbformat.write(notebook(references(slug) + [FOOTER], REFERENCE_DATA[slug]), reference_dir / f"{slug}.ipynb")
    index = ["# Lecture notebooks", "", "Each numbered folder matches one scheduled lecture.",
             "Open `lecture.ipynb` for the fully written examples or Power BI steps, and",
             "`exercises.ipynb` for ungraded practice. There are no separate live/reference variants.", "",
             "| Date | Lecture | Teaching notebook | Exercises |", "| --- | --- | --- | --- |"]
    for folder, title, date in SESSIONS:
        index.append(f"| {date} | {title} | [Open]({folder}/lecture.ipynb) | [Open]({folder}/exercises.ipynb) |")
    index += ["", "Python notebooks run from the repository root; Power BI notebooks guide work in Desktop.",
              "The first lecture ends with the 2014 monthly-births pie-chart redesign exercise.", "",
              "## Optional references", "", "These are not additional scheduled lectures."]
    for slug in REFERENCES:
        index.append(f"- [{slug.replace('-', ' ').capitalize()}](reference/{slug}.ipynb)")
    (ROOT / "notebooks/README.md").write_text("\n".join(index) + "\n")
    print("Wrote 12 scheduled notebooks and 3 optional references.")


if __name__ == "__main__":
    main()
