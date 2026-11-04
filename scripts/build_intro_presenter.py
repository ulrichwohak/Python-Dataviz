"""Instructor-only projection and presenter PDFs from reviewed native slide renders.

Usage: python scripts/build_intro_presenter.py /path/to/introduction-build-directory
Requires the notes.json and preview/ files produced by build_introduction.mjs.
"""

import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas as pdf_canvas
from reportlab.platypus import Image, PageBreak, Paragraph, SimpleDocTemplate, Spacer


def main() -> None:
    build = Path(sys.argv[1])
    notes = json.loads((build / "notes.json").read_text())
    output = build / "output/course-introduction-presenter.pdf"
    # LibreOffice changes the native scatter charts in this deck. Preserve the checked
    # appearance in the projection PDF. The PPTX is editable; this PDF is raster-based.
    projection_path = build / "output/course-introduction.pdf"
    native_projection = "--native-projection" in sys.argv[2:]
    if native_projection and not projection_path.exists():
        raise FileNotFoundError(projection_path)
    projection = None if native_projection else pdf_canvas.Canvas(str(projection_path), pagesize=(960, 540))
    if projection:
        write_projection(projection, build, notes)

    write_presenter(build, notes, output)
    print(projection_path)
    print(output)


def write_projection(projection, build, notes):
    projection.setTitle("Data Visualization and Storytelling — Course Introduction")
    projection.setAuthor("Ulrich Wohak")
    for i in range(len(notes)):
        projection.drawImage(str(build / f"preview/slide-{i + 1:02d}.png"),
                             0, 0, width=960, height=540)
        for link in notes[i].get("links", []):
            x, y, w, h = link["rect"]
            projection.linkURL(link["url"],
                               (x * 0.75, (720 - y - h) * 0.75,
                                (x + w) * 0.75, (720 - y) * 0.75),
                               relative=0, thickness=0)
        projection.showPage()
    projection.save()


def write_presenter(build, notes, output):
    width = A4[0] - 84
    styles = {
        "title": ParagraphStyle("Title", fontName="Helvetica-Bold", fontSize=14,
                                leading=17, textColor=colors.HexColor("#172D43")),
        "body": ParagraphStyle("Body", fontName="Helvetica", fontSize=10, leading=14,
                               spaceAfter=10),
        "source": ParagraphStyle("Source", fontName="Helvetica", fontSize=8, leading=11,
                                 textColor=colors.HexColor("#536270")),
    }
    # Replace only unsupported mathematical glyphs in the *notes*. The slide itself
    # retains the exact typeset notation. Do not change the mathematics or labels.
    substitutions = {"β": "beta", "ᵀ": "^T", "−": "-", "₀": "0", "₁": "1",
                     "̂": "-hat", "∑": "sum", "⁻": "-", "¹": "1"}

    def paragraph(value: str, style: str) -> Paragraph:
        for original, replacement in substitutions.items():
            value = value.replace(original, replacement)
        return Paragraph(escape(value).replace("\n", "<br/>"), styles[style])

    story = []
    for i, note in enumerate(notes):
        if i:
            story.append(PageBreak())
        story.extend([
            paragraph(f"{note['number']}. {note['title']}", "title"),
            Spacer(1, 10),
            Image(str(build / f"preview/slide-{i + 1:02d}.png"), width=width,
                  height=width * 720 / 1280),
            Spacer(1, 14),
            paragraph(note["text"], "body"),
            paragraph(note["source"], "source"),
        ])
        for link in note.get("links", []):
            story.append(Paragraph(
                f'<link href="{escape(link["url"])}" color="#176B73">'
                f'{escape(link["label"])}</link>', styles["body"]))

    def footer(canvas, doc):
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#536270"))
        canvas.drawString(42, 25, "ECBS5209 | Instructor notes | Local teaching copy")
        canvas.drawRightString(A4[0] - 42, 25, str(doc.page))

    document = SimpleDocTemplate(str(output), pagesize=A4, leftMargin=42, rightMargin=42,
                                 topMargin=36, bottomMargin=42,
                                 title="Data Visualization and Storytelling — Presenter Notes",
                                 author="Ulrich Wohak")
    document.build(story, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    main()
