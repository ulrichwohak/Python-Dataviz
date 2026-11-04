"""Archived synthetic redesign examples; not used by the current notebook generator.

The scheduled real-data exercises live in real_data_content.py and lecture_content.py.
"""

from textwrap import dedent


def code(source: str) -> str:
    return dedent(source).strip()


REDESIGN_ACTIVITIES = {
    1: {
        "title": "Weekly revenue",
        "brief": (
            "A commercial manager asks: **How did weekly revenue change during the first "
            "12 recorded weeks?** Run the supplied chart and decide how well it answers "
            "the question. Keep all 12 weeks and the same weekly totals."
        ),
        "prepare": code('''
            # Add up revenue across regions, products and channels for each week.
            weekly_redesign = (
                sales.dropna(subset=["revenue"])
                .groupby("date")["revenue"].sum().sort_index().head(12)
            )
            print(weekly_redesign)
        '''),
        "weak": code('''
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.pie(weekly_redesign, labels=weekly_redesign.index.strftime("%d %b"), autopct="%.1f%%")
            ax.set_title("Weekly revenue: first 12 recorded weeks")
            plt.show()
        '''),
        "prompt": (
            "1. What is difficult to see in the supplied chart?\n"
            "2. Copy the chart cell into the answer cell below and change it to make weekly "
            "changes easier to see. Keep the same `weekly_redesign` data in chronological order.\n"
            "3. Add a clear title, axis labels with units, and a short figure note: synthetic "
            "course data, weekly totals, missing revenue excluded.\n"
            "4. Check the first and last plotted values against the printed totals. "
            "Explain in one sentence why your chart helps the manager."
        ),
        "solution": code('''
            fig, ax = plt.subplots(figsize=(9, 4))
            ax.plot(weekly_redesign.index, weekly_redesign.values, marker="o")
            ax.set_title("How did weekly revenue change in the first 12 recorded weeks?", loc="left")
            ax.set_xlabel("Week")
            ax.set_ylabel("Total revenue (€)")
            fig.autofmt_xdate()
            fig.text(0.01, 0.01, "Synthetic course data. Weekly totals; rows with missing revenue excluded.")
            fig.tight_layout(rect=(0, 0.07, 1, 1))
            fig.savefig("figures/session01_redesign.png", dpi=150, bbox_inches="tight")
            plt.show()
        '''),
        "reason": (
            "The line puts dates in sequence and values on a shared scale. The points retain "
            "the 12 observed totals. Chronologically ordered bars could also work. A pie chart "
            "is not always wrong: it simply serves a different question here."
        ),
    },
    2: {
        "title": "A connected line suggests an order that regions do not have",
        "brief": (
            "A sales director asks: **Which regions have the highest total revenue?** "
            "Compare totals over the full dataset, not revenue per customer or per store. "
            "Keep the same regional totals in your redesign."
        ),
        "weak": code('''
            region_redesign = sales.dropna(subset=["revenue"]).groupby("region")["revenue"].sum()
            print(region_redesign)
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(region_redesign.index, region_redesign.values, marker="o")
            ax.set_title("Total revenue by region")
            ax.set_ylabel("Revenue (€)")
            plt.show()
        '''),
        "prompt": (
            "What does the connecting line suggest? Does alphabetical order help the ranking "
            "task? Redesign to make the ranking easy to read. Check that every region and its "
            "value are retained. Explain why a total does not measure performance adjusted "
            "for regional size."
        ),
        "solution": code('''
            ordered_regions = region_redesign.sort_values()
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.barh(ordered_regions.index, ordered_regions.values / 1_000_000)
            ax.set_title("Which regions contribute the largest revenue totals?", loc="left")
            ax.set_xlabel("Total revenue (€ million)")
            ax.set_xlim(left=0)
            fig.text(0.01, 0.01, "Synthetic course data. Full-period totals; missing revenue excluded; not size-adjusted.")
            fig.tight_layout(rect=(0, 0.07, 1, 1))
            fig.savefig("figures/session02_redesign.png", dpi=150, bbox_inches="tight")
            plt.show()
        '''),
        "reason": (
            "Ordered bars use aligned lengths and a zero baseline to show ranking. A sorted "
            "dot plot is another defensible choice. Removing the connecting line avoids "
            "suggesting a continuous path between unordered regions."
        ),
    },
    3: {
        "title": "Averages conceal the spread the reader needs",
        "brief": (
            "A customer analyst asks: **How much does income vary within each customer "
            "segment, and how much do the segments overlap?** A bar for each mean cannot "
            "answer this. Use the same customers with non-missing income."
        ),
        "weak": code('''
            income_redesign = customers.dropna(subset=["income", "segment"])
            print("Customers excluded:", len(customers) - len(income_redesign))
            print(income_redesign.groupby("segment")["income"].agg(["count", "mean", "median"]))
            mean_income = income_redesign.groupby("segment")["income"].mean()
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.bar(mean_income.index, mean_income.values)
            ax.set_title("Income by customer segment")
            ax.set_ylabel("Mean income (€)")
            plt.show()
        '''),
        "prompt": (
            "Which information has the mean discarded? Redesign to show within-segment "
            "variation on a common scale. Explain what a reader can now see. Say explicitly "
            "whether your chart shows variation among customers or uncertainty about a mean."
        ),
        "solution": code('''
            import seaborn as sns

            fig, ax = plt.subplots(figsize=(8, 4))
            sns.boxplot(data=income_redesign, x="segment", y="income", color="#9DBFCA", ax=ax)
            ax.set_title("How much do income distributions overlap across segments?", loc="left")
            ax.set_xlabel("Customer segment")
            ax.set_ylabel("Income (€)")
            fig.text(0.01, 0.01, "Synthetic course data. Box: middle 50%; line: median; whiskers: within 1.5 IQR; points: beyond.")
            fig.tight_layout(rect=(0, 0.07, 1, 1))
            fig.savefig("figures/session03_redesign.png", dpi=150, bbox_inches="tight")
            plt.show()
        '''),
        "reason": (
            "The boxes show spread and overlap rather than only a centre. These are "
            "distributions of customer values, not confidence intervals for means. Small "
            "multiple histograms with common bins and scales are also appropriate."
        ),
    },
}
