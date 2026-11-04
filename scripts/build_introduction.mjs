// Historical PowerPoint builder. Active PDF builder: build_introduction_pdf.py.
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { buildIntroduction } from '../presentations/session01/course-introduction.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const required = ['ARTIFACT_TOOL_MODULE', 'RUNTIME_NODE_MODULES', 'PRESENTATION_SKILL_DIR', 'ARTIFACT_PYTHON', 'INTRO_BUILD_DIR'];
for (const key of required) if (!process.env[key]) throw Error(`Set ${key}; see the presentation README.`);
const { Presentation, PresentationFile } = await import(pathToFileURL(process.env.ARTIFACT_TOOL_MODULE).href);
const skill = process.env.PRESENTATION_SKILL_DIR;
const { finalizePresentation, applyPresentationChartFont } = await import(pathToFileURL(path.join(skill, 'container_tools/artifact_tool_utils.mjs')).href);
const build = path.resolve(process.env.INTRO_BUILD_DIR);
const finalPath = path.join(build, 'output', 'course-introduction.pptx');
await fs.mkdir(path.join(build, 'output'), { recursive: true });
await fs.mkdir(path.join(build, 'preview'), { recursive: true });

// The generated course CSVs have no quoted fields. Fail rather than silently misparse a
// future dataset that needs a full CSV parser.
async function csv(relative) {
  const raw = await fs.readFile(path.join(root, relative), 'utf8');
  if (raw.includes('"')) throw Error(`${relative}: quoted CSV fields need a CSV parser.`);
  const [header, ...rows] = raw.trim().split(/\r?\n/).map(line => line.split(','));
  return rows.map(row => Object.fromEntries(header.map((key, i) => [key, row[i]])));
}
const hotels = (await csv('data/raw/simpson_hotels.csv')).map(d => ({ ...d, distance_km: Number(d.distance_km), price_eur: Number(d.price_eur) }));
const totals = new Map();
for (const d of await csv('data/raw/sales.csv')) {
  if (d.revenue === '') continue;
  const revenue = Number(d.revenue);
  if (!Number.isFinite(revenue)) throw Error('Invalid revenue.');
  totals.set(d.date, (totals.get(d.date) ?? 0) + revenue);
}
const weekly = [...totals.entries()].sort(([a], [b]) => a.localeCompare(b)).slice(0, 12).map(([date, revenue]) => ({ date, revenue: Number(revenue.toFixed(2)) }));
const { presentation, notes } = buildIntroduction(Presentation, applyPresentationChartFont, {
  hotels, weekly,
  fullFigure: await fs.readFile(path.join(root, 'textbook/extracts/cairo-figure3-full.png')),
  chartDetail: await fs.readFile(path.join(root, 'textbook/extracts/cairo-figure3-chart.png')),
});
const candidatePath = path.join(build, 'candidate.pptx');
await (await PresentationFile.exportPptx(presentation)).save(candidatePath);
await finalizePresentation({
  workspaceDir: build, candidatePath, finalPath,
  pythonExecutable: process.env.ARTIFACT_PYTHON,
  integrityValidatorPath: path.join(skill, 'container_tools/inspect_presentation_package_integrity.py'),
  layoutValidatorPath: path.join(skill, 'container_tools/inspect_presentation_layout_geometry.py'),
  layoutArgs: ['--expected-slide-size-emu', '12192000,6858000', '--validate-heading-fit', '--require-native-table-slide', '5'],
  explicitTotalSlideCount: 23,
  requiredNativeTableOwnerSlides: [5],
  requiredNativeChartOwnerSlides: [12, 13, 14, 15, 20],
  materializeLiteralChartWorkbooks: true,
  fontPolicy: { basis: 'design', families: ['Arial', 'STIX Two Math', 'Consolas'] },
  verifyArtifactToolImport: true,
  receiptPath: path.join(build, 'validation.json'),
});
for (const [index, slide] of presentation.slides.items.entries()) {
  const png = await presentation.export({ slide, format: 'png', scale: 2 });
  await fs.writeFile(path.join(build, 'preview', `slide-${String(index + 1).padStart(2, '0')}.png`), new Uint8Array(await png.arrayBuffer()));
}
await fs.writeFile(path.join(build, 'notes.json'), JSON.stringify(notes, null, 2));
console.log(`Validated deck and ${notes.length} slide previews: ${build}`);
