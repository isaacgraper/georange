from enum import Enum


class FileType(str, Enum):
    """
    Different type formats that can be converted into a GeoSet.
    """

    KML = (".kml",)
