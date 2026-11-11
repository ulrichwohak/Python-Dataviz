"""Prepare the local OLS illustrations from donated footwear purchases and NOAA data."""

from __future__ import annotations

import hashlib
import json
import re
import urllib.error
import urllib.request

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

NOAA_BASE = "https://www.ncei.noaa.gov/monitoring-content/data/us/climdiv/monthly/current/"
NOAA_RELEASE = "climdiv-tmpcst-v1.0.0-20261105"
WEATHER_SHA256 = "b563fa2b9fc15929878ead9116e3dec57e6fd53d082c665a5618b48a54b5afb9"
# NOAA state codes, in order 001-050; these are not FIPS codes.
# Source: NOAA's state-readme.txt, STATE CODE TABLE.
NOAA_STATES = (
    "AL AZ AR CA CO CT DE FL GA ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT "
    "NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY HI AK"
).split()


def temperature_extract(data: bytes) -> pd.DataFrame:
    """Parse NOAA's fixed-width, statewide average temperatures for 2018-2022."""
    rows = []
    for line in data.decode("ascii").splitlines():
        state_code, year = int(line[:3]), int(line[6:10])
        if not (1 <= state_code <= 50 and 2018 <= year <= 2022):
            continue
        if line[3:6] != "002":
            raise ValueError("Expected statewide mean-temperature records, element 02.")
        for month in range(1, 13):
            value = float(line[10 + 7 * (month - 1):10 + 7 * month])
            if not -50 <= value <= 140:
                raise ValueError("Missing or invalid NOAA temperature in the teaching period.")
            rows.append((NOAA_STATES[state_code - 1], year, month, value))
    result = pd.DataFrame(rows, columns=["state", "year", "month", "temperature_f"])
    result = result.sort_values(["state", "year", "month"]).reset_index(drop=True)
    if len(result) != 3000 or result.duplicated(["state", "year", "month"]).any():
        raise ValueError("Expected 50 states × 5 years × 12 unique monthly temperatures.")
    return result


