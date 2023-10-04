"""Render GPX waypoints/tracks into a shapely BaseGeometry"""

from shapely.geometry import Point, LineString

def gpx2geometry(gpx):
    """
    Convert GPX waypoint and track data to a list of Points and LineStrings
    """
    def _line(track):
        path = []
        for segment in track.segments:
            path += [(p.longitude, p.latitude) for p in segment.points]
        return LineString(path)

    points = [Point(wp.longitude, wp.latitude) for wp in gpx.waypoints]
    lines = [_line(track) for track in gpx.tracks]
    return points, lines
