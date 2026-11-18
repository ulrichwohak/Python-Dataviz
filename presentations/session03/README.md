# Mapping in Python

Lecture 3 · 18 November 2026

- [Presentation](vector-and-raster.pdf)
- [Lecture notebook](../../notebooks/03-mapping-in-python/lecture.ipynb)
- [In-class exercises](../../notebooks/03-mapping-in-python/exercises.ipynb)

The presentation starts with last week's chart redesign: the original pie charts,
anonymous student examples and two reference designs with labelled seasons. The line
chart shows monthly percentages within each footwear category; the paired bars show
purchase-record counts. The next examples invite discussion of visual design before
the introduction to mapping.

The Economist comparison appears in two steps on PDF pages 11–12: the original chart
first, then the redesign alongside it. The second view links to Sarah Leo's
[Mistakes, we've drawn a few](https://medium.com/the-economist/mistakes-weve-drawn-a-few-8cdd8a42d368).
Advance one page to reveal the second view.

The mapping introduction covers vector and raster data, coordinate reference systems,
projections and free sources of geographical data. A spherical diagram shows longitude
and latitude as angles, with 0° longitude explicitly labelled, before the CRS explanation.
The country-emissions analysis is in the notebook.

## Prepare the data

From the repository root, run:

```bash
uv sync
uv run python scripts/fetch_data.py
```

The preparation script creates both GeoJSON and shapefile versions of the country
boundaries, plus the emissions table. Keep the shapefile's companion files together.
See the [data documentation](../../data/README.md) for sources and preparation steps.

## Free geographical data

- [Natural Earth](https://www.naturalearthdata.com/): country boundaries and other base-map layers.
- [geoBoundaries](https://www.geoboundaries.org/): administrative boundaries.
- [Eurostat GISCO](https://ec.europa.eu/eurostat/web/gisco): European geographical datasets.
- [Geofabrik](https://download.geofabrik.de/): regional OpenStreetMap extracts.

Third-party figures retain their original credits and licences; see
[source acknowledgements](../../NOTICE.md#session-3-vector-and-raster-supplement).