def _read_url(url):
    request = urllib.request.Request(url, headers={"User-Agent": "CEU-Dataviz-Course/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def prepare_temperature(cache, out):
    """Pin the values used in class even if NOAA rotates its dated full-history file."""
    path = cache / "noaa-state-temperature-2018-2022.csv"
    provenance = cache / "noaa-state-temperature-source.json"
    if not path.exists():
        url = NOAA_BASE + NOAA_RELEASE
        try:
            data = _read_url(url)
        except urllib.error.HTTPError as exc:
            if exc.code != 404:
                raise
            release = _read_url(NOAA_BASE + "procdate.txt").decode("ascii").strip()
            if not re.fullmatch(r"\d{8}", release):
                raise ValueError("Unexpected NOAA release date.") from exc
            url = NOAA_BASE + f"climdiv-tmpcst-v1.0.0-{release}"
            data = _read_url(url)
        weather = temperature_extract(data)
        payload = weather.to_csv(index=False, float_format="%.2f").encode()
        if hashlib.sha256(payload).hexdigest() != WEATHER_SHA256:
            raise ValueError("NOAA's 2018-2022 temperatures changed; review before replacing them.")
        path.write_bytes(payload)
        provenance.write_text(json.dumps({"url": url, "download_sha256": hashlib.sha256(data).hexdigest()}, indent=2) + "\n")
    if hashlib.sha256(path.read_bytes()).hexdigest() != WEATHER_SHA256:
        raise ValueError("Checksum mismatch in the cached NOAA teaching extract.")
    weather = pd.read_csv(path)
    weather["temperature_c"] = (weather["temperature_f"] - 32) * 5 / 9
    weather.to_csv(out / "state_month_temperature.csv", index=False)
    return weather, {"extract_sha256": WEATHER_SHA256, **json.loads(provenance.read_text())}


def _coefficient(model, term):
    interval = model.conf_int(alpha=0.05).loc[term]
    return {"estimate": float(model.params[term]), "std_error": float(model.bse[term]),
            "ci_low": float(interval.iloc[0]), "ci_high": float(interval.iloc[1])}


def prepare_footwear_models(purchases, cache, out):
    """Fit OLS; export aggregate estimates and an anonymous weather-matched extract."""
    footwear = purchases.loc[purchases["category"].isin(["Boots", "Sandals"])].copy()
    if footwear["participant_id"].isna().any():
        raise ValueError("Participant identifiers are required for clustered standard errors.")
    footwear["year"] = footwear["date"].dt.year
    footwear["month"] = footwear["date"].dt.month
    weather, provenance = prepare_temperature(cache, out)
    joined = footwear.merge(weather, on=["state", "year", "month"], how="left", validate="many_to_one")
    matched = joined.loc[joined["temperature_c"].notna()].copy()
    # Outcome is 0 or 100: coefficients are percentage points, not percent changes.
    matched["boot_percent"] = matched["category"].eq("Boots").astype(int) * 100
    matched["temperature_10c"] = matched["temperature_c"] / 10
    clusters = np.column_stack([pd.factorize(matched["participant_id"])[0],
                               pd.factorize(matched["state"])[0]])
    base = "boot_percent ~ temperature_10c + C(state) + C(year)"
    weather_rows = []
    for label, formula in [("State and year", base), ("Also calendar month", base + " + C(month)")]:
        model = smf.ols(formula, data=matched, missing="raise").fit(
            cov_type="cluster", cov_kwds={"groups": clusters, "use_correction": True, "df_correction": True}, use_t=True)
        weather_rows.append({"model": label, **_coefficient(model, "temperature_10c")})
    weather_coefficients = pd.DataFrame(weather_rows)
    if not np.isfinite(weather_coefficients.select_dtypes("number")).all().all():
        raise ValueError("Non-finite weather coefficient or interval.")
    weather_coefficients.to_csv(out / "footwear_weather_coefficients.csv", index=False)
    matched.drop(columns="participant_id").to_csv(out / "footwear_weather.csv", index=False)

    # Preserve all boot purchases, including those without weather matches.
    boots = footwear.loc[footwear["category"].eq("Boots")].copy()
    price_formula = "unit_price_usd ~ C(month, Treatment(reference=1)) + C(year) + C(state)"
    price_model = smf.ols(price_formula, data=boots, missing="raise").fit(
        cov_type="cluster", cov_kwds={"groups": boots["participant_id"], "use_correction": True, "df_correction": True}, use_t=True)
    price_rows = [{"month": month, **_coefficient(price_model, f"C(month, Treatment(reference=1))[T.{month}]")}
                  for month in range(2, 13)]
    pd.DataFrame(price_rows).to_csv(out / "boot_month_coefficients.csv", index=False)
    # The June-August average is a pre-specified contrast, not a selected significant month.
    summer = np.zeros(len(price_model.params))
    for month in (6, 7, 8):
        summer[price_model.params.index.get_loc(f"C(month, Treatment(reference=1))[T.{month}]")] = 1 / 3
    contrast = price_model.t_test(summer)
    summer_interval = contrast.conf_int()[0]
    summer_result = {"estimate": float(contrast.effect.item()), "ci_low": float(summer_interval[0]), "ci_high": float(summer_interval[1])}
    pd.DataFrame([summer_result]).to_csv(out / "boot_summer_contrast.csv", index=False)
    report = {
        "footwear_rows": len(footwear), "weather_matched_rows": len(matched),
        "weather_exclusions_by_state": joined.loc[joined.temperature_c.isna(), "state"].value_counts().to_dict(),
        "weather_participants": matched.participant_id.nunique(), "weather_states": matched.state.nunique(),
        "weather_formulas": [base, base + " + C(month)"],
        "weather_clustering": "participant and state (two-way)", "weather_t_df": int(model.df_resid_inference),
        "boot_rows": len(boots), "boot_participants": boots.participant_id.nunique(),
        "price_formula": price_formula, "price_clustering": "participant", "price_t_df": int(price_model.df_resid_inference),
        "intervals": "95% pointwise, finite-sample cluster corrections; not simultaneous bands",
        "summer_vs_january": summer_result,
        "weather_source": provenance,
    }
    (out / "footwear_model_details.json").write_text(json.dumps(report, indent=2) + "\n")
    return report
