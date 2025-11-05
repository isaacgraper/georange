from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class GeoSet:
    """
    Represents a unified geographic entity extracted from heterogeneous spatial
    data sources.

    name  (str):   Identifier for the geographic feature or marker.
    desc  (str):   Optional textual description of the feature.
    coord (tuple): Immutable pair (latitude, longitude) in decimal degrees, following EPSG:4326 (WGS84) standard.
    """

    name: str
    desc: Optional[str]
    coord: Tuple[float, float]

    @property
    def lat(self) -> float:
        """
        Latitude component of the coordinate.
        """
        return self.coord[0]

    @property
    def lon(self) -> float:
        """
        Longitude component of the coordinate.
        """
        return self.coord[1]

    def __repr__(self):
        return f"GeoSet(name={self.name}, coord={self.coord})"
