"""Python teaching cells using documented public data. No downloads in notebooks."""

from textwrap import dedent


def m(text):
    return {"cell_type": "markdown", "source": dedent(text).strip()}


def c(text):
    return {"cell_type": "code", "source": dedent(text).strip()}


DATA_DESCRIPTIONS = {
    "births": "`us_births.csv` records daily US births from 2000 to 2014. Each row is one date, with its weekday and birth count. FiveThirtyEight published these Social Security Administration counts. They let us investigate weekday patterns and changes over time. These are historical administrative counts, not a random sample of individual mothers or an explanation of why a birth occurred on a particular day.",
    "amazon": "`amazon_purchases.csv` is an extract of Berke and colleagues' Open e-commerce 1.0 dataset. US volunteers donated their Amazon purchase histories. Each row is a product-purchase record with a date, shipping state, category, unit price, quantity and calculated spending in USD. We retain 2018–2022 and seven named product categories. The extract omits participant identifiers and product titles. This convenience sample is not representative of all Amazon customers or total company revenue.",
    "dashboard": "`amazon_monthly.csv` aggregates the same Amazon extract by month, shipping state and product category. Each row contains sample spending in USD, items purchased and the number of purchase records. There is no unique order identifier, so record counts are not order counts. Missing shipping states remain as Unknown. Months with no records for a particular state/category combination have no row.",
    "event_study_results": "`event_study_results.csv` contains published estimates from Callaway and Sant'Anna's did-package real-data example: minimum-wage increases and log teen employment in a 500-county panel, 2003–2007. Each row is a year relative to the increase, with an estimate and published 95% simultaneous confidence-band bounds. We plot their supplied results rather than estimate a model. The authors describe this as an illustrative application, not a definitive policy evaluation.",
    "countries": "`countries.geojson` contains Natural Earth's simplified country boundaries (1:110 million, version 5.1.2), with a country name and ISO code per mapped area. Antarctica is omitted. Small territories may be absent and boundaries reflect the source's cartographic conventions, not a position on sovereignty.",
    "co2": "`co2_2023.csv` contains 2023 country emissions estimates from Our World in Data and the Global Carbon Budget. Each row is a country that can be matched to our map. It includes population, territorial fossil/industrial CO₂ in million tonnes and tonnes per person, plus consumption-based estimates where available. Territorial emissions exclude land-use change. Missing values remain missing.",
}


def data_intro(datasets):
    return "\n\n".join(["## About the data", *(DATA_DESCRIPTIONS[name] for name in datasets),
        "Sources, licences, selection rules and limitations are in the [data documentation](../../data/README.md). Files are prepared by `scripts/fetch_data.py`; this notebook reads local data only."])


PY_SETUP = c('''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
''')
LECTURE_PY_SETUP = PY_SETUP
DAY_ORDER = '["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]'


