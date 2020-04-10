import os

import mercantile
import requests

x, y, zoom = mercantile.tile(121.1725, -30.9736, 16)

base_path = "https://api.mapbox.com"
format = "jpg90"
tileset_id = "mapbox.satellite"
token = os.getenv("MAPBOX_TOKEN")
url = base_path + f"/v4/{tileset_id}/{zoom}/{x}/{y}@2x.{format}" + f"?access_token={token}"

with open("tiles/tile.jpg", "bw") as f:
    f.write(requests.get(url).content)