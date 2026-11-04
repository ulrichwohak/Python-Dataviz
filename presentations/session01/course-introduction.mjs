// Historical pre-LaTeX introduction. Active source: course-introduction.tex.
// Local instructor export embeds Cairo's Figure 3. Do not publish that export (NOTICE.md).
import { example, fitLine, residuals, sse, openingQuote } from './ols-opening.mjs';

export function buildIntroduction(Presentation, chartFont, { hotels, weekly, fullFigure, chartDetail }) {
  const p = Presentation.create({ slideSize: { width: 1280, height: 720 } });
  const C = { ink: '#172D43', accent: '#176B73', muted: '#536270', paper: '#FFFFFF',
    orange: '#B54C22', pale: '#F4D4C3', blue: '#4363A8', rule: '#CAD2D8' };
  p.theme.defaultFont = 'Arial';
  const notes = [];
  const policy = 'Course sources: Data-Visualization-and-Storytelling-Syllabus.md; schedule/session_plan.md; assignments/README.md; docs/ai_policy.md. Version: 4 November 2026. Deadlines, room and Power BI access route are not yet confirmed. Do not invent them.';
  function text(s, name, value, x, y, w, h, size = 30, color = C.ink, extra = {}) {
    const t = s.shapes.add({ geometry: 'textbox', name,
      position: { left: x, top: y, width: w, height: h }, fill: 'none', line: { fill: 'none', width: 0 } });
    t.text = value;
    t.text.style = { typeface: 'Arial', fontSize: size, color, insets: 0,
      verticalAlignment: 'middle', autoFit: 'none', ...extra };
    return t;
  }
  function math(s, name, value, x, y, w, h, size = 42, color = C.ink) {
    return text(s, name, value, x, y, w, h, size, color, { typeface: 'STIX Two Math' });
  }
  function slide(title, guidance, source = policy) {
    const s = p.slides.add();
    s.background.fill = C.paper;
    const number = p.slides.items.length;
    if (title) text(s, 'heading', title, 64, 36, 1152, 78, 44, C.ink, { bold: true });
    text(s, 'footer', 'ECBS5209 · Data Visualization and Storytelling · Ulrich Wohak', 64, 678, 1060, 24, 17, C.muted);
    text(s, 'page', String(number), 1155, 678, 60, 24, 17, C.muted, { alignment: 'right' });
    s.speakerNotes.text = `${guidance}\n\n${source}`;
    notes.push({ number, title: title || 'Welcome: insight, not pictures', text: guidance, source });
    return s;
  }
  function lines(s, items, top = 175, gap = 95, size = 32) {
    items.forEach((value, i) => text(s, `point-${i}`, value, 80, top + i * gap, 1110, 72, size));
  }
  function label(s, value, y = 605) {
    text(s, 'takeaway', value, 80, y, 1115, 50, 29, C.accent, { bold: true });
  }
  function scatter(s, name, series, xAxis, yAxis, position) {
    const c = s.charts.add('scatter', { name, position, series,
      scatterOptions: { style: 'lineWithMarkers' }, hasLegend: false,
      chartFill: C.paper, plotAreaFill: C.paper,
      xAxis: { textStyle: { fontSize: 21, fill: C.muted }, line: { fill: C.rule, width: 1 }, majorGridlines: null, ...xAxis },
      yAxis: { textStyle: { fontSize: 21, fill: C.muted }, line: { fill: C.rule, width: 1 }, majorGridlines: null, ...yAxis },
    });
    chartFont(c, { fontFamily: 'Arial' });
  }
  {
    const s = slide('', 'Read the quotation first. Pause before introducing yourself. Ask: what would you need to understand for a visualisation to have helped you? This is a course about communication and visual reasoning, with Python as the principal implementation tool.', openingQuote.notes);
    text(s, 'quote-lead', '“The purpose of visualization is', 80, 120, 1120, 78, 51);
    text(s, 'quote-emphasis', 'insight, not pictures.”', 80, 208, 1120, 92, 68, C.accent, { bold: true });
    text(s, 'course-title', 'Data Visualization and Storytelling', 80, 440, 1120, 65, 41, C.ink, { bold: true });
    text(s, 'course-meta', 'ECBS5209 · CEU · Fall 2026\nUlrich Wohak · 4 November 2026', 80, 523, 1120, 92, 27);
  }
  {
    const s = slide('Welcome to the course', 'Introduce yourself and confirm practical questions in the room. Contact and credits come from the syllabus; do not import the Coding 1 teaching assistant or its policies. Office hours and room remain TBD.');
    lines(s, ['Ulrich Wohak, PhD · wohaku@ceu.edu', 'MSc Business Analytics · 1 US credit / 2 ECTS', 'Six Wednesday sessions · 17:40–19:20', 'Bring your laptop; use your existing Python and pandas skills.'], 165, 100, 32);
    label(s, 'Questions are welcome—especially “why this chart?”');
  }
  {
    const s = slide('What you should be able to do', 'Explain that neither visual polish nor a working plotting command alone is sufficient. The course connects purpose, evidence, design and implementation. These are selected learning outcomes, not a new assessment scheme.');
    lines(s, ['Frame a useful question for a particular audience.', 'Choose and critique charts that make comparison easier.', 'Tell a clear story without hiding uncertainty or context.', 'Build, verify and reproduce your visualisations in Python.'], 160, 100, 33);
    label(s, 'Design judgment matters as much as technical execution.');
  }
  {
    const s = slide('How we will work in class', 'Explain the recurring pattern. During redesign practice, students first diagnose a working but unsuitable chart without AI, then change it and verify the numbers. These are formative exercises under the current syllabus. They replace some existing practice time rather than extending the class. The two Power BI sessions apply the same routine in another tool. Short project reviews use existing practice time in Sessions 2–4.');
    lines(s, ['Discuss a question and inspect the evidence.', 'Build Python examples, then Power BI charts and dashboards.', 'Inspect a chart and decide what you would change.', 'Explain your choices; check what changed and what did not.'], 160, 100, 32);
    label(s, 'The code may run perfectly while the chart communicates badly.');
  }
  {
    const s = slide('Our six sessions', 'All meetings are 100 minutes, 17:40–19:20. Sessions 5–6 cover Power BI basics, then dashboard building. Short project reviews take place in Sessions 2–4 instead of a standalone project class. Plotly, Streamlit and the project-workshop notebooks remain optional support. Confirm the access route well before Session 5. Source: local syllabus and session plan.');
    const values = [['Date', 'Focus'], ['4 Nov', 'Purpose, audience and questions'], ['11 Nov', 'Perception and truthful comparison'], ['18 Nov', 'Analytical chart forms'], ['25 Nov', 'Design and storytelling'], ['2 Dec', 'Power BI: introduction and basic charts'], ['9 Dec', 'Power BI: building a dashboard']];
    const t = s.tables.add({ rows: 7, columns: 2, left: 80, top: 152, width: 1120, height: 445,
      columnWidths: [195, 925], values });
    t.borders.assign({ fill: C.paper, width: 0 });
    for (let r = 0; r < 7; r++) {
      t.rows[r].height = r === 0 ? 55 : 65;
      for (let c = 0; c < 2; c++) {
        const cell = t.getCell(r, c);
        cell.fill = r === 0 ? C.ink : C.paper;
        cell.text.style = { typeface: 'Arial', fontSize: 29, color: r === 0 ? '#FFFFFF' : C.ink,
          bold: r === 0 || r >= 5, verticalAlignment: 'middle' };
      }
    }
    text(s, 'time', 'Wednesdays, 17:40–19:20 · 2026', 80, 615, 1120, 40, 27, C.muted);
  }
  {
    const s = slide('Assessment', 'The instructor confirmed on 4 November 2026 that the 25% individual assignment is an original figure answering a supplied question using supplied data, with figure and notes as the only submission. The 75% final project remains unchanged. Classroom redesign exercises are ungraded practice. The syllabus states 50% minimum to pass. Due dates and submission routes are TBD; announce them when confirmed.');
    text(s, 'redesign-weight', '25%', 80, 174, 220, 100, 74, C.accent, { bold: true });
    text(s, 'redesign-label', 'Individual figure with notes', 330, 174, 860, 100, 36);
    text(s, 'story-weight', '75%', 80, 322, 220, 100, 74, C.accent, { bold: true });
    text(s, 'story-label', 'Final Python data story', 330, 322, 860, 100, 36);
    text(s, 'assessment-note', 'In-class exercises: practice and feedback\nMinimum overall mark to pass: 50%', 80, 495, 1100, 100, 30);
    text(s, 'deadline', 'Submission dates and routes: to be announced', 80, 612, 1100, 40, 25, C.muted);
  }
  {
    const s = slide('The individual figure · 25%', 'The instructor supplies the data and question when the assignment opens. Students design a figure from scratch in Python. Submit only the figure and its attached notes, with no code, separate rationale or other supporting files. Notes provide relevant provenance, sample, units, aggregation, filters, uncertainty and limitations, plus a brief AI disclosure. Assess the answer, analytic correctness, design, accessibility and notes. Do not assess unsubmitted code. The final project is unchanged. Source: assignments/chart-critique-redesign/README.md.');
    lines(s, ['I supply the data and the question.', 'You design an original figure in Python.', 'Submit only the figure with its accompanying notes.', 'Check that the figure answers the question accurately.'], 160, 100, 32);
    label(s, 'The reader should understand the figure without your code.');
  }
  {
    const s = slide('The final Python data story · 75%', 'Use the final-data-story brief as authority. Individuals or teams of up to three create 3–5 purposeful figures with a narrative, local reproducible code, provenance and disclosures. Teams include contribution statements. Interactive output is not required; a strong static story is enough. Short reviews in Sessions 2–4 support the project; the former project-workshop notebooks remain optional.');
    lines(s, ['One coherent question and a specific audience.', 'A sequence of 3–5 figures—not an unrelated chart collection.', 'Reproducible code, data provenance and a written narrative.', 'Work individually or in a team of up to three.'], 160, 100, 32);
    label(s, 'A strong static story is enough; interactivity is not required.');
  }
  {
    const s = slide('AI: use it, then verify it', 'The policy differs from Coding 1. Material AI use must be disclosed; using AI is permitted, but the student owns every number, decision and claim. Do not send confidential data. For classroom redesigns, inspect the weak chart yourself before asking an assistant. Source: docs/ai_policy.md.');
    lines(s, ['You may use AI for code, alternatives and critique.', 'Check rows, aggregation, scales, labels and claims.', 'Understand the result well enough to explain and change it.', 'Disclose material assistance; protect confidential information.'], 160, 100, 32);
    label(s, 'A confident answer is not evidence that a chart is correct.');
  }
  {
    const s = slide('Where to find the material', 'Repository is the technical home of the course. Live, completed and exercise notebook variants exist; The Session 5 interactivity and Session 6 project notebooks are optional support. Scheduled Sessions 5–6 use Power BI workshop guides. Cairo is primary, Munzner secondary. The local Cairo PDF is a 72-page excerpt, not the complete book; do not describe it as a full copy or distribute it. No book purchase is required.');
    text(s, 'repo', 'github.com/ulrichwohak/Python-Dataviz', 80, 150, 1120, 65, 35, C.accent, { bold: true });
    lines(s, ['Python notebooks and Power BI workshop guides', 'Python: pandas, matplotlib and seaborn · environment: uv', 'Cairo: The Functional Art · primary conceptual influence', 'Munzner: Visualization Analysis and Design · supporting framework'], 260, 85, 29);
    text(s, 'reading', 'No required textbook purchase. Readings will be identified in class.', 80, 614, 1120, 36, 25, C.muted);
  }
  {
    const s = slide('What are we trying to make small?', 'Show the equations first; do not derive them. Then ask what the bracketed quantity means and reveal the picture. X has a column of ones and the x values. The scalar and matrix expressions describe the same objective. The appendix expands the notation for questions; it is not an additional regression lesson.', 'OLS objective: https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd431.htm . Matrix notation: https://stat151a.berkeley.edu/fall-2024/lectures/Lecture4.html .');
    math(s, 'scalar-left', '(β̂₀, β̂₁) = arg min', 100, 210, 500, 100, 50);
    math(s, 'min-over', 'β₀, β₁', 442, 290, 150, 40, 27);
    math(s, 'sigma', '∑', 601, 196, 80, 112, 79);
    math(s, 'n', 'n', 624, 170, 45, 35, 27);
    math(s, 'i', 'i = 1', 607, 302, 80, 35, 25);
    math(s, 'residual-squared', '[yᵢ − (β₀ + β₁xᵢ)]²', 700, 210, 500, 100, 46);
    math(s, 'matrix', 'β̂ = arg min (y − Xβ)ᵀ(y − Xβ)', 210, 425, 1000, 85, 47);
    math(s, 'matrix-over', 'β', 375, 490, 55, 40, 28);
    label(s, 'The equation gives precision. Can a picture give intuition?');
  }
  const best = fitLine(example.x, example.y);
  for (const [beta, fitted] of [[example.candidate, false], [best, true]]) {
    const s = slide(fitted ? 'Moving the line reduces squared error' : 'The gaps become visible',
      `Five constructed points, not observed data. x=${example.x}; y=${example.y}. Line coefficients=${beta}. SSE=${sse(beta).toFixed(2)}. Each orange segment is a VERTICAL gap at fixed x, not the shortest perpendicular distance to the line. Each separate square has side length equal to that gap's magnitude. The scales and square positions are identical on both slides. Comparing these two lines illustrates minimisation; it does not prove the formula. ${fitted ? 'Return to the equation and connect y, prediction and residual. Read Cairo’s quotation with emphasis on because.' : 'Ask students which gap contributes most to the sum.'}`,
      'Original synthetic mathematical illustration. Cairo quotation: The Functional Art, printed p. xv (local PDF p. 16). OLS: NIST link in preceding slide.');
    const prediction = x => Number((beta[0] + beta[1] * x).toFixed(10));
    const series = example.x.map((x, i) => ({ name: `Residual ${i + 1}`, xValues: [x, x], values: [prediction(x), example.y[i]], line: { fill: C.orange, width: 3 }, marker: { symbol: 'none' } }));
    series.push({ name: 'Candidate line', xValues: [0, 15], values: [prediction(0), prediction(15)], line: { fill: C.accent, width: 3 }, marker: { symbol: 'none' } });
    series.push({ name: 'Observations', xValues: example.x, values: example.y, line: { fill: 'none', width: 0 }, marker: { symbol: 'circle', size: 9, fill: C.ink }, dataLabelOverrides: example.x.map((_, i) => ({ idx: i, text: String(i + 1), position: example.y[i] < prediction(example.x[i]) ? 'bottom' : 'top', showValue: false, textStyle: { fontSize: 19, fill: C.ink } })) });
    scatter(s, 'OLS residuals', series, { title: 'x', min: 0, max: 15, majorUnit: 3 }, { title: 'y', min: 0, max: 6, majorUnit: 2 }, { left: 55, top: 165, width: 680, height: 405 });
    text(s, 'square-heading', 'A square for each vertical gap', 765, 160, 450, 80, 28, C.accent, { bold: true });
    const centers = [792, 880, 968, 1060, 1160];
    residuals(beta).forEach((gap, i) => {
      const side = Math.abs(gap) * 45;
      s.shapes.add({ name: `Squared gap ${i + 1}`, geometry: 'rect', position: { left: centers[i] - side / 2, top: 370 - side, width: side, height: side }, fill: C.pale, line: { fill: C.orange, width: 1.5 } });
      text(s, `id-${i}`, String(i + 1), centers[i] - 28, 380, 56, 32, 22, C.ink, { alignment: 'center' });
      text(s, `area-${i}`, (gap * gap).toFixed(2), centers[i] - 36, 426, 72, 35, 22, C.orange, { alignment: 'center' });
    });
    text(s, 'total-area', `Total area = ${sse(beta).toFixed(2)}`, 765, 492, 450, 58, 38, C.orange, { bold: true });
    text(s, 'synthetic', 'Five synthetic points · same axes and square-size scale', 80, 580, 1120, 35, 21, C.muted);
    if (fitted) {
      text(s, 'cairo-quote-start', '“We understand', 80, 621, 210, 40, 28, C.accent);
      text(s, 'cairo-because', 'because', 295, 621, 115, 40, 28, C.accent, { italic: true });
      text(s, 'cairo-quote-end', 'we see.” — Alberto Cairo, p. xv', 414, 621, 760, 40, 28, C.accent);
    } else label(s, 'Choose the line that makes the sum of the square areas smallest.', 621);
  }
  if (hotels.length !== 24) throw Error('Expected 24 synthetic hotels.');
  const pooled = fitLine(hotels.map(d => d.distance_km), hotels.map(d => d.price_eur));
  const groups = ['A', 'B', 'C'].map((country, i) => {
    const rows = hotels.filter(d => d.country === country);
    const x = rows.map(d => d.distance_km), y = rows.map(d => d.price_eur);
    return { country, x, y, beta: fitLine(x, y), color: [C.accent, C.orange, C.blue][i], symbol: ['circle', 'square', 'triangle'][i] };
  });
  if (!(pooled[1] > 0) || !groups.every(g => g.x.length === 8 && Math.abs(g.beta[1] + 8) < 1e-8)) throw Error('Missing slope reversal.');
  for (const grouped of [false, true]) {
    const s = slide(grouped ? 'The same points tell a different story' : 'What would you conclude from this chart?',
      grouped ? 'Reveal country membership without changing data or axes. Within every fictional country the slope is −8, while the pooled slope is positive. Groups differ in both mean distance and mean price. Neither relationship is causal. Ask what would be misleading about presenting only the pooled chart. This is a deliberately constructed Simpson reversal, not an empirical market claim.' : 'Do not reveal countries yet. Ask students to describe the visible association, then ask whether they would trust it as the whole story. One point is one hotel. The next slide keeps all points and scales identical.',
      `Synthetic data: data/raw/simpson_hotels.csv generated by make_simpson_hotels(). Pooled slope ${pooled[1]}; group slopes ${groups.map(g => g.beta[1])}. Concept: Kievit et al. (2013), https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00513/full .`);
    const series = [{ name: 'Pooled fit', xValues: [1, 11], values: [1, 11].map(x => Number((pooled[0] + pooled[1] * x).toFixed(8))), line: { fill: grouped ? '#A6ADB5' : C.ink, width: 2.5 }, marker: { symbol: 'none' } }];
    if (grouped) groups.forEach(g => {
      const ends = [Math.min(...g.x), Math.max(...g.x)];
      series.push({ name: `Country ${g.country} fit`, xValues: ends, values: ends.map(x => Number((g.beta[0] + g.beta[1] * x).toFixed(8))), line: { fill: g.color, width: 3 }, marker: { symbol: 'none' } });
      series.push({ name: `Country ${g.country}`, xValues: g.x, values: g.y, line: { fill: 'none', width: 0 }, marker: { symbol: g.symbol, size: 10, fill: g.color } });
    });
    else series.push({ name: 'Hotels', xValues: hotels.map(d => d.distance_km), values: hotels.map(d => d.price_eur), line: { fill: 'none', width: 0 }, marker: { symbol: 'circle', size: 10, fill: C.ink } });
    scatter(s, 'Pooled and within-country association', series, { title: 'Distance from city centre (km)', min: 0, max: 12, majorUnit: 3 }, { title: 'Price per night (€)', min: 0, max: 220, majorUnit: 50 }, { left: 60, top: 150, width: 780, height: 470 });
    text(s, 'relationship', grouped ? 'Within each country:\nprice falls with distance.' : 'Across all hotels:\nprice rises with distance.', 885, 195, 325, 145, 30, C.accent, { bold: true });
    if (grouped) groups.forEach((g, i) => text(s, `group-${i}`, `${['●', '■', '▲'][i]}  Country ${g.country}`, 900, 365 + i * 58, 300, 48, 27, g.color));
    else text(s, 'hidden', 'What information\nmight be missing?', 885, 403, 325, 125, 32);
    text(s, 'synthetic-note', 'Synthetic illustration · 24 hotels · three fictional countries · association, not causation', 80, 630, 1120, 35, 21, C.muted);
  }
  const cairoSource = 'Alberto Cairo / Época, The Functional Art, Figure 3, printed p. xix (local PDF p. 20). Surrounding discussion pp. xvi–xx. Original figure credits World Bank, IMF and IBGE. Source-image critique, not an independent data verification. Images and exports remain local; see NOTICE.md.';
  {
    const s = slide('What is this figure trying to communicate?', 'Let students look before offering the instructor’s critique. Ask for one-sentence takeaways. Compare responses: GDP and inequality, historical change, or a story about governments? This is a magazine graphic, not an academic-paper figure. The next slide enlarges the chart.', cairoSource);
    s.images.add({ blob: fullFigure, contentType: 'image/png', fit: 'contain', alt: 'Cairo’s Figure 3 for Época: Brazilian GDP and Gini, years and presidencies, with headline and source.', position: { left: 70, top: 132, width: 640, height: 500 } });
    text(s, 'question', 'Describe the takeaway\nin one sentence.', 770, 245, 430, 110, 35, C.accent, { bold: true });
    text(s, 'agreement', 'Would another reader\nchoose the same message?', 770, 430, 430, 110, 30);
    text(s, 'credit', 'Cairo / Época · The Functional Art, Figure 3, p. xix', 80, 637, 1120, 30, 19, C.muted);
  }
  {
    const s = slide('Which details serve the intended purpose?', 'Identify the encodings: GDP LEVEL on x, Gini on y, successive years along a path, presidencies in colour. The connecting path is not a fitted regression line; colours are not evidence of government causation. For a focused academic argument, some layers may distract. For historical exploration they may be useful. Ask what should be retained, removed or separated for each purpose. Density is not automatically bad.', cairoSource);
    s.images.add({ blob: chartDetail, contentType: 'image/png', fit: 'contain', alt: 'Enlarged Figure 3 chart with axes, chronology, presidency colours, annotation and sources retained.', position: { left: 70, top: 145, width: 780, height: 485 } });
    text(s, 'academic', 'A focused finding?', 885, 205, 320, 70, 31, C.accent, { bold: true });
    text(s, 'historical', 'Historical exploration?', 885, 335, 320, 90, 31, C.accent, { bold: true });
    text(s, 'layers', 'Keep, remove,\nor separate?', 885, 490, 320, 90, 30);
    text(s, 'credit', 'Cairo / Época · Figure 3, p. xix · same figure, enlarged chart detail', 80, 637, 1120, 30, 19, C.muted);
  }
  {
    const s = slide('Give each figure a job—and enough context', 'Tie together the examples. Purpose may be explanation, exploration, scrutiny, curiosity, or motivation of a hypothesis. Do not predetermine an exploratory conclusion. Adapt to readers without changing evidence. Figure notes are part of the visualisation: units, sample, period, aggregation, uncertainty and sources as relevant. Later we will examine statistical-result charts; do not invent intervals or confuse variation with uncertainty.');
    lines(s, ['Who is reading—and what are they trying to understand?', 'What should this figure reveal, support or let them explore?', 'What would become misleading if we left it out?', 'Keep necessary units, sample, uncertainty and source notes.'], 160, 100, 32);
    label(s, 'Simplify the presentation, not the evidence.');
  }
  {
    const s = slide('A quick Reddit chart critique', 'In pairs, browse either community and choose one chart to discuss. Ask students to describe its intended message, identify something clear or potentially misleading, and propose one concrete change. Judge the chart rather than assuming that its subreddit name establishes its quality. This is ungraded discussion within the introduction, not an additional assignment. Preview the live feeds before class because their contents change. If browsing is unavailable, use the preceding Cairo figure with the same questions.', 'Discussion links supplied by the instructor: https://www.reddit.com/r/dataisugly/ and https://www.reddit.com/r/dataisbeautiful/.');
    const links = [
      { label: 'reddit.com/r/dataisugly', url: 'https://www.reddit.com/r/dataisugly/', rect: [80, 155, 1120, 60] },
      { label: 'reddit.com/r/dataisbeautiful', url: 'https://www.reddit.com/r/dataisbeautiful/', rect: [80, 235, 1120, 60] },
    ];
    for (const [i, link] of links.entries()) {
      const t = text(s, `reddit-link-${i}`, link.label, ...link.rect, 36, C.accent, { underline: 'sng' });
      t.text.get(link.label).link = { uri: link.url, isExternal: true };
    }
    notes.at(-1).links = links;
    text(s, 'exercise', 'Choose a chart and discuss it with a neighbour.', 80, 345, 1120, 65, 32, C.ink, { bold: true });
    lines(s, ['What do you learn from it?', 'What is clear, and what could mislead the reader?', 'What one change would you make?'], 425, 75, 30);
  }
  {
    const s = slide('Your first redesign: change over time', 'Run the Session 1 activity in the live or exercise notebook. Ask students to diagnose before choosing a new chart. Keep the first 12 weekly totals, their order, and missing-value handling consistent. A chronological line or bars can both work. Let students implement their choice and check the first and last values against the printed series. This uses existing practice time, not an extra assessed task.', 'scripts/redesign_activities.py; data/raw/sales.csv from scripts/fetch_data.py. All data synthetic.');
    text(s, 'brief', 'A manager asks: “How did weekly revenue change?”', 80, 140, 1120, 65, 33, C.accent, { bold: true });
    const c = s.charts.add('pie', { name: 'Deliberately unsuitable pie chart of weekly revenue', position: { left: 80, top: 230, width: 610, height: 365 },
      categories: weekly.map(d => d.date.slice(5)), series: [{ name: 'Weekly revenue', values: weekly.map(d => d.revenue) }], hasLegend: true,
      legend: { position: 'right', textStyle: { fontSize: 17 } }, chartFill: C.paper });
    chartFont(c, { fontFamily: 'Arial' });
    text(s, 'task', 'Diagnose the mismatch.\n\nRedesign the chart.\n\nVerify the values.', 770, 263, 425, 290, 32);
    text(s, 'chart-note', 'Synthetic course data · first 12 weekly totals · missing revenue excluded', 80, 630, 1120, 35, 22, C.muted);
  }
  {
    const s = slide('Today: from question to a first redesign', 'Move to notebooks/live/session01_purpose_audience_and_questions.ipynb. For a 100-minute session allow roughly 30–35 minutes for the introduction, including discussion, then data inspection and live plotting, and 10–15 minutes for the redesign. Skip optional exploration-board tasks if needed; retain verification and the short explanation. These are facilitator suggestions, not extra student deadlines.');
    lines(s, ['Inspect the synthetic sales data and its limitations.', 'Frame a question for a commercial manager.', 'Build and interpret a first chart together.', 'Redesign the supplied chart; explain and verify your choice.'], 160, 100, 32);
    label(s, 'Open the Session 1 live notebook.');
  }
  {
    const s = slide('Backup · the same OLS objective in matrix form', 'Use only if students ask. For an intercept and one predictor, X contains a column of ones and the x values; y and e are n-vectors and beta is a two-vector. At the optimum Xᵀe = 0: residuals are orthogonal to the columns of X in observation space. This does NOT mean perpendicular distances in the scatterplot. The inverse formula requires full column rank. The visual comparison was an illustration, not a proof.', 'NIST and Berkeley sources on slide 11. Synthetic example in ols-opening.mjs.');
    math(s, 'matrix-def', 'X = [(1, x₁); … ; (1, xₙ)]     β = (β₀, β₁)ᵀ', 80, 160, 1120, 90, 41);
    math(s, 'residual-vector', 'e = y − Xβ', 80, 280, 1120, 70, 46);
    math(s, 'normal-equation', 'Xᵀ(y − Xβ̂) = 0', 80, 380, 1120, 70, 46);
    math(s, 'solution', 'β̂ = (XᵀX)⁻¹Xᵀy', 80, 480, 1120, 70, 46);
    text(s, 'rank', 'Inverse formula requires X to have full column rank.', 80, 592, 1120, 50, 29, C.accent);
  }
  {
    const s = slide('Backup · setup and Power BI access', 'The Python commands run from the repository root. The VS Code notebook setting or manual working-directory choice should keep notebooks rooted there. Before 2 December, confirm a Windows computer or an institution-provided access route for all students. CEU virtual-lab availability is not established. Do not require a purchase or claim an access route works before testing it.', 'README.md; workshops/power-bi/README.md. Power BI Desktop access requirements must be confirmed before class.');
    text(s, 'python-label', 'Python: from the repository root', 80, 150, 1120, 55, 32, C.accent, { bold: true });
    text(s, 'commands', 'uv sync\nuv run python scripts/fetch_data.py\nuv run jupyter lab', 80, 230, 1120, 165, 30, C.ink, { typeface: 'Consolas' });
    text(s, 'powerbi-access', 'Before Session 5: Power BI access will be confirmed.\nWindows / CEU access route: to be announced.\nNo purchase is required for this course.', 80, 460, 1120, 160, 29);
  }
  return { presentation: p, notes };
}
