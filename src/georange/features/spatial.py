from collections.abc import Sequence

from geopy.distance import geodesic

from georange.models.geoset import GeoSet


def distance(p1: GeoSet, p2: GeoSet) -> float:
    """
    Returns the geodesic distance between two points in kilometers.
    """

    # can be changed in the future for differents unit of measurement
    return geodesic(p1.coord, p2.coord).km


def nearest_point(points: Sequence[GeoSet], target: GeoSet) -> GeoSet:
    """
    Returns the point nearest to the target.
    """
    return min(points, key=lambda p: distance(p, target))


def average_distance(points: Sequence[GeoSet]) -> float:
    """
    Calculates the average pairwise distance between all points.
    """
    if len(points) < 2:
        return 0.0

    dists = [distance(a, b) for i, a in enumerate(points) for b in points[i + 1 :]]
    return sum(dists) / len(dists)