def chart_basics():
    return [m('''
    ## A question before a chart

    A public-health researcher asks whether daily births are evenly spread across the week.
    Start with the longer time trend, then compare weekdays. What might a single average hide?
    '''), LECTURE_PY_SETUP, c('''
    # parse_dates asks pandas to read "date" as dates instead of text.
    births = pd.read_csv("data/raw/us_births.csv", parse_dates=["date"])
    print(births.head())
    # isna() marks missing values; sum() counts them in each column.
    print(births.isna().sum())
    print("Dates:", births["date"].min(), births["date"].max())
    '''), m('''
    ## Line plots: change over time

    Calculate the mean number of births per day in each month. Monthly totals also depend
    on the number of days in a month; this mean answers a different, explicit question.
    A Figure is the canvas and an Axes is the plotting area. Sorting dates keeps the line chronological.
    '''), c('''
    # Resampling uses the date index to group observations over time.
    # resample("MS") groups dates into months, labelled by the month's start.
    # mean() calculates the average daily count within each month.
    monthly = births.set_index("date")["births"].resample("MS").mean()
    # fig is the whole figure; ax is its plotting area. figsize is in inches.
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(monthly.index, monthly.values)
    ax.set(title="US births per day, averaged within each month", xlabel="Month", ylabel="Births per day")
    # Rotate and align date labels so that they are easier to read.
    fig.autofmt_xdate()
    # Adjust spacing to make room for titles and axis labels.
    fig.tight_layout()
    plt.show()
    '''), m('''
    ## Bar plots: compare weekdays

    Each bar represents a mean across dates, not a total across all Mondays or Tuesdays.
    Keep the familiar weekday order and start bar lengths at zero. Before running: do you expect weekends to differ?
    '''), c(f'''
    # Put weekdays in calendar order rather than alphabetical order.
    day_order = {DAY_ORDER}
    # groupby forms one group per weekday; mean averages its birth counts.
    # reindex puts those averages into our chosen weekday order.
    by_day = births.groupby("weekday")["births"].mean().reindex(day_order)
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.bar(by_day.index, by_day.values)
    # ylim fixes the vertical range; a zero baseline makes bar lengths comparable.
    ax.set(title="Average daily births by weekday, 2000–2014", ylabel="Births per day", ylim=(0, 14000))
    # Rotate the x-axis labels by 25 degrees to avoid crowding.
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    plt.show()
    print(by_day.round(1))
    '''), m('''
    The weekend difference is visible in these records. Scheduling of deliveries is one
    possible explanation, but these counts alone cannot distinguish delivery methods or establish a cause.
    ''')]


def chart_tour():
    cells = [m('''
    ## Scatter, histogram, box, violin and strip plots

    Use the same 365 dates from 2014 throughout this tour. We are comparing daily counts,
    not showing individual births. Which views reveal the weekly pattern most clearly?
    '''), c('''
    # Use the same 2014 sample in every plot; copy() keeps it separate from births.
    tour = births.loc[births["year"] == 2014].copy()
    print("Dates shown:", len(tour))
    # count() counts non-missing birth values within each weekday group.
    print(tour.groupby("weekday")["births"].count().reindex(day_order))
    '''), m('''
    ### Scatterplot

    Each point is one date. Unlike the monthly line, the daily points reveal short-run variation.
    '''), c('''
    fig, ax = plt.subplots(figsize=(9, 4))
    # .dt accesses date features; dayofyear gives 1 for 1 January, etc.
    # alpha controls opacity (0 transparent, 1 opaque); s sets marker area.
    ax.scatter(tour["date"].dt.dayofyear, tour["births"], alpha=0.6, s=15)
    ax.set(title="Daily US births in 2014", xlabel="Day of year", ylabel="Births")
    fig.tight_layout()
    plt.show()
    '''), m('''
    ### Histogram

    A histogram counts dates in numerical intervals. The two concentrations suggest that
    pooling all days may hide a meaningful grouping. We can investigate it rather than merely choose a colour.
    '''), c('''
    fig, ax = plt.subplots(figsize=(8, 4))
    # bins=20 divides the observed range into 20 equal-width intervals.
    # Each bar counts dates in an interval; white edges separate the bars.
    ax.hist(tour["births"], bins=20, edgecolor="white")
    ax.set(title="Distribution of daily US births in 2014", xlabel="Births per day", ylabel="Number of dates")
    fig.tight_layout()
    plt.show()
    ''')]
    for kind, explanation, call, parameter_notes in [
        ("Box", "The box covers the middle half of daily counts, with a line at the median. Whiskers reach the furthest observations within 1.5 box-lengths. Points beyond them are not automatically errors.", 'sns.boxplot(data=tour, x="weekday", y="births", order=day_order, color="#9DBFCA", ax=ax)',
         ["Each box shows the middle half of one weekday's birth counts.", "The line inside each box marks the median."]),
        ("Violin", 'Width shows a smoothed concentration of daily counts. `cut=0` stops at the observed range. `density_norm="width"` gives equal maximum widths, so width does not compare sample sizes. A violin is not a confidence interval.', 'sns.violinplot(data=tour, x="weekday", y="births", order=day_order, inner="quart", cut=0, density_norm="width", color="#9DBFCA", ax=ax)',
         ['inner="quart" adds lines at the quartiles, including the median.', 'cut=0 keeps the violin within the observed range of each group.', 'density_norm="width" gives each violin the same maximum width.']),
        ("Strip", "Each dot is a date. Sideways jitter reduces overlap and has no substantive meaning. Compare the actual points with the smoothed violin.", 'sns.stripplot(data=tour, x="weekday", y="births", order=day_order, jitter=0.2, alpha=0.5, size=3, color="#176B73", ax=ax)',
         ["jitter adds random sideways movement to reduce overlapping dots.", "alpha=0.5 makes dots partly transparent; size=3 sets their size."]),
    ]:
        code_comments = "\n        ".join(f"# {line}" for line in parameter_notes)
        cells += [m(f"### {kind} plot\n\n{explanation}"), c(f'''
        # Fix the random seed so the strip plot's jitter repeats on each run.
        np.random.seed(42)
        fig, ax = plt.subplots(figsize=(9, 4.5))
        # Seaborn uses column names for x/y; order preserves calendar order.
        {code_comments}
        {call}
        # Use the same vertical limits in all three views for fair comparison.
        ax.set(title="Daily US births by weekday: {kind.lower()} plot", xlabel="", ylabel="Births per day", ylim=(5000, 16000))
        ax.tick_params(axis="x", rotation=25)
        # Figure text coordinates run from 0 to 1; (0.01, 0.01) is near bottom-left.
        fig.text(0.01, 0.01, "Source: SSA via FiveThirtyEight. All 365 dates in 2014; same sample in each view.", fontsize=9)
        # rect=(left, bottom, right, top) reserves the bottom 8% for the note.
        fig.tight_layout(rect=(0, 0.08, 1, 1))
        plt.show()
        ''')]
    cells += [m('''
    What does each view reveal or conceal? Check whether the fixed limits contain all observations.
    How would you explain a violin to a reader who has never seen one?
    Session 2 develops distribution comparisons and distinguishes them from uncertainty about estimates.
    ''')]
    return cells


