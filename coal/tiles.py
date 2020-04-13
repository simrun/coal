import os
import pathlib

import mercantile
import requests

from tqdm import tqdm

from . import config, mines

zoom = 11
path = f"tiles/{zoom}"

def get_tile(long, lat, zoom):
    x, y, zoom = mercantile.tile(long, lat, zoom)

    base_path = "https://api.mapbox.com"
    format = "jpg90"
    tileset_id = "mapbox.satellite"
    token = os.getenv("MAPBOX_TOKEN")
    url = base_path + f"/v4/{tileset_id}/{zoom}/{x}/{y}@2x.{format}" + f"?access_token={token}"

    response = requests.get(url)
    response.raise_for_status()

    return response.content

if __name__ == "__main__":
    pathlib.Path(f"{config.web_root}/{path}").mkdir(parents=True, exist_ok=True)
    for _, mine in tqdm(mines.coal_mines.iterrows(), total=len(mines.coal_mines)):
        # ENO is the Entity Number defined by Geoscience Australia
        ENO = mine["ENO"]
        long = mine["Longitude"]
        lat = mine["Latitude"]
        
        with open(f"{config.web_root}/{path}/{ENO}.jpg", "bw") as f:
            f.write(get_tile(long, lat, zoom))