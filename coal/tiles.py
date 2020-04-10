import os

import mercantile
import requests

def get_tile(long, lat, zoom):
    x, y, zoom = mercantile.tile(long, lat, zoom)

    base_path = "https://api.mapbox.com"
    format = "jpg90"
    tileset_id = "mapbox.satellite"
    token = os.getenv("MAPBOX_TOKEN")
    url = base_path + f"/v4/{tileset_id}/{zoom}/{x}/{y}@2x.{format}" + f"?access_token={token}"

    return requests.get(url).content