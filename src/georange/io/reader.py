import logging
from pathlib import Path
from typing import Optional

from georange.io.files import kml
from georange.io.files.types import FileType

logger = logging.getLogger(__name__)


def read(source: str, engine=None, layer: Optional[str] = None):
    """
    Read different geospatial file formats into a GeoSet list.
    """
    src = Path(source)
    logger.info(f"Reading file from: {src}")

    if not src.exists():
        raise FileNotFoundError(f"File not found: {src}")

    fmt = src.suffix.lower()
    logger.info(f"Detected file format: {fmt}")

    supported_fmt = [ft.value for ft in FileType]
    if fmt not in supported_fmt:
        raise ValueError(f"Unsupported file format: {fmt}")

    if fmt == FileType.KML.value:
        try:
            logger.info(f"Reading from source: {src} with the following format: {fmt}")
            return kml.parse_kml(src)
        except Exception as e:
            logger.error(f"Failed to parse KML file: {src} | Error: {e}")
            raise

    raise ValueError(f"No parser implemented for extension: {fmt}")
