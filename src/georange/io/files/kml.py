import xml.etree.ElementTree as ET
from pathlib import Path

from georange.models import GeoSet


def parse_kml(path: str | Path) -> GeoSet:
    """
    Load KML file and extract placemarks into a GeoSet.
    """
    tree = ET.parse(path)
    root = tree.getroot()
    ns = {"kml": "http://www.opengis.net/kml/2.2"}

    geoset = []

    for pm in root.findall(".//kml:Placemark", ns):
        name = pm.find("kml:name", ns)
        desc = pm.find("kml:description", ns)
        coords = pm.find(".//kml:coordinates", ns)

        if coords is not None:
            lon, lat, *_ = map(float, coords.text.strip().split(","))
            geoset.append(
                GeoSet(
                    name=name.text if name is not None else "Unknown",
                    desc=desc.text if desc is not None else None,
                    coord=(lat, lon),
                )
            )

    return geoset
