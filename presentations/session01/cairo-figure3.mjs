// Append this discussion to the ten-slide OLS opening.
// The caller supplies the locally extracted images; no textbook image is in Git.
// See NOTICE.md and docs/live_coding_notes.md for attribution and teaching context.
export function appendCairoDiscussion(presentation, { fullFigure, chartDetail }) {
  const C = { ink: '#182C39', muted: '#546670', paper: '#FAF8F4', teal: '#087F82' };
  const credit = 'Alberto Cairo / Época · The Functional Art, Figure 3, p. xix';
  const provenance = 'Source: Alberto Cairo, The Functional Art, Introduction, printed p. xix (local PDF page 20); surrounding discussion pp. xvi–xx. The caption identifies Época magazine, translated from Portuguese. The figure credits World Bank, IMF and IBGE. This is a source-image critique, not a reanalysis or independent verification of its data. The extracted image and this extended deck remain local and outside Git.';
  function text(slide, name, value, x, y, w, h, size = 28, color = C.ink, bold = false) {
    const shape = slide.shapes.add({ geometry: 'textbox', name,
      position: { left: x, top: y, width: w, height: h }, fill: 'none',
      line: { fill: 'none', width: 0 } });
    shape.text = value;
    shape.text.style = { typeface: 'Arial', fontSize: size, color, bold,
      insets: 0, verticalAlignment: 'middle', autoFit: 'none' };
  }
  function slide(title, notes, compact = false) {
    const s = presentation.slides.add();
    s.background.fill = C.paper;
    text(s, 'title', title, 72, compact ? 18 : 44, 1136, compact ? 56 : 70,
      compact ? 36 : 43, C.ink, true);
    text(s, 'source-credit', credit, 72, 687, 1136, 22, 16, C.muted);
    s.speakerNotes.text = `${notes}\n\n${provenance}`;
    return s;
  }
  {
    const s = slide('What is the main message?',
      'Let students inspect the original before announcing a verdict. Ask each for one sentence describing what they take away. Compare answers: a GDP–inequality relationship, change over time, or a story about presidencies? The full image retains the original headline, introductory paragraph, chart and source line. The next slide enlarges the chart; use the full-resolution local image for closer reading if needed. This is a magazine graphic, not a figure extracted from a research paper.');
    s.images.add({ blob: fullFigure, contentType: 'image/png', fit: 'contain',
      alt: 'Cairo’s Figure 3 for Época, including its headline and explanatory text. A connected scatterplot shows Brazilian GDP against the Gini inequality index, 1981–2010, with years labelled and presidencies colour-coded. The plotted path rises in the late 1980s and falls as GDP increases in later years.',
      position: { left: 72, top: 135, width: 630, height: 532 } });
    text(s, 'first-impression', 'What do you notice first?', 755, 220, 440, 95, 34, C.teal, true);
    text(s, 'one-sentence', 'Describe the takeaway\nin one sentence.', 755, 362, 440, 100, 31);
    text(s, 'agreement', 'Would another reader\nchoose the same message?', 755, 514, 440, 100, 29);
  }
  {
    const s = slide('Detail: what do the extra layers add?',
      'This detail removes only the headline and introductory paragraph shown on the previous slide; the plotting area, axes, labels, historical annotation and source credit are intact. Identify the encodings: horizontal position = GDP level; vertical position = Gini; labels and connecting path = successive years; colour and names = presidencies. The horizontal axis is not a growth rate. Ask what the dates and presidency colours add, what distracts, and which details are necessary for the intended question. Dates can reveal changing patterns that an unlabelled scatterplot would hide. Colours provide historical context but do not establish that a government caused a change. Do not treat the connecting curve as a regression fit.', true);
    s.images.add({ blob: chartDetail, contentType: 'image/png', fit: 'contain',
      alt: 'Enlarged chart detail: GDP in billions of dollars versus Gini, with all year labels, presidency colours, historical annotation, axes and source line retained. The original headline and introductory paragraph appear on the preceding slide.',
      position: { left: 186, top: 84, width: 908, height: 588 } });
  }
  {
    const s = slide('One chart, two possible purposes',
      'Introduce the instructor’s critique now: for a focused academic argument, foreground one important claim; the dates, presidency colours and historical prose may compete with it. Present this as a judgment about purpose, not a universal ban on information-rich figures. Cairo discusses presentation and exploration as a continuum and uses this graphic to support both a headline and historical discovery. Ask students to propose two designs without calculating or inventing data. For an academic relationship claim, what should be retained, removed or separated into another view? For historical exploration, what would be lost without chronology? Require reasons rather than a vote on whether the graphic is simply good or bad. Optionally ask whether the original headline needs qualification across periods. Bridge to the audience–question brief and the need for concise figure notes.');
    text(s, 'academic-heading', 'Academic explanation', 72, 175, 530, 60, 33, C.teal, true);
    text(s, 'academic-purpose', 'Make one important finding\neasy to identify.', 72, 263, 530, 100, 32);
    text(s, 'academic-question', 'Which details support the claim?\nWhich compete for attention?', 72, 408, 530, 110, 28);
    text(s, 'exploration-heading', 'Historical exploration', 678, 175, 530, 60, 33, C.teal, true);
    text(s, 'exploration-purpose', 'Let readers investigate\nchanges across periods.', 678, 263, 530, 100, 32);
    text(s, 'exploration-question', 'What do years and presidencies reveal?\nWhat would a simpler chart hide?', 678, 408, 530, 110, 28);
    text(s, 'redesign-prompt', 'For each purpose: what would you keep, remove or separate?',
      72, 589, 1136, 65, 30, C.ink, true);
  }
  return presentation;
}
