import logging
from pathlib import Path
from typing import Optional

from georange.io.files import kml
from georange.io.files.types import FileType

logger = logging.getLogger(__name__)


def read(source: str, engine=None, layer: Optional[str] = None):
    """
    Read different geospatial file formats into a GeoDataFrame.
    """
    if engine is not None:
        pass

    src = Path(source) if "://" not in source else None
    logger.info(f"Reading file from source: {src}")

    fmt = src.suffix.lower()
    logger.info(f"File format detected: {fmt}")

    if fmt not in FileType.name:
        raise ValueError(f"Unsupported file format: {fmt}")

    if src is not None and src.exists():
        ext = src.suffix.lower()
        logger.info(f"Detected file extension: {ext}")

        # Add support for more file types as needed
        if ext == ".kml":
            return kml.load(src)

        raise ValueError(f"Unsupported extension: {ext}")
