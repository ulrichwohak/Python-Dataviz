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
| `raw/us_births.csv` | 5,479 dates, 2000–2014; births and weekday | Session 1; Session 2 slide review and interactive chart; annotation reference |
| `raw/amazon_purchases.csv` | 195,520 selected product-purchase records, 2018–2022 | Session 2; project reference |
| `processed/amazon_monthly.csv` | 14,190 month × state × category aggregates | Sessions 4–6; Python dashboard |
| `processed/state_month_temperature.csv` | 3,000 state × month temperatures, 50 states, 2018–2022 | Session 2 weather match |
| `processed/footwear_weather.csv` | 6,502 footwear records with matched temperatures; no participant IDs | Session 2 |
| `processed/footwear_weather_coefficients.csv` | Two OLS temperature coefficients and 95% pointwise intervals | Retained reference; not plotted in the current lecture |
| `processed/boot_month_coefficients.csv` | Eleven OLS monthly boot-price coefficients relative to January | Session 2 |
| `processed/boot_summer_contrast.csv` | One pre-specified June–August versus January contrast and interval | Session 2 |
| `raw/countries.geojson` | 176 simplified mapped areas, excluding Antarctica | Session 3 |
| `raw/co2_2023.csv` | 169 country records matched to the map | Session 3 |
| `processed/event_study_results.csv` | Seven published event-time estimates and confidence-band bounds | Retained reference; superseded in Session 2 |
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

## Footwear regressions and monthly weather

The three lecture questions use the same Amazon purchase source. Question 1 uses all
6,658 Boot/Sandal records for cumulative price distributions. Question 2 computes twelve
calendar-month summaries from the weather-matched records. Question 3 plots prepared
monthly boot-price OLS estimates. The preparation script fits the models below through
`src/dataviz_course/footwear.py`; the notebook does not rerun them. The original purchase extract and its selection rules are unchanged.
Pseudonymous source participant IDs are used only inside preparation to calculate clustered
standard errors and are omitted from every exported teaching table.

**Weather source and match.** NOAA NCEI's [nClimDiv statewide data](https://www.ncei.noaa.gov/monitoring-content/data/us/climdiv/monthly/current/),
mean-temperature release `climdiv-tmpcst-v1.0.0-20261105`, with the
[state codes and file format](https://www.ncei.noaa.gov/monitoring-content/data/us/climdiv/monthly/current/state-readme.txt).
These are area-weighted monthly state averages, not a measurement at the buyer's address.
Read element 02 for state codes 001–050 (NOAA codes, not FIPS), retain 2018–2022,
and convert Fahrenheit to Celsius as `(F - 32) * 5 / 9`. All 3,000 state-months have valid
temperatures. Match by shipping-state code, year and month, validating many-to-one cardinality.
Of 6,658 footwear records, 6,502 match; 129 with unknown state and 27 in DC are excluded
only from the weather analyses. The matched sample contains 2,062 participants and all 50 states.

The canonical 2018–2022 temperature extract is cached with SHA-256
`b563fa2b9fc15929878ead9116e3dec57e6fd53d082c665a5618b48a54b5afb9`.
NOAA rotates its dated full-history files. If the stated release is unavailable, the script
reads the current release but accepts it only if the complete selected historical extract
matches that checksum. A historical revision stops preparation. The actual download URL and
checksum are recorded in `raw/sources/noaa-state-temperature-source.json` and the preparation report.

**Question 1: budget shares.** The hypothetical $50 threshold is not a sample restriction.
The fraction of prices at or below it is calculated separately within Boots and Sandals;
each category has its own denominator. The empirical cumulative distributions retain all
prices. These are historical record shares, not current product availability or representative
shopping probabilities.

**Question 2: monthly weather summaries.** Matched records are pooled by calendar month.
Each point compares mean `temperature_c` with `100 × Boot records / all footwear records`.
Temperature is averaged over purchase records, so places and years are weighted by their
frequency in this sample; it is not a national weather average. Both scatterplots use the
same summaries and scales. These are descriptive aggregates without regression adjustment
or uncertainty intervals. Similar average temperatures do not imply identical exposure
distributions or purchasers. The plot does not identify a causal temperature effect.

**Weather OLS (retained reference, not the current classroom plot).** The outcome is 100 for a Boot record and 0 for a Sandal record, so this
linear probability model describes the share of Boots among these two categories, not
total purchases or market demand. Temperature is scaled in units of 10°C. Fit
`boot_percent ~ temperature_10c + C(state) + C(year)`, then add `C(month)` to adjust for
the usual calendar-month pattern. Both models use the same 6,502 records. Use two-way
participant/state clustered standard errors with finite-sample corrections and t critical
values with 49 degrees of freedom.

**Seasonal-price OLS.** Use all 3,081 Boot records (1,392 participants), including those
without weather matches; no outlier trimming or log transformation. Fit
`unit_price_usd ~ C(month, Treatment(reference=1)) + C(year) + C(state)`.
Month coefficients compare nominal USD prices with January after year/state adjustment;
the model assumes the same month pattern across years and states. January is an omitted
reference, not an estimated zero with a zero-width interval. Use participant-clustered
standard errors with finite-sample corrections and t critical values with 1,391 degrees
of freedom. Intervals are 95% **pointwise**, not a simultaneous band for eleven comparisons.

Define summer as June–August before examining the coefficients. Its contrast is the
equal-weight average of the three monthly coefficients relative to January. Calculate its
standard error using the full fitted covariance matrix, not an average of interval endpoints.
This is not the purchase-count-weighted mean summer price. Full formulas, counts, clustering
and unrounded estimates are recorded in `processed/footwear_model_details.json`.

All comparisons are observational. Voluntary participation, changing product mix, broad
geographic weather averages and nominal prices limit interpretation; confidence intervals
do not correct selection bias or establish causality. The seasonal coefficient plot uses
the visual form of an event-study graph, without claiming an identified intervention.
For implementation details, see [statsmodels' clustered-covariance documentation](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.RegressionResults.get_robustcov_results.html).

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
