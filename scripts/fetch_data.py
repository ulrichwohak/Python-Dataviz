"""Download public sources and prepare local teaching tables.

First run downloads about 330 MB; later runs use checksum-verified caches.
No credentials are needed. Notebooks themselves make no network requests.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
import shutil
import sys
import urllib.request
from pathlib import Path

import geopandas as gpd
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dataviz_course.synthetic_data import make_simpson_hotels  # noqa: E402

RAW = ROOT / "data/raw"
OUT = ROOT / "data/processed"
CACHE = RAW / "sources"
SOURCES = {
    "amazon-purchases.csv": (
        "https://dataverse.harvard.edu/api/access/datafile/7616235",
        "6efb098a6e01a9acb6e215402a450f4a848ed1b102ca016f9be6c4f03c585e1e"),
    "births.csv": (
        "https://raw.githubusercontent.com/fivethirtyeight/data/4c1ff5e3aef1816ae04af63218015066e186c147/births/US_births_2000-2014_SSA.csv",
        "67ed396cecc999664a737ee75f287cf3472e24c3257fcca795b672579f0ed910"),
    "co2.csv": (
        "https://raw.githubusercontent.com/owid/co2-data/382ee6c662b0ece26e111f263b44c029afad7787/owid-co2-data.csv",
        "7f78e2b218ce4bb8c538bbec04fdc9a7982e8d40bff972e650df603899edd5f6"),
    "countries.geojson": (
        "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/v5.1.2/geojson/ne_110m_admin_0_countries.geojson",
        "6866c877d39cba9c357620878839b336d569f8c662d3cfab4cb1dbe2d39c977f"),
    "did-basics.html": (
        "https://raw.githubusercontent.com/bcallaway11/did/9ead26b9d37c7f2bc202bebc4f5e8220ab7e8c13/docs/articles/did-basics.html",
        "89f1982bc840fb8f51316f437037d1933f7859ca1e524510e3cad7026e31c574"),
}
CATEGORIES = {
    "ABIS_BOOK": "Books", "PET_FOOD": "Pet food", "GIFT_CARD": "Gift cards",
    "SHIRT": "Shirts", "HEADPHONES": "Headphones", "BOOT": "Boots", "SANDAL": "Sandals",
}


def checksum(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def download(name, url, expected):
    path = CACHE / name
    if path.exists():
        if checksum(path) != expected:
            raise ValueError(f"Checksum mismatch in {path}. Move it aside and rerun; no data substituted.")
        print(f"Cached: {name}", flush=True)
        return path
    print(f"Downloading: {name}", flush=True)
    temporary = path.with_suffix(path.suffix + ".partial")
    request = urllib.request.Request(url, headers={"User-Agent": "CEU-Dataviz-Course/1.0"})
    with urllib.request.urlopen(request, timeout=180) as response, temporary.open("wb") as stream:
        shutil.copyfileobj(response, stream)
    if checksum(temporary) != expected:
        raise ValueError(f"Unexpected source version for {name}; kept {temporary} for inspection.")
    temporary.replace(path)
    return path


def prepare_amazon():
    rename = {"Order Date": "date", "Purchase Price Per Unit": "unit_price_usd",
              "Quantity": "quantity", "Shipping Address State": "state", "Category": "category"}
    source = pd.read_csv(CACHE / "amazon-purchases.csv", usecols=list(rename)).rename(columns=rename)
    source["date"] = pd.to_datetime(source["date"], errors="raise")
    in_period = source["date"].between("2018-01-01", "2022-12-31")
    selected = source["category"].isin(CATEGORIES)
    valid = (source["unit_price_usd"] > 0) & (source["quantity"] > 0)
    purchases = source.loc[in_period & selected & valid].copy()
    purchases["category"] = purchases["category"].map(CATEGORIES)
    purchases["state"] = purchases["state"].fillna("Unknown")
    purchases["spending_usd"] = (purchases["unit_price_usd"] * purchases["quantity"]).round(2)
    purchases = purchases.sort_values(["date", "category", "state"], kind="stable")
    purchases.to_csv(RAW / "amazon_purchases.csv", index=False)
    purchases["month"] = purchases["date"].dt.to_period("M").dt.to_timestamp()
    dashboard = purchases.groupby(["month", "state", "category"], as_index=False).agg(
        spending_usd=("spending_usd", "sum"), quantity=("quantity", "sum"),
        purchase_records=("spending_usd", "size"))
    dashboard["quantity"] = dashboard["quantity"].astype(int)
    dashboard.to_csv(OUT / "amazon_monthly.csv", index=False)
    assert abs(dashboard.spending_usd.sum() - purchases.spending_usd.sum()) < 0.01
    assert dashboard.purchase_records.sum() == len(purchases)
    return {"source_rows": len(source), "outside_2018_2022": int((~in_period).sum()),
            "selected_categories": CATEGORIES, "extract_rows": len(purchases),
            "missing_state_in_extract": int((purchases.state == "Unknown").sum()),
            "invalid_price_quantity_in_selected_period": int((in_period & selected & ~valid).sum()),
            "monthly_rows": len(dashboard), "spending_usd": float(purchases.spending_usd.sum())}


def prepare_births():
    births = pd.read_csv(CACHE / "births.csv")
    births["date"] = pd.to_datetime(dict(year=births.year, month=births.month, day=births.date_of_month))
    assert len(births) == 5479 and births.date.is_unique
    assert (births.day_of_week == births.date.dt.dayofweek + 1).all()
    births["weekday"] = births.date.dt.day_name()
    births[["date", "year", "month", "day_of_week", "weekday", "births"]].to_csv(RAW / "us_births.csv", index=False)
    return {"rows": len(births), "start": str(births.date.min().date()), "end": str(births.date.max().date())}


def prepare_maps():
    countries = gpd.read_file(CACHE / "countries.geojson")
    # ISO_A3_EH includes France and Norway, which have -99 in ISO_A3 in this release.
    non_iso = countries["ISO_A3_EH"] == "-99"
    countries.loc[non_iso, "ISO_A3_EH"] = "NE_" + countries.loc[non_iso, "ADM0_A3"]
    countries = countries[["ISO_A3_EH", "ADMIN", "geometry"]].rename(
        columns={"ISO_A3_EH": "iso_code", "ADMIN": "map_name"})
    countries = countries.loc[countries.iso_code != "ATA"].copy()
    assert countries.iso_code.is_unique
    countries.to_file(RAW / "countries.geojson", driver="GeoJSON")
    emissions = pd.read_csv(CACHE / "co2.csv")
    fields = ["country", "iso_code", "year", "population", "co2", "co2_per_capita",
              "consumption_co2", "consumption_co2_per_capita"]
    snapshot = emissions.loc[(emissions.year == 2023) & emissions.iso_code.isin(countries.iso_code), fields]
    assert snapshot.iso_code.is_unique
    snapshot.to_csv(RAW / "co2_2023.csv", index=False)
    return {"map_rows": len(countries), "emissions_rows": len(snapshot),
            "unmatched_map_codes": sorted(set(countries.iso_code) - set(snapshot.iso_code))}


def prepare_event_study():
    # Extract the published real-data mw.dyn output, not the earlier simulated example.
    page = html.unescape(re.sub(r"<[^>]+>", "", (CACHE / "did-basics.html").read_text()))
    table = page.split('aggte(MP = mw.attgt, type = "dynamic")', 1)[1]
    table = table.split("Dynamic Effects:", 1)[1].split("#> ---", 1)[0]
    rows = re.findall(r"#>\s+(-?\d+)\s+(-?\d+\.\d+)\s+(\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)", table)
    results = pd.DataFrame(rows, columns=["event_year", "estimate", "std_error", "ci_low", "ci_high"]).astype(float)
    results["event_year"] = results.event_year.astype(int)
    assert results.event_year.tolist() == list(range(-3, 4))
    assert (results.ci_low < results.estimate).all() and (results.estimate < results.ci_high).all()
    results.to_csv(OUT / "event_study_results.csv", index=False)
    return {"rows": len(results), "source_output": "summary(mw.dyn)",
            "intervals": "published 95% simultaneous confidence bands", "units": "log employment"}


def main():
    for folder in [RAW, OUT, CACHE, ROOT / "figures"]:
        folder.mkdir(parents=True, exist_ok=True)
    for name, (url, expected) in SOURCES.items():
        download(name, url, expected)
    report = {"amazon": prepare_amazon(), "births": prepare_births(),
              "mapping": prepare_maps(), "event_study": prepare_event_study()}
    make_simpson_hotels().to_csv(RAW / "simpson_hotels.csv", index=False)
    report["sources"] = {name: {"url": url, "sha256": digest} for name, (url, digest) in SOURCES.items()}
    (OUT / "preparation_report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "sources"}, indent=2))
    print("Prepared local course data. See data/README.md for sources and limitations.")


if __name__ == "__main__":
    main()
