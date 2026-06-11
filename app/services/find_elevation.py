from pathlib import Path

import rasterio

dir = Path(__file__).resolve().parents[2]
file_elevation = dir / "srtm_N55E160.tif"
def get_elevation(lon: float, lat: float):

    if not file_elevation.exists():
        raise FileNotFoundError(f"file not found {file_elevation}")
    
    with rasterio.open(file_elevation) as src:
        values = src.sample([(lon, lat)])
        for val in values:
            elevation = val[0]
            return elevation