def notes_and_export():
    return [m('''
    ## Labels, notes and export

    The title states the quantity. Labels give units. The note identifies the source,
    period and aggregation. Keep the note attached when exporting the Figure.
    '''), c('''
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(monthly.index, monthly.values)
    ax.set(title="US births per day, averaged within each month", xlabel="Month", ylabel="Births per day")
    fig.autofmt_xdate()
    # Add a note to the figure itself, so it stays with the exported image.
    fig.text(0.01, 0.01, "SSA via FiveThirtyEight, 2000–2014. Mean daily counts within calendar months; no dates excluded.", fontsize=9)
    # Leave space below the axes for the figure note.
    fig.tight_layout(rect=(0, 0.09, 1, 1))
    # Save a PNG: dpi sets resolution; bbox_inches="tight" trims excess margins.
    fig.savefig("figures/01_monthly_births.png", dpi=150, bbox_inches="tight")
    plt.show()
    '''), m('''
    ## Your redesign

    Keep the final 20 minutes for [the exercise](exercises.ipynb). It supplies a pie chart
    of the 12 monthly birth totals in 2014. The data preparation is provided.
    ''')]


def first_exercise():
    return [m('''
    # Python chart tour — Exercises

    **Final 20 minutes. Ungraded. Work individually or in pairs.**
    Run from the repository root. Inspect the supplied pie chart, then change the plotting code.
    The data preparation is provided. A researcher asks: **How did total births change from month to month in 2014?**
    '''), c('''
    import matplotlib.pyplot as plt
    import pandas as pd

    births = pd.read_csv("data/raw/us_births.csv", parse_dates=["date"])
    monthly_redesign = births.loc[births["year"] == 2014].set_index("date")["births"].resample("MS").sum()
    print(monthly_redesign)
    '''), c('''
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.pie(monthly_redesign, labels=monthly_redesign.index.strftime("%b"), autopct="%.1f%%")
    ax.set_title("US births by month, 2014")
    plt.show()
    '''), m('''
    ## Your task

    1. What is difficult to see in this chart?
    2. Copy and change the chart cell. Keep all 12 months, the same totals and chronological order.
    3. Add labels with units and a short figure note naming the source, year and monthly aggregation.
    4. Check the January and December values against the printed table. Explain why your chart helps the reader.

    Monthly totals reflect both birth frequency and month length. Mention this limitation;
    do not silently change the quantity while redesigning the chart.
    '''), c('# Your redesigned chart here.'), m('**Your explanation and checks:**'),
    m('''
    ## Optional further practice

    Calculate births per day within each month and make a separate, clearly labelled chart.
    Does adjusting for month length change the apparent pattern? Choose one finding,
    write a supported takeaway title, and adapt the explanation for a general reader.
    Save the revised figure with its note in `figures/`.
    ''')]


