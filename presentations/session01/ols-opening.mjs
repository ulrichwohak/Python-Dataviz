// Instructor authoring source for the opening slides.
// The caller supplies @oai/artifact-tool's Presentation and chart-font helper.
// Students need only the exported PPTX, not a JavaScript environment.
export const example = {
  x: [1, 4, 7, 10, 13],
  y: [0.9, 2.8, 2.7, 4.6, 4.5],
  candidate: [0.5, 0.2],
};

export const openingQuote = {
  lead: '“The purpose of visualization is',
  conclusion: 'insight, not pictures.”',
  attribution: 'Ben Shneiderman',
  source: 'Quoted in Alberto Cairo, The Functional Art, p. xx',
  notes: 'Data Visualization and Storytelling, Ulrich Wohak. Read the quotation as the first words of Session 1, then pause. Ask what students would need to understand for a chart to have helped them. Introduce the course through that question and move to the OLS example. The equation and visual reveal illustrate how a picture can make an abstract objective understandable. Later, return to the idea when discussing competing messages and uncertainty: a clear insight must remain supported by the evidence.\n\nQuotation and attribution: Alberto Cairo, The Functional Art, introduction, printed p. xx (local PDF page 21), attributes these exact words to Ben Shneiderman. Footnote 3 cites Stuart K. Card, Jock D. Mackinlay and Ben Shneiderman, Readings in Information Visualization: Using Vision to Think (1999). Shneiderman’s own bibliography lists Morgan Kaufmann, San Francisco, as the publisher: https://www.cs.umd.edu/~ben/books.html . Cairo’s footnote instead gives Academic Press, London. Use the author’s bibliographic record for the full reference. The quotation is verified in Cairo; an original page number in the 1999 volume has not been established.',
};

export function fitLine(x, y) {
  const mean = values => values.reduce((a, b) => a + b, 0) / values.length;
  const mx = mean(x), my = mean(y);
  const slope = x.reduce((sum, value, i) => sum + (value - mx) * (y[i] - my), 0)
    / x.reduce((sum, value) => sum + (value - mx) ** 2, 0);
  return [my - slope * mx, slope];
}

export function residuals(beta) {
  return example.y.map((value, i) => value - beta[0] - beta[1] * example.x[i]);
}

export function sse(beta) {
  return residuals(beta).reduce((sum, value) => sum + value ** 2, 0);
}

