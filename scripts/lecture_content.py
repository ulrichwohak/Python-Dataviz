"""Power BI workshop cells for the three scheduled Desktop sessions."""

from real_data_content import c, m

POWER_BI_START = m('''
## Working in Power BI

This notebook is a workshop guide. Build the visuals in Power BI Desktop; Python cells at
the end are optional numerical checks. Use a Windows computer or a confirmed institutional
access route. The course's access arrangements remain TBD.

Prepare the local data once from the course root with `uv run python scripts/fetch_data.py`.
Import `data/processed/amazon_monthly.csv`. These are observed purchases donated by volunteers (Berke et al., Open e-commerce 1.0).
One row is a month × shipping state × category combination. Sample spending is unit price
multiplied by quantity, in nominal USD. Only seven categories and 2018–2022 are included.
Missing states remain Unknown. This sample is not representative of Amazon sales.
Rename the imported table to `dashboard` and use that name throughout. Interface positions can vary by installed version.
''')

POWER_BI_CHECK = c('''
import pandas as pd

# parse_dates reads "month" as dates rather than text, enabling date comparisons.
dashboard = pd.read_csv("data/processed/amazon_monthly.csv", parse_dates=["month"])
# These rows are monthly aggregates, not individual purchases or orders.
print("Rows:", len(dashboard))
print("Dates:", dashboard["month"].min().date(), "to", dashboard["month"].max().date())
# Check spending and item totals against the unfiltered Power BI cards.
print(dashboard[["spending_usd", "quantity"]].sum())
# groupby("state") calculates those same totals separately for each state.
print(dashboard.groupby("state")[["spending_usd", "quantity"]].sum())
''')


def power_bi_foundations():
    return [POWER_BI_START,
        m('''
        ## Interface

        Open a blank report. Identify the report canvas, the list of data fields, the visual
        building controls, the formatting controls and the Filters pane. Select a visual to
        change its fields or appearance. Click empty canvas before adding another visual.

        Report view is where we arrange charts. Table view lets us inspect rows and columns.
        Power Query is for preparing imported data; we need only a few type checks today.
        '''),
        m('''
        ## Importing data and field types

        1. Choose **Get data → Text/CSV** and select `amazon_monthly.csv`.
        2. Inspect the preview. Choose **Transform data** to check column types.
        3. Set `month` to Date; `spending_usd` to a decimal number; `quantity` to Whole number.
           Keep `state` and `category` as Text. Set `purchase_records` to Whole number.
        4. Leave the source rows unchanged. Apply the changes and load the table.
        5. Inspect a few rows. Explain why the same month and state appear several times.

        If dates or decimals import incorrectly, check the parsing locale rather than editing
        individual values. Keep spending, quantity and record counts distinct; no unique order count is available.
        '''),
        m('''
        ## Line chart

        A consumer researcher asks how monthly sample spending changed.

        1. Add a line chart. Put `month` on the horizontal axis and `spending_usd` on the vertical axis.
        2. Set the spending_usd aggregation to **Sum**.
        3. Use the Date field itself, not an unintended date hierarchy. Keep the year visible
           so January 2021 and January 2022 are distinct.
        4. Sort by month ascending. Label the value axis Sample spending (USD).
        5. Set the title to “Monthly sample spending”. Check the earliest and latest months.

        What would pooling all Januaries together change about this question?
        '''),
        m('''
        ## Bar chart

        Add a clustered bar chart with `state` as the category and **Sum of spending_usd** as
        the value. Sort by spending_usd descending. Start the value axis at zero and use a single
        colour. Label it “Sample spending by shipping state”. This compares full-period totals, not
        spending adjusted for population or sample size.

        Select a state. Notice that another chart may change in response. Clear the
        selection before comparing the all-data views. We will control these interactions later.
        '''),
        m('''
        ## Sum, average and count

        Duplicate the bar chart. Change the duplicate from Sum of spending_usd to Average, then
        Count. Sum adds monthly spending_usd. Average describes a mean aggregated row. Count counts
        monthly aggregate rows. Sum of purchase_records counts source records; none is a unique order count.
        Explain the units each version would need, then restore Sum.

        ## Labels and notes

        Use readable text and consistent USD formatting. Add a text note: “Berke et al., 2018–2022. Seven categories in donated Amazon histories. Monthly sample spending in USD.” If
        display units are millions, say so. Hover over a point to inspect its more precise value.

        Save the report locally as `course_purchases.pbix`. Keep it for the next two classes.
        No cloud publication or Power BI submission for credit is required.
        '''),
        m('''
        ## Exercise and project review

        Open [the exercises](exercises.ipynb). Briefly exchange a project outline and a figure:
        can your partner state the intended message and identify a useful numerical check?

        ## Optional Python check

        These totals should agree with Power BI after clearing all filters and selections.
        '''), POWER_BI_CHECK,
        m('''
        Reference: [Microsoft report-design walkthrough](https://microsoftlearning.github.io/PL-300-Microsoft-Power-BI-Data-Analyst/Instructions/Labs/08-design-power-bi-reports.html).
        '''),
    ]