def comparisons():
    return [LECTURE_PY_SETUP, m('''
    ## Purchase prices: why an average can hide the distribution

    Compare Boots and Sandals in the donated Amazon histories. Each observation is a
    purchase record. Frequent shoppers contribute repeatedly, so this is not a sample
    of independent customers. Inspect large values rather than deleting them automatically.
    '''), c('''
    # parse_dates reads the date column as dates, enabling .dt below.
    purchases = pd.read_csv("data/raw/amazon_purchases.csv", parse_dates=["date"])
    # isin keeps both footwear categories; copy() creates a separate working table.
    footwear = purchases.loc[purchases["category"].isin(["Boots", "Sandals"])].copy()
    # agg applies several summaries to unit prices within each category.
    # count reports non-missing prices, not distinct shoppers.
    print(footwear.groupby("category")["unit_price_usd"].agg(["count", "mean", "median", "min", "max"]))
    '''), m('''
    ## Histogram bins and box plots

    Both histograms contain the same prices. Check which features survive a change in bins.
    The box plot then compares the two categories on the same scale. Box-plot whiskers
    describe observed variation, not uncertainty about the median or mean.
    '''), c('''
    # Make one row of two panels; sharex=True gives both the same x-axis limits.
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharex=True)
    # strict=True checks that the panel and bin-count sequences have equal lengths.
    for ax, bins in zip(axes, [15, 40], strict=True):
        # bins controls the number of intervals; edgecolor outlines their bars.
        ax.hist(footwear["unit_price_usd"], bins=bins, edgecolor="white")
        ax.set(title=f"{bins} bins", xlabel="Price per item (USD)", ylabel="Purchase records")
    fig.tight_layout()
    plt.show()
    '''), c('''
    fig, ax = plt.subplots(figsize=(8, 4))
    # Compare both categories on one price scale, including outliers.
    sns.boxplot(data=footwear, x="category", y="unit_price_usd", color="#9DBFCA", ax=ax)
    # xlabel="" removes a redundant category-axis title.
    ax.set(title="Boot and sandal prices in donated purchase histories", xlabel="", ylabel="Price per item (USD)")
    # Put the source note near the figure's bottom-left, outside the axes.
    fig.text(0.01, 0.01, "Berke et al., Open e-commerce 1.0. Selected categories, 2018–2022. No price outliers removed.", fontsize=8)
    # Reserve the bottom 9% of the figure for that note.
    fig.tight_layout(rect=(0, 0.09, 1, 1))
    plt.show()
    '''), m('''
    ## Seasonal comparisons

    Count purchase records by calendar month and category, pooled over 2018–2022.
    A record may contain more than one item. This view asks about recorded purchases,
    not revenue or distinct shoppers. Which footwear category peaks in colder months?
    '''), c('''
    # .dt.month extracts month numbers (1–12), pooling the years here.
    # size() counts rows in each month/category group.
    # unstack makes categories into columns; absent combinations become 0.
    seasonal = footwear.groupby([footwear["date"].dt.month, "category"]).size().unstack(fill_value=0)
    print(seasonal)
    fig, ax = plt.subplots(figsize=(9, 4))
    # Plot one line per category column; marker="o" adds a dot at each month.
    seasonal.plot(ax=ax, marker="o")
    ax.set(title="Footwear purchase records by calendar month", xlabel="Month number", ylabel="Records, 2018–2022 combined", xticks=range(1, 13))
    fig.tight_layout()
    plt.show()
    '''), m('''
    ## Published estimates and uncertainty

    Now switch from variation in purchases to uncertainty about statistical estimates.
    Callaway and Sant'Anna's real-data example studies minimum-wage increases and log
    teen employment in 500 US counties, 2003–2007. We use their published `mw.dyn` output,
    without covariates, with never-treated counties as the comparison group.

    The horizontal coordinate is years since a county's first minimum-wage increase.
    The vertical coordinate is an estimated difference in log employment. The supplied
    bounds form a **95% simultaneous confidence band**, not 95% of individual observations.
    Use these bounds directly; do not replace them with estimate ± 1.96 × standard error.

    Before treatment, the published default compares successive pre-treatment periods.
    In particular, year -1 is an estimated pre-treatment contrast, **not a zero normalisation**.
    Post-treatment comparisons use the last pre-treatment year. The cohorts contributing
    to each event time vary. The authors caution that this example is illustrative, not a
    definitive evaluation of minimum-wage policy.
    '''), c('''
    # These are supplied estimates and confidence bounds, not raw observations.
    event = pd.read_csv("data/processed/event_study_results.csv")
    print(event)
    # errorbar needs distances from each estimate, not the endpoints themselves.
    # The first list entry is downward distances; the second is upward distances.
    errors = [event["estimate"] - event["ci_low"], event["ci_high"] - event["estimate"]]
    '''), c('''
    fig, ax = plt.subplots(figsize=(9, 4.5))
    # yerr supplies the distances; fmt="o" draws dots; capsize adds end caps.
    ax.errorbar(event["event_year"], event["estimate"], yerr=errors, fmt="o", capsize=4)
    # Zero is the reference for no estimated change in log employment.
    ax.axhline(0, color="grey", linewidth=1)
    # A dashed vertical line separates pre-treatment years from year 0 onward.
    ax.axvline(-0.5, color="grey", linestyle="--", linewidth=1)
    # Place a tick at each supplied event year.
    ax.set(title="Minimum-wage increases and teen employment", xlabel="Years relative to first increase (0 = first year)", ylabel="Estimated change in log employment", xticks=event["event_year"])
    # Add the source and interval definition below the plot.
    fig.text(0.01, 0.02, "Callaway & Sant'Anna, did real-data example. Published 95% simultaneous bands; illustrative application.", fontsize=8)
    fig.tight_layout(rect=(0, 0.10, 1, 1))
    # Save at 150 dots per inch, including the note in the tight image bounds.
    fig.savefig("figures/02_event_study.png", dpi=150, bbox_inches="tight")
    plt.show()
    '''), m('''
    Which estimates have bands spanning zero? That does not prove a zero effect. Which
    periods are relatively uncertain? What would disappear if we showed only the points?
    The chart does not itself establish the assumptions needed for causal interpretation.

    [Published example](https://bcallaway11.github.io/did/articles/did-basics.html#an-example-with-real-data)
    and [source details](../../data/README.md).

    Open [the exercises](exercises.ipynb), then briefly exchange project questions and an example figure.
    ''')]


