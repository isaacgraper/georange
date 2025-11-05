![Georange](https://raw.githubusercontent.com/isaacgraper/georange/main/images/cover.png)


<p align="center">
  <a href="https://github.com/isaacgraper/georange">
    <img src="https://img.shields.io/badge/georange-Homepage-blue?style=flat-square&logo=homebridge" alt="Homepage"/>
  </a>
  <a href="https://github.com/isaacgraper/georange/tree/main/docs">
    <img src="https://img.shields.io/badge/Docs-ReadTheDocs-orange?style=flat-square&logo=read-the-docs&logoColor=white" alt="Documentation"/>
  </a>
  <a href="https://pypi.org/project/georange/">
    <img src="https://img.shields.io/badge/PyPI-georange-red?style=flat-square&logo=pypi" alt="PyPI"/>
  </a>
  <a href="https://x.com/isaacgraper">
    <img src="https://img.shields.io/badge/Follow-@isaacgraper-1DA1F2?style=flat-square&logo=x&logoColor=white" alt="Twitter"/>
  </a>
  <a href="https://github.com/isaacgraper/georange/issues">
    <img src="https://img.shields.io/badge/Issues-GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="Issues"/>
  </a>
</p>

# What is Georange?

Georange is a lightweight, extensible geospatial analysis toolkit written in Python.

It acts as a wrapper layer around robust GIS libraries like geopy.

## Key Features

✅ Parse KML files into structured Python objects (GeoSet)
✅ Compute pairwise distances using accurate geodesic formulas (via geopy)
✅ Find nearest points between features
✅ Calculate average distances between all points
✅ Modular, testable CLI interface built with Typer

⚙️ Quick Start

1. Setup the development environment

Clone and install dependencies with Poetry:

```
git clone https://github.com/isaacgraper/georange.git
cd georange
make setup
```

If you already have everything incstalled:

`make dev`

2. Run the CLI

Show global help:

`poetry run python -m georange.main --help`

3. Parse a sample KML file

`poetry run python -m georange.main docs/samples/kml_file.kml analyze`

### Pairwise distances between all points
`poetry run python -m georange.main docs/samples/kml_file.kml distances`

### Find the nearest point to the first one
`poetry run python -m georange.main docs/samples/kml_file.kml nearest --target-index 0`

### Average distance across all features
`poetry run python -m georange.main docs/samples/kml_file.kml avgdist`

# Roadmap

- Add support for GeoJSON and Shapefiles
- Integrate Shapely for geometric operations (area, intersection)
- Implement plotting utilities with matplotlib and folium
- Export computed results to CSV/JSON
- Add optional REST API for remote analysis