def power_bi_comparisons():
    return [POWER_BI_START,
        m('''
        ## Tables

        Reopen `course_purchases.pbix` from the previous class. Add a new page called Comparisons.
        Insert a table containing `state`, **Sum of spending_usd** and **Sum of quantity**.
        Format spending_usd as USD, and check the totals against the all-data charts.
        Tables help readers retrieve exact values that a chart only approximates.
        '''),
        m('''
        ## Matrices

        Insert a matrix. Place `state` in Rows, `category` in Columns and
        **Sum of spending_usd** in Values. Show row totals, column totals and the grand total.
        Pick one cell and explain exactly which rows it summarises. Its row total should
        agree with the same state in the table when both have the same filters.
        '''),
        m('''
        ## Cards and KPIs

        Add cards showing **Sum of spending_usd** and **Sum of quantity**. A card displays a
        summary; a KPI adds a comparison with a defined goal. A large spending number alone
        does not tell us whether performance met a target.

        For a small KPI demonstration, assume a **hypothetical monthly sample-spending target of
        USD 100,000**. This is an invented classroom target, not a real business goal.
        Choose New measure and create each of these separately:

        ```dax
        Total sample spending = SUM(dashboard[spending_usd])
        ```

        ```dax
        Monthly classroom target = 100000
        ```

        First make a column chart with `month` and `Total sample spending`. Sort it by month
        ascending, then convert it to a KPI visual. Use `Total sample spending` as the indicator,
        `month` as the trend axis and `Monthly classroom target` as the target. Sort before
        conversion: the KPI visual has no sort control. Clear all filters.
        Check the latest month's value against the line chart. The KPI indicator concerns
        that latest month, whereas an unfiltered card sums the full period.

        Keep this demonstration on its own page. The fixed target is for the full selected sample;
        it is inappropriate for a filtered product or state unless a matching target is supplied.
        '''),
        m('''
        ## Filter levels

        Return to Comparisons. Try `category = Boots` at each level, one at a time:

        - **Visual filter:** changes only the selected table or chart.
        - **Page filter:** changes applicable visuals on the current page.
        - **Report filter:** applies across report pages.

        Clear each test filter before the next one. Keep an unfiltered copy of the report
        for comparison. Inspect the Filters pane when a total is unexpectedly different.
        '''),
        m('''
        ## Slicers

        Add slicers for `category` and `month` (Between mode for a date range). Try a single selection in each,
        then both together. The combined selection should restrict the data to rows meeting
        both conditions. Keep active selections visible. Clear both slicers and confirm
        that the original totals return.

        A slicer is an on-canvas filtering control. It is useful when readers need to make
        a frequent choice without opening the Filters pane.

        ## Exercise

        Open [the filtering exercises](exercises.ipynb). Save the report after clearing
        temporary filters. Keep the tables and cards for the dashboard-building class.
        '''),
        m('## Optional Python check'), POWER_BI_CHECK,
        c('''
        # Match the Boots/2022 slicer selection. Pandas combines row conditions
        # with & rather than Python's and; each condition needs parentheses.
        selected = dashboard.loc[(dashboard["category"] == "Boots") & (dashboard["month"].dt.year == 2022)]
        # Sum spending and quantity only for the selected category and year.
        print(selected[["spending_usd", "quantity"]].sum())
        # These all-category monthly totals check the unfiltered KPI, not the Boots selection.
        print(dashboard.groupby("month")["spending_usd"].sum().tail())
        '''),
        m('''
        References: [filters](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-add-filter),
        [slicers](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers),
        [KPIs](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-kpi).
        '''),
    ]