def comparison_exercises():
    return [PY_SETUP, m('''
    ## What is hidden by the average?

    A researcher asks how much purchase prices vary within the Boot and Sandal categories.
    Run this chart and redesign it to show within-category variation. Keep the same records.
    '''), c('''
    purchases = pd.read_csv("data/raw/amazon_purchases.csv")
    footwear = purchases.loc[purchases["category"].isin(["Boots", "Sandals"])]
    means = footwear.groupby("category")["unit_price_usd"].mean()
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(means.index, means.values)
    ax.set(title="Footwear purchase prices", ylabel="Mean price (USD)")
    plt.show()
    '''), m('''
    1. Explain what the mean conceals. Make a distribution plot using a common scale.
    2. Add units, period, source and the convenience-sample limitation.
    3. Check the number of observations before and after. Distinguish variation from estimation uncertainty.
    '''), c('# Your redesigned distribution plot here.'), m('''
    ## What is missing from the statistical result?

    A reader wants to judge how precisely the employment changes are estimated.
    Revise the plot below using the supplied bounds. Mark treatment timing, label units
    and describe the 95% simultaneous band. Do not invent a reference-period zero.
    '''), c('''
    event = pd.read_csv("data/processed/event_study_results.csv")
    print(event)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(event["event_year"], event["estimate"], marker="o")
    ax.set_title("Employment changes")
    plt.show()
    '''), c('# Your revised estimates plot and explanation here.')]


