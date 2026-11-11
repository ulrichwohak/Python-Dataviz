# NOTICE

This file records external sources that inform or are adapted in the course. The repository's
MIT License applies to original course code and text; it does not change the rights attached to
third-party books, software, data, images, or examples.

## Conceptual course references

### Alberto Cairo, *The Functional Art*

- **Full title:** *The Functional Art: An Introduction to Information Graphics and
  Visualization*
- **Author:** Alberto Cairo
- **Edition:** first edition, New Riders, published 2012, copyright 2013
- **ISBN:** 978-0-321-83473-7
- **Publisher record:** <https://www.pearson.com/en-us/subject-catalog/p/functional-art-the-an-introduction-to-information-graphics-and-visualization/P200000008946/9780321834737>
- **Use in this course:** conceptual guidance on function before decoration, visualisation as a
  cognitive and communication tool, exploration and explanation, narrative, and the design
  process.
- **Short quotation in the Session 1 opening slides:** “We understand *because* we see.”
  Introduction, “The partnership of presentation and exploration”, printed p. xv. Italics on
  *because* are original. Verified against the local textbook (PDF page 16); no page image or
  textbook file is distributed in Git.
- **First-slide quotation:** “The purpose of visualization is insight, not pictures.” Cairo
  attributes it to Ben Shneiderman on printed p. xx (PDF page 21), footnote 3. The cited volume is Stuart K. Card,
  Jock D. Mackinlay, and Ben Shneiderman, *Readings in Information Visualization: Using Vision
  to Think* (1999). [Shneiderman's bibliography](https://www.cs.umd.edu/~ben/books.html)
  lists Morgan Kaufmann, San Francisco; Cairo's footnote gives Academic Press, London.
  The fuller slide reference follows the author's bibliography. No original page number
  in the 1999 volume is claimed.
- **Figure 3 discussion:** printed p. xix (PDF page 20), with surrounding discussion on
  pp. xvi–xx. The book identifies the graphic as Alberto Cairo's work for *Época* magazine,
  translated from Portuguese. The figure credits the World Bank, IMF, and IBGE. Local
  classroom extracts retain the figure and source credit. The student introduction PDF
  includes this example for discussion at the instructor's request. The source textbook
  and separate image files are not distributed. The figure is not covered by this
  repository's MIT licence; its inclusion does not grant further reuse rights.

### Tamara Munzner, *Visualization Analysis and Design*

- **Full title:** *Visualization Analysis and Design*
- **Author:** Tamara Munzner
- **Edition:** first edition, A K Peters/CRC Press, 2015
- **ISBN:** 978-1-4665-0891-0
- **Publisher record:** <https://www.routledge.com/Visualization-Analysis-and-Design/Munzner/p/book/9781466508910>
- **Author's companion site:** <https://www.cs.ubc.ca/~tmm/vadbook/>
- **Use in this course:** supporting vocabulary for what–why–how analysis, marks and channels,
  colour and other encodings, interaction and multiple views, and validation.

These are copyrighted books. The repository does not redistribute either book and does not
place their figures or extended text under the repository licence. Students should use a
legitimate copy obtained from the publisher, a library, or another authorised source. The
course notebooks are self-contained technical materials; selective readings supplement them.

## Least-squares opening demonstration

The original data-backed figures in
[`presentations/session01/course-introduction.pdf`](presentations/session01/course-introduction.pdf)
use 100 synthetic observations. A local
`random.Random(42)` draws x with mean 1 and standard deviation 2.3, sorts those x values,
then generates `y = 0.5 + 0.55*x + noise`, with independent standard-normal noise.
These are original illustrative data, not observed business data or an external dataset.
The builder estimates the line from the generated observations rather than displaying the
data-generating coefficients. Both slides use identical points and scales. The instructor's
supplied scatterplot guided the visual style; no image or data were copied from it.

References for the mathematics (consulted 3 November 2026):

- NIST/SEMATECH, [*e-Handbook of Statistical Methods*, §4.4.3.1, Least Squares](https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd431.htm):
  scalar objective and straight-line fitting.
- UC Berkeley, [STAT 151A, Fall 2024, *Least squares as a projection*](https://stat151a.berkeley.edu/fall-2024/lectures/Lecture4.html):
  normal equations, matrix solution and its invertibility condition. No source figures or
  substantial prose are reproduced.

## Simpson's-paradox opening demonstration

The Session 1 introduction uses 24 deliberately constructed hotels in fictional countries
A, B, and C. The original generator `make_simpson_hotels()` and the data-backed charts
illustrate the reversal between a positive
pooled slope and negative within-country slopes. Data preparation writes the local
`data/raw/simpson_hotels.csv`; no real country or hotel data are used.

Conceptual reference (consulted 3 November 2026): Rogier A. Kievit, Willem E. Frankenhuis,
Lourens J. Waldorp and Denny Borsboom (2013),
[*Simpson's paradox in psychological science: a practical guide*](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00513/full),
Frontiers in Psychology 4:513, doi:10.3389/fpsyg.2013.00513. Figure 1 demonstrates the
continuous-data reversal. No source figure, data, or substantial prose is reproduced.

## Instructor-supplied chart-critique images

Four images supplied on 4 November 2026 appear unchanged on slides 18–21 of the
student introduction PDF. Separate source image files are not distributed.
They are source images for criticism, not verified datasets or endorsements. No original
post URLs or redistribution licences were supplied. Visible credits are retained:

- `prices-and-wages.png`: photograph showing CBS News branding and a Bureau of Labor
  Statistics source credit. The image compares labels of 21% since January 2021 and
  3.8% since “last September”; the broadcast date and underlying series are unverified.
- `florida-firearm-murders.png`: image bearing Reuters, C. Chan, 16/02/2014 and Florida
  Department of Law Enforcement credits. We critique the axis and labelling, without
  independently verifying counts or claiming a policy effect.
- `pool-and-skyscrapers.png`: social-media screenshot bearing @realDonaldTrump and the
  heading “Our Pool is Bigger than Skyscrapers”. The original post, authorship and
  measurements have not been authenticated. Critique concerns the displayed comparison.
- `county-suicide-rates.png`: screenshot bearing amazingmap and a 30 October 2024 post
  date. That is not an established data period. The underlying source, estimation method
  and reuse rights are unknown.

The instructor has requested inclusion of these images in the student PDF for classroom
critique. The repository's MIT licence does not apply to them; inclusion grants no further
reuse rights. Visible design features can be discussed without treating the underlying
claims or data as independently verified.

## Session 2 submitted visualisations

The 11 November 2026 presentation includes 18 third-party images and four week 1
student submissions supplied for classroom discussion. Original images and visible credits
are preserved in the slides. The Lecture 2 notebook contains only the live-coding analysis;
submitted figures and the week 1 review belong in the presentation. Filenames describing an image as good or ugly are
not used as judgments in the lecture. No original post URLs or reuse licences accompanied
these files. The credits below identify what is visible, not independently authenticated
authorship or data provenance. The repository's MIT licence does not apply to these images.

| Lecture ID | Image | Visible attribution or source information |
| --- | --- | --- |
| V01 | Average monthly wage in the EU | No creator, data source or currency shown. |
| V02 | 3D pie-chart template | No creator or source shown; placeholder labels. |
| V03 | Survey shares in a semicircle | CPOST/NORC, September 2021; cpost.uchicago.edu; caption refers to a US Census adult-population estimate. |
| V04 | Cigarette cost in Australia | 9NEWS; Adobe Stock. |
| V05 | Weekly initial unemployment claims | Alabama Department of Labor, Labor Market Information Division. |
| V06 | Browser-use areas | No creator or data source shown. |
| V07 | Timeline of world history | ChartOrigin.com; footer says the timeline is selective and its blocks do not represent actual territorial scale or boundaries. |
| V08 | Time Series Map, 1990–2022 | No creator, source or mapped variable named in the screenshot. |
| V09 | No night away from home by age | FRONT PAGES.EU; Eurostat TOUR_DEM_TOAGE, 2025; EuroGeographics/GISCO. |
| V10 | Still perfect: Porto | football-md.com / FMD; dated 2 November 2026. |
| V11 | Open-play xA versus non-penalty goals | TOP 5 branding; 2026/27 season and sample restrictions shown, no data provider named. |
| V12 | UK average temperature | BM branding; heading says 1884–2026, plotted period ends in 2025; no data source shown. |
| V13 | Kane and simulated careers | Martin Angelov / DataDealsFC.com; Understat; caption describes a seeded simulation of 20,000 careers. |
| V14 | Leisure time for men and women | OECD; Visme branding; leisure is measured in minutes per day. Survey years are not visible. |
| V15 | US COVID-19 cases on a spiral timeline | The New York Times, 6 January 2022; new US cases, seven-day average. |
| V16 | Pacific Beach building-height comparison | Feet; no creator or measurement source visible. The tallest-building label is an open-ended “239+ ft”. |
| V17 | TV station group revenue, 2025 | BIA Advisory Services / company filings. Labels give millions of dollars and percentage shares. |
| V18 | US household size, 1960–2025 | US Census Bureau, CPS table HH-4 (1960–2025); ACS 2025. Made with Artio / artio.so. These are visible source labels, not independently checked provenance. |
| S01–S04 | Monthly US births, 2014 | Student submissions, authors not named in the supplied images. S03 and S04 include FiveThirtyEight / SSA source notes. S04's twelve annual-share labels match the local data, rounded to one decimal place. The exercise uses the SSA data documented below. |

The supplied context identifies r/dataisugly as the discovery route for V01/V07 and an
unnamed football news channel for V10/V11/V13; neither is treated as original data provenance.
Student identities and private correspondence are excluded. Source screenshots retain
public creators' credits. Labels describing figures as good or poor are submission opinions,
not verified data claims. The WebP-to-PNG conversions preserve decoded pixels for the PDF.

Critique distinguishes visible design features from unverified factual claims. We have
checked the course's monthly birth totals against its local source extract; the screenshots
alone cannot establish that every plotted student value matches. The third-party datasets,
simulation code, live interactive behaviour and historical/sporting claims have not been
independently verified. The presentation embeds the images for viewing without separate image files or an internet connection.

## Real teaching data

The course downloads public source files locally; downloaded data and source HTML are
ignored by Git. Selection rules, pinned versions and hashes are documented in
[data/README.md](data/README.md) and the fetch script. Course code and prose are original;
no third-party notebook or R implementation is copied.

- **SSA daily births via FiveThirtyEight:** [source](https://github.com/fivethirtyeight/data/tree/master/births),
  commit `4c1ff5e3aef1816ae04af63218015066e186c147`, CC BY 4.0. We derive dates/weekday labels and plot counts.
- **Berke et al., Open e-commerce 1.0:** [Harvard Dataverse V1](https://doi.org/10.7910/DVN/YGLYDY),
  file 7616235, CC0 1.0. We select seven categories and 2018–2022, omit identifiers/titles from
  the student extract, and aggregate sample spending. Respect the source's research-use and
  no-re-identification notice. Do not present the sample as representative Amazon sales.
- **NOAA NCEI nClimDiv:** [statewide monthly files](https://www.ncei.noaa.gov/monitoring-content/data/us/climdiv/monthly/current/),
  mean-temperature release `climdiv-tmpcst-v1.0.0-20261105`. The course extracts all 50 states
  for 2018–2022, converts Fahrenheit to Celsius and joins by shipping state and month.
  The historical extract is checksum-pinned; see `data/README.md`. Footwear OLS estimates
  and confidence intervals are computed by the course, not published by NOAA or Berke et al.
  Participant identifiers are used internally for clustering and omitted from exported tables.
- **OWID / Global Carbon Budget:** [source](https://github.com/owid/co2-data), commit
  `382ee6c662b0ece26e111f263b44c029afad7787`. We select 2023 emissions and population
  fields for mapped countries. OWID data are CC BY; third-party source terms remain applicable.
- **Natural Earth:** [source](https://www.naturalearthdata.com/), public-domain 1:110m
  countries, version 5.1.2. We retain simplified boundaries and join keys, omitting Antarctica.
- **Callaway and Sant'Anna:** [did real-data example](https://bcallaway11.github.io/did/articles/did-basics.html#an-example-with-real-data),
  repository commit `9ead26b9d37c7f2bc202bebc4f5e8220ab7e8c13`. We extract seven numeric
  rows of published `summary(mw.dyn)` output, including its 95% simultaneous bands.
  This table is retained as a reference; the current Session 2 uses footwear OLS instead.
  The source R package is GPL-3. We neither copy its implementation nor redistribute its
  figures. Preserve the authors' warning that this application is illustrative.

[Todd Jones's catalogue](https://github.com/toddrjones/datasets) helped identify sources.
It is a discovery resource, not the producer or licensor of every linked dataset.

## Implementation references

Original chart code uses [Seaborn violin](https://seaborn.pydata.org/generated/seaborn.violinplot.html)
and [strip](https://seaborn.pydata.org/generated/seaborn.stripplot.html) plots,
[GeoPandas joins](https://geopandas.org/en/stable/docs/user_guide/mergingdata.html) and
[projections](https://geopandas.org/en/stable/docs/user_guide/projections.html).
Power BI guides are original walkthroughs, not recovered prior-year teaching files.
Official Microsoft references are linked in each guide. No screenshots are reproduced.