def power_bi_dashboard():
    return [POWER_BI_START,
        m('''
        ## Audience and question

        A consumer researcher wants to see how monthly sample spending changed and which states
        contributed most, with options to investigate categories and dates. Reopen the report
        from the previous class. Create a new page called Overview.

        We call this a dashboard in everyday language. In Power BI terminology we are
        building a Desktop **report page**, not a Service dashboard made of pinned tiles.
        '''),
        m('''
        ## Layout

        Sketch the page before moving visuals. Put the reader's question first, then the
        summary cards, monthly line and state bars. Place the category and date slicers
        where their selections remain visible. Keep the detailed matrix on a separate page.

        Copy the existing visuals to Overview. Align their edges and leave enough room for
        labels. Use consistent spending_usd units and colour meanings. Do not add another chart
        simply to fill space. The hypothetical KPI target from the previous class stays off
        this page because it is not valid for every filtered subset.
        '''),
        m('''
        ## Interactions

        Select a state bar and inspect the line and cards. Filtering removes other rows
        from a visual's calculation; highlighting can retain the full context while marking
        a subset. Choose the behaviour deliberately.

        In Desktop, select a source visual, then **Format → Edit interactions**. For this
        report, make the state bars filter the line and both cards. Make both slicers
        filter every main-page data visual. Test each source separately, then turn interaction
        editing off. Do not assume that every visual responds identically by default.
        '''),
        m('''
        ## Titles, notes and storytelling

        Use titles that remain true after filtering: “Monthly sample spending (USD)” and “Sample spending by
        state (USD)”. A fixed claim that one state is largest can become false after a
        selection. Label an all-data takeaway explicitly, or keep the title descriptive.

        Include a concise note: Berke et al., 2018–2022 donated histories, seven selected categories,
        monthly sample spending in USD, not representative of all shoppers. Keep selected categories and dates visible.
        Explain the main all-data pattern, then use one selection to answer a follow-up question.
        '''),
        m('''
        ## Checking filtered results

        Temporarily copy the exact-value table onto Overview. In Edit interactions, make
        both slicers and the state bars filter this checking table too. A table on
        another page does not automatically share this page's selections.

        1. Clear slicers, chart selections and page/report filters. Compare both cards with
           the corresponding totals in the table.
        2. Select a product, then a date range, then both. Reconcile cards, table and chart totals
           for each state. Allow for displayed rounding, not unexplained differences.
        3. Clear slicers, select one state, and check that the line and cards follow it.
        4. Check that dates remain chronological and titles still describe the selected data.
        5. Clear every selection and confirm that the starting totals return.

        After checking, remove only the temporary copy from Overview. Retain the original
        table on the checking page; apply matching filters there before future comparisons.
        '''),
        m('''
        ## Exercise

        Open [the dashboard exercise](exercises.ipynb). Let a partner use the report without
        explaining its controls. Revise one obstacle they encounter. Save `course_purchases.pbix`
        with the unfiltered Overview as the starting page. A screenshot can support discussion;
        no Service publishing or graded Power BI submission is required.

        ## Optional Python check
        '''), POWER_BI_CHECK,
        c('''
        # Match a California selection and a 2022 date filter in Power BI.
        selected = dashboard.loc[(dashboard["state"] == "CA") & (dashboard["month"].dt.year == 2022)]
        # Compare these selected totals with the filtered Power BI cards.
        print(selected[["spending_usd", "quantity"]].sum())
        # Add spending within each selected month to check the filtered line chart.
        print(selected.groupby("month")["spending_usd"].sum())
        '''),
        m('''
        Reference: [visual interactions](https://learn.microsoft.com/en-us/power-bi/create-reports/service-reports-visual-interactions).
        '''),
    ]


def power_bi_exercises(number):
    tasks = {
        4: '''
            ## Monthly spending and state comparison

            Work in your local Power BI report using `amazon_monthly.csv`. On a practice page,
            make a pie chart of monthly spending_usd and a line connecting state totals.
            A researcher asks how sample spending changed over time and which states contributed most.

            1. Explain how well each chart answers its question.
            2. Revise both charts, keeping data, aggregations and filters unchanged.
            3. Add readable titles, labels, units and a source note.
            4. Compare two values before and after. Check the full-period state total.

            Save your `.pbix`. In the Markdown cell below, explain one change and record
            the two numerical checks. This is ungraded practice.
        ''',
        5: '''
            ## Tables, cards and filters

            On a practice page, create a state table, a state-by-product matrix, a spending_usd
            card and category/date slicers. Start with all data.

            1. Record the spending_usd total. Apply a visual-only category filter to the card.
               Explain why the card and table no longer agree.
            2. Remove that filter. Select Boots and the date range 1 January–31 December 2022 in the slicers. Make the
               card, table and matrix reflect the same subset. Record the spending_usd total.
            3. Clear the slicers and confirm that the original value returns.
            4. Explain why the full-period card and latest-month KPI can differ without an error.
               Would the hypothetical sample target remain meaningful for Boots alone?

            Save the report. Add your checks and explanations below. Do not invent a product
            target to force a green KPI. This is ungraded practice.
        ''',
        6: '''
            ## Dashboard review

            Build an Overview page for a consumer researcher using your existing monthly line,
            state bars, spending/items cards and category/date slicers.

            1. Arrange the page so a new reader can identify its purpose without explanation.
            2. Add consistent labels, units and a concise figure note.
            3. Make slicers and state selections affect the intended visuals. Test all data,
               one product, one date range, both together, and one state.
            4. Ask a partner to answer the two business questions and return to the unfiltered
               view without help. Record one difficulty and revise it.
            5. Save the report with a clear starting state. Explain one layout change and
               record one filtered total that you checked against a table.

            All work stays in the local `.pbix`. No cloud publishing is required. This is
            ungraded practice; the final graded project remains a Python data story.
        ''',
    }
    return [m(tasks[number]), m('## Your explanation and checks\n\nAdd your answers here.')]
