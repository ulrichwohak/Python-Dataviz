"""Build the local introduction with XeLaTeX, then render and make presenter notes.

Run with the bundled document Python runtime. Supply a fresh build directory.
Teaching data must already exist (scripts/fetch_data.py). No network access is used.
"""

import argparse
import csv
import json
import math
import random
import shutil
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "presentations/session01"
CRITIQUE_IMAGES = (
    "prices-and-wages.png", "florida-firearm-murders.png",
    "pool-and-skyscrapers.png", "county-suicide-rates.png",
)


def fit_line(xs, ys):
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys, strict=True)) / sum(
        (x - mx) ** 2 for x in xs)
    return my - slope * mx, slope


def coordinates(xs, ys):
    return " ".join(f"({x:.8f},{y:.8f})" for x, y in zip(xs, ys, strict=True))


def ols_example():
    """Reproducible synthetic observations, with visible variation around the trend."""
    rng = random.Random(42)
    xs = sorted(rng.gauss(1, 2.3) for _ in range(100))
    ys = [0.5 + 0.55 * x + rng.gauss(0, 1) for x in xs]
    return xs, ys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("build", type=Path)
    parser.add_argument("--xelatex", default="/Library/TeX/texbin/xelatex")
    args = parser.parse_args()
    build = args.build.resolve()
    build.mkdir(parents=True, exist_ok=True)
    output = build / "output"
    output.mkdir(exist_ok=True)
    if (output / "course-introduction.pdf").exists():
        raise FileExistsError("Use a fresh build directory.")
    for filename in ["cairo-figure3-full.png", "cairo-figure3-chart.png"]:
        shutil.copy2(ROOT / "textbook/extracts" / filename, build / filename)
    for filename in CRITIQUE_IMAGES:
        shutil.copy2(SOURCE / "local-critique-images" / filename, build / filename)
    shutil.copy2(SOURCE / "course-introduction.tex", build / "course-introduction.tex")
    notes = json.loads((SOURCE / "course-introduction-notes.json").read_text())
    assert len(notes) == 24
    assert [note["number"] for note in notes] == list(range(1, len(notes) + 1))
    (build / "notes.json").write_text(json.dumps(notes, ensure_ascii=False, indent=2))

    xs, ys = ols_example()
    fitted = fit_line(xs, ys)
    residuals = [y - fitted[0] - fitted[1] * x for x, y in zip(xs, ys, strict=True)]
    # The fitted residuals must be orthogonal to the intercept and x column.
    assert math.isclose(sum(residuals), 0, abs_tol=1e-10)
    assert math.isclose(sum(x * r for x, r in zip(xs, residuals, strict=True)), 0, abs_tol=1e-10)
    assert all(-6 < x < 7 for x in xs) and all(-4 < y < 7 for y in ys)
    for name in ["scatter", "fitted"]:
        chart = [r"\begin{tikzpicture}\begin{axis}[width=.9\textwidth,height=52mm,",
                 r"xmin=-6,xmax=7,ymin=-4,ymax=7,xtick={-6,-4,-2,0,2,4,6},ytick={-4,-2,0,2,4,6},",
                 r"xlabel={Independent variable ($x$)},ylabel={Dependent variable ($y$)},",
                 r"tick label style={font=\scriptsize},label style={font=\scriptsize},",
                 r"axis line style={muted!60},grid=major,grid style={muted!18},",
                 r"legend pos=north west,legend style={font=\scriptsize,draw=none,fill=white}]"]
        chart.append(r"\addplot[only marks,mark=*,blue,mark size=1.5pt,opacity=.85] coordinates {"
                     + coordinates(xs, ys) + "};")
        chart.append(r"\addlegendentry{Synthetic observations}")
        if name == "fitted":
            ends = [min(xs), max(xs)]
            chart.append(r"\addplot[orange,line width=1.1pt] coordinates {"
                         + coordinates(ends, [fitted[0] + fitted[1] * x for x in ends]) + "};")
            chart.append(r"\addlegendentry{OLS fitted line}")
        chart.append(r"\end{axis}\end{tikzpicture}")
        (build / f"ols-{name}.tex").write_text("\n".join(chart))

    with (ROOT / "data/raw/simpson_hotels.csv").open() as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 24
    hx = [float(r["distance_km"]) for r in rows]
    hy = [float(r["price_eur"]) for r in rows]
    pooled = fit_line(hx, hy)
    assert pooled[1] > 0
    for grouped in [False, True]:
        chart = [r"\begin{tikzpicture}\begin{axis}[width=\linewidth,height=54mm,",
                 r"xmin=0,xmax=12,ymin=0,ymax=220,xtick={0,3,6,9,12},ytick={0,50,100,150,200},",
                 r"xlabel={Distance from city centre (km)},ylabel={Price per night (€)},",
                 r"tick label style={font=\scriptsize},label style={font=\scriptsize},",
                 r"axis line style={muted!50}]"]
        colour = "muted!50" if grouped else "ink"
        chart.append(rf"\addplot[{colour},thick] coordinates {{"
                     + coordinates([1, 11], [pooled[0] + pooled[1]*x for x in [1, 11]]) + "};")
        if grouped:
            for country, colour, mark in [("A", "accent", "*"), ("B", "orange", "square*"),
                                          ("C", "blue", "triangle*")]:
                group = [r for r in rows if r["country"] == country]
                gx = [float(r["distance_km"]) for r in group]
                gy = [float(r["price_eur"]) for r in group]
                beta = fit_line(gx, gy)
                assert len(group) == 8 and math.isclose(beta[1], -8)
                ends = [min(gx), max(gx)]
                chart.append(rf"\addplot[{colour},thick] coordinates {{"
                             + coordinates(ends, [beta[0]+beta[1]*x for x in ends]) + "};")
                chart.append(rf"\addplot[only marks,{colour},mark={mark},mark size=2pt] coordinates {{"
                             + coordinates(gx, gy) + "};")
        else:
            chart.append(r"\addplot[only marks,ink,mark=*,mark size=2pt] coordinates {"
                         + coordinates(hx, hy) + "};")
        chart.append(r"\end{axis}\end{tikzpicture}")
        (build / f"simpson-{'grouped' if grouped else 'pooled'}.tex").write_text("\n".join(chart))

    for _ in range(2):
        result = subprocess.run([args.xelatex, "-no-shell-escape", "-halt-on-error",
                                 "-interaction=nonstopmode", "course-introduction.tex"],
                                cwd=build, capture_output=True, text=True)
        if result.returncode:
            print(result.stdout[-7000:])
            raise RuntimeError("XeLaTeX failed; see the build log.")
    log = (build / "course-introduction.log").read_text()
    if "Overfull" in log or "Missing character" in log:
        raise RuntimeError("Inspect LaTeX layout/font warnings before delivery.")
    shutil.copy2(build / "course-introduction.pdf", output / "course-introduction.pdf")
    preview = build / "preview"
    preview.mkdir(exist_ok=True)
    assert len(PdfReader(output / "course-introduction.pdf").pages) == len(notes)
    subprocess.run(["/opt/homebrew/bin/pdftoppm", "-scale-to", "1600", "-png",
                    str(output / "course-introduction.pdf"), str(preview / "slide")], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/build_intro_presenter.py"),
                    str(build), "--native-projection"], check=True)
    print(f"Built {len(notes)} LaTeX slides and presenter notes in {output}")


if __name__ == "__main__":
    main()
