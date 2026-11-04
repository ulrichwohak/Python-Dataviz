# Course data

The scheduled notebooks use public real data. The OLS and Simpson's-paradox opening
slides retain explicitly constructed mathematical illustrations. They are not empirical findings.

## Prepare the local files

```bash
uv run python scripts/fetch_data.py
```

The first run downloads about **330 MB**. Internet access is required, but no login or API key.
Downloads are cached in `data/raw/sources/`; subsequent runs verify SHA-256 hashes and reuse
them. Pinned source URLs and expected hashes are in the script. If a source changes or fails,
the script stops rather than silently substituting data. A `.partial` file is not accepted as a cache.

The script writes the files below and `data/processed/preparation_report.json`, which records
source URLs, hashes, row counts, exclusions and aggregate checks. Raw and processed files
remain ignored by Git. Notebooks use local reads only and run from the repository root.
Existing legacy synthetic files may remain on an older checkout but are no longer used by
the current notebooks; the fetch script does not delete unrelated local files.

| Local file | Rows and contents | Used in |
| --- | --- | --- |
| `raw/us_births.csv` | 5,479 dates, 2000–2014; births and weekday | Session 1; annotation reference |
| `raw/amazon_purchases.csv` | 195,520 selected product-purchase records, 2018–2022 | Session 2; project reference |
| `processed/amazon_monthly.csv` | 14,190 month × state × category aggregates | Sessions 4–6; Python dashboard |
| `raw/countries.geojson` | 176 simplified mapped areas, excluding Antarctica | Session 3 |
| `raw/co2_2023.csv` | 169 country records matched to the map | Session 3 |
| `processed/event_study_results.csv` | Seven published event-time estimates and confidence-band bounds | Session 2 |
| `raw/simpson_hotels.csv` | 24 constructed fictional hotels | Introductory mathematical illustration only |

## Daily US births

