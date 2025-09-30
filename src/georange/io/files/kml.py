import xml.etree.ElementTree as ET
from pathlib import Path


def load(path: str | Path):
    """
    Load KML file and extract placemarks into a GeoDataFrame.
    """
    tree = ET.parse(path)
    root = tree.getroot()
    ns = {"kml": "http://www.opengis.net/kml/2.2"}

    placemarks = []

    for pm in root.findall(".//kml:Placemark", ns):
        name = pm.find("kml:name", ns)
        desc = pm.find("kml:description", ns)
        coords = pm.find(".//kml:coordinates", ns)

        if coords is not None:
            lon, lat, *_ = map(float, coords.text.strip().split(","))
            placemarks.append(
                {
                    "name": name.text if name is not None else "Unknown",
                    "description": desc.text if desc is not None else "",
                    "lat": lat if lat is not None else None,
                    "lon": lon if lon is not None else None,
                }
            )

    return placemarks