export function buildOpening(Presentation, applyPresentationChartFont) {
  const p = Presentation.create({ slideSize: { width: 1280, height: 720 } });
  const C = { ink: '#182C39', muted: '#546670', paper: '#FAF8F4', teal: '#087F82',
    orange: '#B54C22', pale: '#F6D4C3', axis: '#9CA6A9' };
  const bodyFont = 'Arial';
  const mathFont = 'STIX Two Math';
  p.theme.defaultFont = bodyFont;
  const best = fitLine(example.x, example.y);
  const nist = 'https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd431.htm';
  const matrixSource = 'https://stat151a.berkeley.edu/fall-2024/lectures/Lecture4.html';
  const sourceNote = `Five deliberately constructed synthetic points, not observed data. x = ${example.x}; y = ${example.y}. OLS objective: ${nist}`;

  function text(s, name, value, x, y, w, h, size = 28, color = C.ink, extra = {}) {
    const shape = s.shapes.add({ geometry: 'textbox', name,
      position: { left: x, top: y, width: w, height: h }, fill: 'none',
      line: { fill: 'none', width: 0 } });
    shape.text = value;
    shape.text.style = { typeface: bodyFont, fontSize: size, color, insets: 0,
      verticalAlignment: 'middle', autoFit: 'none', ...extra };
    return shape;
  }
  const math = (s, name, value, x, y, w, h, size = 42, color = C.ink) =>
    text(s, name, value, x, y, w, h, size, color, { typeface: mathFont });
  function slide(title, notes) {
    const s = p.slides.add();
    s.background.fill = C.paper;
    if (title) text(s, 'title', title, 72, 44, 1136, 70, 43, C.ink, { bold: true });
    s.speakerNotes.text = notes;
    return s;
  }
  function scalarObjective(s, top) {
    math(s, 'estimated-intercept-and-slope', '(β̂₀, β̂₁) =', 112, top, 230, 80, 48);
    math(s, 'argmin', 'arg min', 355, top, 180, 80, 47);
    math(s, 'minimise-over', 'β₀, β₁', 395, top + 62, 110, 38, 27);
    math(s, 'sum', '∑', 554, top - 8, 66, 100, 75);
    math(s, 'sum-upper-limit', 'n', 575, top - 26, 35, 30, 24);
    math(s, 'sum-lower-limit', 'i = 1', 557, top + 99, 75, 32, 24);
    math(s, 'squared-residual', '[yᵢ − (β₀ + β₁xᵢ)]²', 642, top, 525, 80, 48);
  }
  function chart(s, beta, showResiduals, w = 690) {
    // Remove floating-point tail digits from the editable chart's workbook.
    // The constructed example has exact predictions at this precision.
    const prediction = x => Number((beta[0] + beta[1] * x).toFixed(10));
    const series = [];
    if (showResiduals) example.x.forEach((x, i) => {
      series.push({ name: `Residual ${i + 1}`, xValues: [x, x],
        values: [prediction(x), example.y[i]],
        line: { fill: C.orange, width: 3 }, marker: { symbol: 'none' } });
    });
    series.push({ name: 'Line', xValues: [0, 15],
      values: [prediction(0), prediction(15)],
      line: { fill: C.teal, width: 3 }, marker: { symbol: 'none' } });
    series.push({ name: 'Observations', xValues: example.x, values: example.y,
      line: { fill: 'none', width: 0 }, marker: { symbol: 'circle', size: 9, fill: C.ink },
      dataLabelOverrides: example.x.map((_, i) => ({ idx: i, text: String(i + 1),
        position: example.y[i] < prediction(example.x[i]) ? 'bottom' : 'top',
        showValue: false, textStyle: { fontSize: 18, fill: C.ink } })) });
    const chart = s.charts.add('scatter', {
      name: 'Five synthetic observations and candidate line',
      position: { left: 65, top: 164, width: w, height: 438 },
      series, scatterOptions: { style: 'lineWithMarkers' }, hasLegend: false,
      chartFill: C.paper, plotAreaFill: C.paper,
      xAxis: { title: 'x', min: 0, max: 15, majorUnit: 3, numberFormatCode: '0',
        textStyle: { fontSize: 19, fill: C.muted }, line: { fill: C.axis, width: 1 }, majorGridlines: null },
      yAxis: { title: 'y', min: 0, max: 6, majorUnit: 2, numberFormatCode: '0',
        textStyle: { fontSize: 19, fill: C.muted }, line: { fill: C.axis, width: 1 }, majorGridlines: null },
    });
    applyPresentationChartFont(chart, { fontFamily: bodyFont });
    text(s, 'data-disclosure', 'Five synthetic observations', 88, 636, 500, 28, 19, C.muted);
  }
  function squares(s, beta) {
    // Mathematical area diagram. One shared scale (45 px per residual unit)
    // and fixed observation positions on both slides make area comparable.
    const scale = 45;
    const centers = [795, 880, 965, 1060, 1160];
    const gaps = residuals(beta);
    text(s, 'square-diagram-heading', 'One square for each vertical gap', 770, 175, 438, 68, 27);
    gaps.forEach((gap, i) => {
      const side = Math.abs(gap) * scale;
      s.shapes.add({ geometry: 'rect', name: `Residual ${i + 1} squared`,
        position: { left: centers[i] - side / 2, top: 395 - side, width: side, height: side },
        fill: C.pale, line: { fill: C.orange, width: 1.5 } });
      text(s, `observation-number-${i + 1}`, String(i + 1), centers[i] - 25, 405, 50, 28, 21, C.ink,
        { alignment: 'center' });
      text(s, `square-area-${i + 1}`, (gap * gap).toFixed(2), centers[i] - 35, 447, 70, 30, 21, C.orange,
        { alignment: 'center' });
    });
    text(s, 'square-area-label', 'Areas', 770, 492, 100, 35, 22, C.muted);
    text(s, 'total-square-area', `Total area = ${sse(beta).toFixed(2)}`, 770, 545, 440, 58, 36, C.orange,
      { bold: true });
    text(s, 'shared-area-scale', 'Same square-size scale on both slides', 770, 636, 450, 28, 19, C.muted);
  }
  function bracket(s, name, x, y, w, h) {
    for (const [side, xx, sign] of [['left', x, 1], ['right', x + w, -1]]) {
      s.shapes.add({ geometry: 'custom', name: `${name}-${side}`,
        position: { left: Math.min(xx, xx + sign * 12), top: y, width: 12, height: h },
        fill: 'none', line: { fill: C.ink, width: 2 },
        customPaths: [{ width: 12, height: h, commands: side === 'left'
          ? [{ moveTo: { x: 12, y: 0 } }, { lineTo: { x: 0, y: 0 } }, { lineTo: { x: 0, y: h } }, { lineTo: { x: 12, y: h } }]
          : [{ moveTo: { x: 0, y: 0 } }, { lineTo: { x: 12, y: 0 } }, { lineTo: { x: 12, y: h } }, { lineTo: { x: 0, y: h } }] }] });
    }
  }

  {
    const s = slide('', openingQuote.notes);
    text(s, 'course', openingQuote.lead, 96, 210, 1090, 80, 52);
    text(s, 'cover-title', openingQuote.conclusion, 96, 300, 1090, 110, 72, C.teal, { bold: true });
    text(s, 'cover-subtitle', openingQuote.attribution, 96, 475, 1090, 45, 29);
    text(s, 'instructor', openingQuote.source, 96, 529, 1090, 40, 23, C.muted);
  }
  {
    const s = slide('The least-squares objective', `Ask: What are we trying to make small? Do not ask students to calculate or derive anything. The two expressions are equivalent when X contains a column of ones and the x values. Define the symbols after the visual reveal. Sources: ${nist}; ${matrixSource}`);
    scalarObjective(s, 220);
    math(s, 'matrix-objective', 'β̂ = arg min (y − Xβ)ᵀ(y − Xβ)', 250, 413, 930, 90, 46);
    math(s, 'matrix-minimiser', 'β', 410, 480, 45, 38, 27);
    text(s, 'opening-question', 'What are we trying to make small?', 112, 610, 1050, 48, 31, C.teal);
  }
  {
    const s = slide('Five observations and a candidate line', `${sourceNote}\nCandidate intercept 0.5, slope 0.2. The observations stay fixed in the next slides. Ask students which points this line predicts poorly.`);
    chart(s, example.candidate, false);
    math(s, 'candidate-equation', 'Predicted y = 0.5 + 0.2x', 790, 235, 420, 95, 34, C.teal);
    text(s, 'fit-question', 'How well does this line fit?', 790, 394, 415, 112, 34);
  }
  {
    const s = slide('The vertical gaps are the residuals', `${sourceNote}\nEach gap compares an observed and predicted y at the same x. These are vertical distances, not perpendicular distances to the plotted line. Residuals can have either sign.`);
    chart(s, example.candidate, true);
    math(s, 'residual-equation', 'eᵢ = yᵢ − (β₀ + β₁xᵢ)', 785, 247, 430, 85, 36, C.orange);
    text(s, 'residual-explanation', 'Observed y minus predicted y,\nat the same x.', 785, 380, 430, 112, 30);
  }
  {
    const s = slide('Squaring gives each gap an area', `${sourceNote}\nThe squares form a separate area diagram. Each side is proportional to the absolute residual, so each area is proportional to its square. Observation labels connect the plots. All squares use the same scale, also retained on the next slide. Candidate residuals: ${residuals(example.candidate)}. SSE = ${sse(example.candidate).toFixed(2)}. The gaps, not horizontal widths on the x axis, determine square sides.`);
    chart(s, example.candidate, true);
    squares(s, example.candidate);
  }
  {
    const s = slide('The least-squares line minimises the total area', `${sourceNote}\nOLS coefficients = ${best}. SSE = ${sse(best).toFixed(2)}, compared with 9.30 for the candidate. The data, axes, square positions and area scale stay fixed. Some individual residuals may increase. OLS minimises the sum, not every residual separately. Comparison alone illustrates rather than proves global optimality; the matrix solution supplies the computed minimiser.`);
    chart(s, best, true);
    squares(s, best);
    math(s, 'best-equation', 'ŷ = 1 + 0.3x', 335, 125, 400, 45, 30, C.teal);
  }
  {
    const s = slide('The equation now describes the picture', `Return to the opening notation. Read it as: change the intercept and slope, calculate every vertical residual, square it, add the squared values, and choose the smallest total. The equation gives precision; the visualisation gives intuition. Source: ${nist}`);
    scalarObjective(s, 215);
    text(s, 'choose-label', 'Choose the\nintercept and slope', 115, 423, 300, 100, 28);
    text(s, 'sum-label', 'Add the\nsquared gaps', 490, 423, 250, 100, 28);
    text(s, 'gap-label', 'Each observation’s\nvertical gap, squared', 835, 423, 365, 100, 28, C.orange);
    text(s, 'meaning', 'The best line has the smallest total squared gap.', 115, 604, 1080, 48, 31, C.teal);
  }
  {
    const s = slide('Matrix notation stacks the same observations', `${sourceNote}\nX is 5 by 2, with a column of ones for the intercept and a column of x values. y and e are 5 by 1. β is 2 by 1. Xβ contains the five predictions. eᵀe is a scalar equal to the sum of squared residuals. A superscript T denotes transpose. Source: ${matrixSource}`);
    math(s, 'y-label', 'y =', 100, 260, 90, 65, 42);
    bracket(s, 'y-vector', 207, 190, 110, 254);
    example.y.forEach((v, i) => math(s, `y-${i}`, v.toFixed(1), 231, 192 + i * 48, 65, 48, 35));
    math(s, 'X-label', 'X =', 397, 260, 95, 65, 42);
    bracket(s, 'X-matrix', 507, 190, 180, 254);
    example.x.forEach((v, i) => {
      math(s, `intercept-${i}`, '1', 532, 192 + i * 48, 40, 48, 35);
      math(s, `x-${i}`, String(v), 606, 192 + i * 48, 60, 48, 35);
    });
    math(s, 'beta-label', 'β =', 806, 260, 95, 65, 42);
    bracket(s, 'beta-vector', 917, 240, 115, 112);
    math(s, 'beta-zero', 'β₀', 943, 240, 75, 50, 39);
    math(s, 'beta-one', 'β₁', 943, 293, 75, 50, 39);
    text(s, 'y-dim', 'Observed values\n5 × 1', 100, 468, 250, 80, 25, C.muted);
    text(s, 'X-dim', 'Ones and x values\n5 × 2', 397, 468, 340, 80, 25, C.muted);
    text(s, 'beta-dim', 'Intercept and slope\n2 × 1', 806, 468, 365, 80, 25, C.muted);
    math(s, 'stacked-residuals', 'e = y − Xβ', 105, 588, 420, 65, 43, C.orange);
    math(s, 'dot-product-of-residuals', 'eᵀe = e₁² + e₂² + ⋯ + e₅²', 580, 588, 625, 65, 42, C.orange);
  }
  {
    const s = slide('The matrix solution gives the fitted line', `With full column rank, XᵀX is invertible. The objective expands to yᵀy − 2βᵀXᵀy + βᵀXᵀXβ. Its gradient is −2Xᵀy + 2XᵀXβ. Setting this to zero gives the normal equations, then the closed-form solution. For these five points: XᵀX = [[5,35],[35,335]], Xᵀy = [15.5,135.5], β̂ = [1,0.3]. NumPy least-squares independently verifies these coefficients. No derivation or matrix computation is required of students. The residual vector is orthogonal to the columns of X in observation space; this does NOT make the residual segments perpendicular to the fitted line in the x-y scatterplot. Source: ${matrixSource}`);
    math(s, 'normal-equations', 'XᵀXβ̂ = Xᵀy', 105, 190, 980, 80, 53);
    math(s, 'closed-form', 'β̂ = (XᵀX)⁻¹Xᵀy', 105, 310, 1070, 90, 61, C.teal);
    text(s, 'rank-condition', 'When X has full column rank, so XᵀX is invertible.', 109, 421, 1070, 45, 28, C.muted);
    text(s, 'numeric-coefficients', 'For these points: intercept = 1, slope = 0.3', 109, 528, 1090, 45, 30);
    math(s, 'fitted-line', 'ŷ = 1 + 0.3x', 109, 592, 950, 70, 49, C.teal);
  }
  {
    const s = slide('', 'Alberto Cairo, The Functional Art: An Introduction to Information Graphics and Visualization, first edition, New Riders, copyright 2013, Introduction, “The partnership of presentation and exploration”, printed p. xv (local PDF page 16). The word “because” is italicised in the original. Verified against the local textbook. Publisher: https://www.pearson.com/en-us/subject-catalog/p/functional-art-the-an-introduction-to-information-graphics-and-visualization/P200000008946/9780321834737\nPause after the quotation. Ask: what became easier to understand when we saw the picture? Transition to Session 1’s audience, question and intended-use brief. The equation gives precision; the visualisation gives intuition.');
    const quote = text(s, 'Cairo-quotation', '“We understand\nbecause we see.”', 110, 212, 1080, 220, 75);
    quote.text.get('because').italic = true;
    text(s, 'Cairo-attribution', 'Alberto Cairo, The Functional Art, p. xv', 114, 494, 1080, 48, 28, C.muted);
  }
  return p;
}