Source: Social Security Administration data published by
[FiveThirtyEight](https://github.com/fivethirtyeight/data/tree/master/births),
`US_births_2000-2014_SSA.csv`, pinned to commit
`4c1ff5e3aef1816ae04af63218015066e186c147`.
FiveThirtyEight's data licence is [CC BY 4.0](https://github.com/fivethirtyeight/data/blob/master/LICENSE).

One row is one calendar date, not one birth. The preparation derives a date and weekday label,
checks uniqueness and checks the source weekday code against the calendar. It excludes no dates.
Do not combine this file with the separate overlapping CDC series.

The lecture compares monthly **mean daily counts**, so unequal month lengths do not drive the
line. The exercise deliberately asks about monthly **totals** in 2014; students preserve those
totals during redesign and discuss month length. Weekday/weekend differences are observed
patterns, not proof of a particular explanation about scheduling or delivery methods.

## Donated Amazon purchase histories

Berke, Calacci, Mahari, Yabe, Larson and Pentland (2023), *Open e-commerce 1.0*,
[Harvard Dataverse V1](https://doi.org/10.7910/DVN/YGLYDY), file 7616235.
[Study description](https://www.nature.com/articles/s41597-024-03329-6).
The catalogue links to the [authors' repository](https://github.com/aberke/amazon-study/tree/master/data).
Dataverse marks the dataset **CC0 1.0** and requests research use and no re-identification.

The source has 1,850,717 records from histories donated by 5,027 US volunteers.
The course uses only purchase records, not the demographic survey. We do not download survey
responses, and the student extract drops participant identifiers, product titles and product codes.
The cached public source still contains pseudonymous identifiers; do not try to identify participants.

Selection and transformation:

- Retain dates from 1 January 2018 through 31 December 2022. The source file contains
  39,924 records outside this interval; they are excluded even though the study describes
  2018–2022 coverage.
- Retain these exact source categories: `ABIS_BOOK` (Books), `PET_FOOD` (Pet food),
  `GIFT_CARD` (Gift cards), `SHIRT` (Shirts), `HEADPHONES` (Headphones),
  `BOOT` (Boots), and `SANDAL` (Sandals). Similar category labels are not silently pooled.
- Require positive unit price and quantity; no selected-period/category rows fail this check.
  Keep large values. There is no price trimming or outlier removal.
- Calculate `spending_usd = unit_price_usd × quantity`, rounded to cents. These are nominal USD,
  not inflation-adjusted spending or a complete measure of checkout totals including all charges.
- Preserve source shipping-state labels. Replace missing state with `Unknown`
  (28,843 extract records). State totals describe shipping destinations in the sample.
- Aggregate by calendar month, state and category. `quantity` adds items, while
  `purchase_records` counts source rows. The file has no unique order identifier.
  A count of aggregate rows is neither an item count nor an order count.

The extract totals USD 4,309,806.82; the preparation checks that the monthly table reconciles
to it and that record counts sum to 195,520. There are no artificial channel, target, demographic
or customer-value columns. Power BI demonstrates one **invented USD 100,000 monthly target**
only as a KPI interface example, separately labelled and not an observed business goal.

This is a convenience sample. Repeated purchases by the same person are not independent
customers. Changes over time or differences across states may reflect sample coverage.
Do not call this Amazon revenue, market share, representative US consumption or a causal effect.

## Country CO₂ estimates and boundaries

[Our World in Data CO₂ data](https://github.com/owid/co2-data), commit
`382ee6c662b0ece26e111f263b44c029afad7787`, drawing on the Global Carbon Budget.
OWID-produced data are CC BY; underlying third-party data retain their own terms.
See the [codebook](https://github.com/owid/co2-data/blob/master/owid-co2-codebook.csv)
and its source column for the Global Carbon Budget and population provenance.

Use 2023 consistently. `co2` is annual territorial fossil/industrial CO₂ in **million tonnes**,
excluding land-use change; `co2_per_capita` is **tonnes per person**. Multiply the total by
1,000,000 before dividing by population. Consumption-based measures account for trade and
answer a different question. Keep unavailable values missing.

Boundaries are [Natural Earth](https://www.naturalearthdata.com/), 1:110m, version 5.1.2,
[public domain](https://www.naturalearthdata.com/about/terms-of-use/).
The join uses `ISO_A3_EH`, which supplies France and Norway correctly in this version.
Three non-ISO map entities get explicit local keys `NE_CYN`, `NE_KOS`, `NE_SOL`, not invented
ISO codes. They remain unmatched. Other unmatched areas are ATF, ESH, FLK and PRI.
We do not assign neighbours' estimates or fill missing values with zero.

The boundary file is simplified, omits small territories, and uses the source's conventions
for disputed areas. Representative points place circles on the map; they are not observations
of emission-source locations. Equal Earth (EPSG:8857) is used for area comparisons.

## Published event-study results

Source: Callaway and Sant'Anna,
[Getting Started with the did Package, real-data example](https://bcallaway11.github.io/did/articles/did-basics.html#an-example-with-real-data).
The source HTML is pinned to repository commit
`9ead26b9d37c7f2bc202bebc4f5e8220ab7e8c13`.
The fetch script extracts the seven numeric rows of **`summary(mw.dyn)`**, not the earlier
simulated example and not `mw.dyn.balance`. It preserves published rounding and interval endpoints.
The source R package is GPL-3; the course copies numeric output, not R implementation or figures.
Authors' method: [Callaway and Sant'Anna (2021)](https://doi.org/10.1016/j.jeconom.2020.12.001).

The application uses the real `mpdta` panel (500 counties, 2003–2007), log teen employment,
staggered minimum-wage increases, no covariates and never-treated comparison counties.
Students plot published estimates; the course script does **not** rerun their estimator.

- `event_year`: years relative to the first increase; 0 is the first treatment year.
- `estimate`: estimated change in log employment, **not employment-rate percentage points**.
- `std_error`: published standard error.
- `ci_low`, `ci_high`: published **95% simultaneous confidence-band** bounds.

The default varying base period gives pre-treatment changes relative to the preceding period.
Thus -1 is an estimated pre-treatment contrast, **not a normalised zero**. Post-treatment
effects use the last pre-treatment period. Contributing cohorts differ by event time.
The authors explicitly caution that their real-data example is illustrative, not a definitive
minimum-wage policy evaluation. Preserve that warning and the simultaneous-band interpretation.

## Constructed introductory illustrations

The OLS scatterplot and the 24-hotel Simpson's-paradox example remain visibly labelled synthetic.
They illustrate mathematical relationships rather than empirical results. The hotel construction
is in `make_simpson_hotels()`; the OLS points are generated by the slide builder.
The legacy `generate_synthetic_data.py` script is not the current course data entry point.
It writes only to separate `legacy-synthetic/` subfolders so it cannot overwrite the real
event-study results.
