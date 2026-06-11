from shapely import wkt
from shapely.geometry import Point, LineString
from app.services.find_elevation import get_elevation


def format_number(value: float):
    if float(value).is_integer():
        return str(int(value))

    return str(value)

def add_elevation_to_wkt(wkt_text: str):
    try:
        #figure = POINT либо LINESTRING
        figure = wkt.loads(wkt_text)
    except Exception:
        raise ValueError("Invalid WKT")

    if isinstance(figure, Point):
        return add_elevation_to_point(figure)

    if isinstance(figure, LineString):
        return add_elevation_to_linestring(figure)

    raise ValueError("Only POINT and LINESTRING are supported now")


def add_elevation_to_point(point: Point):
    lon = point.x
    lat = point.y
    elevation = get_elevation(lon, lat)

    return (
        f"POINT("
        f"{format_number(lon)} "
        f"{format_number(lat)} "
        f"{format_number(elevation)}"
        f")"
    )


def add_elevation_to_linestring(line: LineString):
    points_with_elevation = []
    #для каждой точки вызываем get_elevation
    for lon, lat in line.coords:
        elevation = get_elevation(lon, lat)

        point_text = (
            f"{format_number(lon)} "
            f"{format_number(lat)} "
            f"{format_number(elevation)}"
        )

        points_with_elevation.append(point_text)

    return f"LINESTRING({', '.join(points_with_elevation)})"