GEO_SETUP = c('''
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

countries = gpd.read_file("data/raw/countries.geojson")
emissions = pd.read_csv("data/raw/co2_2023.csv")
''')
LECTURE_GEO_SETUP = c('''
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# read_file loads the country polygons and their coordinate-system information.
countries = gpd.read_file("data/raw/countries.geojson")
# read_csv loads the emissions table; it contains values rather than shapes.
emissions = pd.read_csv("data/raw/co2_2023.csv")
''')


def mapping():
    return [LECTURE_GEO_SETUP, m('''
    ## Geographical joins

    Which countries emit the most CO₂ in total, and which emit most per person? These are
    different questions. Join by ISO code, not by the spelling of country names. Retain map
    areas without estimates and inspect them. The simplified map omits some small territories.
    '''), c('''
    # crs tells us which coordinate reference system the map uses.
    print(countries.crs)
    # on names the matching column; how="left" retains every country polygon.
    # validate checks that each key occurs once in each table.
    # indicator adds _merge, showing whether a row found a match.
    world = countries.merge(emissions, on="iso_code", how="left", validate="one_to_one", indicator=True)
    # Inspect map areas that have no matching row in the emissions table.
    print(world.loc[world["_merge"] != "both", ["iso_code", "map_name"]])
    # isna() also finds missing values inside rows that did match a country.
    print(world.loc[world["co2_per_capita"].isna(), ["map_name", "co2_per_capita"]])
    '''), m('''
    ## Projections

    Longitude and latitude are angles, not metres. A projection changes how Earth's surface
    appears on the page. Equal Earth preserves relative areas and is useful for a world choropleth.
    `to_crs` transforms coordinates; assigning a CRS label alone does not transform them.
    '''), c('''
    # Transform the shapes' coordinates to the Equal Earth projection.
    # EPSG:8857 identifies this projection; it does not change the emissions.
    projected = world.to_crs("EPSG:8857")
    # Compare the original coordinates and the projection side by side.
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    # Give polygons a grey fill and thin white borders in each panel.
    world.plot(ax=axes[0], color="lightgrey", edgecolor="white", linewidth=0.2)
    projected.plot(ax=axes[1], color="lightgrey", edgecolor="white", linewidth=0.2)
    axes[0].set_title("Longitude and latitude")
    axes[1].set_title("Equal Earth")
    # Hide coordinate ticks and frames to focus attention on the map shapes.
    for ax in axes:
        ax.set_axis_off()
    plt.show()
    '''), m('''
    ## Choropleth: emissions per person

    Colour represents tonnes per person. Missing estimates are grey, not zero. Check the
    unit conversion: the total is in million tonnes, while population counts people.
    '''), c('''
    # Check Austria and three large emitters against the supplied per-person values.
    check = emissions.loc[emissions["iso_code"].isin(["AUT", "USA", "CHN", "IND"])].copy()
    # Convert million tonnes to tonnes before dividing by the number of people.
    check["calculated_per_person"] = check["co2"] * 1_000_000 / check["population"]
    print(check[["country", "co2", "co2_per_capita", "calculated_per_person"]])
    fig, ax = plt.subplots(figsize=(11, 5.5))
    # column supplies the values to colour; cmap selects yellow-to-red colours.
    # legend=True adds a colour scale; legend_kwds supplies its label.
    # missing_kwds gives missing values their own colour instead of treating them as 0.
    projected.plot(column="co2_per_capita", cmap="YlOrRd", legend=True, ax=ax,
                   legend_kwds={"label": "Territorial CO₂ (tonnes per person)"},
                   missing_kwds={"color": "lightgrey", "label": "No estimate"})
    ax.set_title("Territorial CO₂ emissions per person, 2023")
    # Hide the coordinate axes so the map and colour scale take priority.
    ax.set_axis_off()
    # Keep the emissions definition, projection and missing-data note with the map.
    fig.text(0.01, 0.01, "OWID / Global Carbon Budget; Natural Earth. Fossil fuels and industry; land-use change excluded.\\nEqual Earth projection. Grey areas have no estimate; they are not zero.", fontsize=8)
    # Export a PNG at 150 dots per inch, with margins fitted around the content.
    fig.savefig("figures/03_co2_per_person.png", dpi=150, bbox_inches="tight")
    plt.show()
    '''), m('''
    ## Proportional symbols: total emissions

    Place one circle within each mapped country. These are cartographic positions, not
    emission-source locations. Matplotlib's `s` controls area in points squared, so scaling
    `s` with emissions makes area proportional to emissions. Include a size legend.
    '''), c('''
    # Only draw circles for reported totals; retain all map areas in the background.
    points = projected.loc[projected["co2"].notna()].copy()
    # Replace each polygon with one point inside it for placing its circle.
    points["geometry"] = points.geometry.representative_point()
    fig, ax = plt.subplots(figsize=(11, 5.5))
    # Draw the country polygons first as a pale background.
    projected.plot(ax=ax, color="#eeeeee", edgecolor="white", linewidth=0.2)
    # geometry.x and .y provide point coordinates in the projected map.
    # s sets circle area in points squared; /10 keeps the symbols manageable.
    # alpha=0.6 makes overlapping circles partly transparent.
    ax.scatter(points.geometry.x, points.geometry.y, s=points["co2"] / 10, alpha=0.6, color="#176B73")
    # Empty x/y lists add no map points, but create labelled symbols for the legend.
    # Use the same size rule as above for a meaningful size legend.
    for total in [100, 1000, 5000]:
        ax.scatter([], [], s=total / 10, color="#176B73", alpha=0.6, label=f"{total:,} million tonnes")
    ax.legend(loc="lower left", fontsize=8)
    ax.set_title("Total territorial CO₂ emissions, 2023")
    ax.set_axis_off()
    fig.text(0.01, 0.01, "OWID / Global Carbon Budget; Natural Earth. Circle area encodes total; locations are representative map points.", fontsize=8)
    plt.show()
    '''), m('''
    ## Reading the maps fairly

    Compare China, the US and India in the table and maps. Total emissions and emissions
    per person rank countries differently. Neither measure is automatically the right one.
    These territorial estimates count production within borders; consumption-based estimates
    account for traded goods. Keep that distinction in the note.

    Optional spatial-join check: recover each representative point's containing polygon.
    This is a geometry check, not evidence about the location of factories or households.
    '''), c('''
    # A spatial join matches by location rather than by country code.
    # predicate="within" finds the polygon containing each point.
    # how="left" keeps all points, including any without a matching polygon.
    located = gpd.sjoin(points[["iso_code", "geometry"]], projected[["map_name", "geometry"]], how="left", predicate="within")
    # Missing names flag unmatched points; sum() counts the True results.
    print("Unmatched points:", located["map_name"].isna().sum())
    # duplicated() flags each repeat after the first occurrence of a code.
    print("Repeated country codes:", located["iso_code"].duplicated().sum())
    '''), m('Open [the exercises](exercises.ipynb). Check join coverage, denominator, units, missing values and projection before keeping a map.')]


def mapping_exercises():
    return [GEO_SETUP, m('''
    ## Does the map answer the question?

    A reader asks where territorial CO₂ emissions **per person** were highest in 2023.
    The supplied chart uses total emissions. Run it, then revise it without changing the year.
    '''), c('''
    initial = countries.merge(emissions, on="iso_code", how="inner").to_crs("EPSG:8857")
    fig, ax = plt.subplots(figsize=(10, 5))
    initial.plot(column="co2", cmap="Blues", legend=True, ax=ax)
    ax.set_title("CO₂ emissions")
    ax.set_axis_off()
    plt.show()
    '''), m('''
    1. Check which mapped areas disappear in the inner join. Keep all map areas in the revision.
    2. Use the requested denominator and label units. Distinguish missing values from zero.
    3. Add the year, sources, projection and emissions definition in a note.
    4. Check Austria's plotted value against total × 1,000,000 / population, allowing source rounding.
    5. Compare the US, China and India. Explain why the total and per-person rankings differ.

    Optional: compare territorial and consumption-based emissions for Austria. State precisely
    how the question changes; do not treat the two measures as competing estimates of the same quantity.
    '''), c('# Your revised map and checks here.')]


def references(slug):
    if slug == "design-and-annotation":
        return [m('# Design and annotation\n\nOptional reference: adapt the same birth counts for different readers.'), PY_SETUP,
                c('''
                births = pd.read_csv("data/raw/us_births.csv", parse_dates=["date"])
                monthly = births.set_index("date")["births"].resample("MS").mean()
                fig, ax = plt.subplots(figsize=(10, 4))
                ax.plot(monthly.index, monthly.values, color="#176B73")
                peak = monthly.idxmax()
                ax.annotate("Highest monthly daily average", xy=(peak, monthly.loc[peak]),
                            xytext=(20, -35), textcoords="offset points", arrowprops={"arrowstyle": "->"})
                ax.set(title="US births per day, averaged within each month", xlabel="Month", ylabel="Births per day")
                fig.text(0.01, 0.01, "SSA via FiveThirtyEight, 2000–2014. Calendar-month daily means; no dates excluded.", fontsize=9)
                fig.tight_layout(rect=(0, 0.08, 1, 1))
                fig.savefig("figures/reference_annotation.png", dpi=150, bbox_inches="tight")
                plt.show()
                '''), m('Write an academic figure note and a short explanation for a general reader. Keep period, units and evidence unchanged. Do not label the peak as a causal effect.')]
    if slug == "python-interactivity":
        return [m('# Python interactivity\n\nOptional reference: investigate category seasonality in the Amazon sample.'), c('''
                import pandas as pd
                import plotly.express as px

                dashboard = pd.read_csv("data/processed/amazon_monthly.csv", parse_dates=["month"])
                monthly = dashboard.groupby(["month", "category"], as_index=False)["spending_usd"].sum()
                fig = px.line(monthly, x="month", y="spending_usd", color="category",
                              labels={"spending_usd": "Sample spending (USD)", "month": "Month"},
                              title="Spending in donated Amazon histories, selected categories")
                fig.write_html("figures/reference_amazon_interactive.html", include_plotlyjs=True)
                fig.show()
                '''), m('Toggle categories and inspect exact values. Source: Berke et al., 2018–2022 convenience sample. This is historical data, not a live feed. The optional Streamlit app uses the same table.')]
    return [m('# Project workshop\n\nOptional reference: develop a question about the donated Amazon histories.'), PY_SETUP,
            c('''
            purchases = pd.read_csv("data/raw/amazon_purchases.csv", parse_dates=["date"])
            print(purchases.groupby("category")["spending_usd"].agg(["size", "sum", "mean", "median"]))
            '''), m('''
            ## Draft, check and review

            Choose an audience and a question. Create three related figures, with units,
            source notes and the sample restriction visible. Separate record counts, quantities
            and spending. Do not claim the sample represents Amazon sales or market share.
            Ask a partner to explain your main finding from the figures alone, then revise.
            The assessment brief, not this optional practice, governs final-project requirements.
            ''')]
