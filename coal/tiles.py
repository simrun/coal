import os
import pathlib

import mercantile
import requests

from tqdm import tqdm

import mines

zoom = 10

path = f"tiles/{zoom}"
pathlib.Path(path).mkdir(parents=True, exist_ok=True)

def get_tile(long, lat, zoom):
    x, y, zoom = mercantile.tile(long, lat, zoom)

    base_path = "https://api.mapbox.com"
    format = "jpg90"
    tileset_id = "mapbox.satellite"
    token = os.getenv("MAPBOX_TOKEN")
    url = base_path + f"/v4/{tileset_id}/{zoom}/{x}/{y}@2x.{format}" + f"?access_token={token}"

    return requests.get(url).content

if __name__ == "__main__":
    for _, mine in tqdm(mines.coal_mines.iterrows(), total=len(mines.coal_mines)):
        # ENO is the Entity Number defined by Geoscience Australia
        ENO = mine["ENO"]
        long = mine["Longitude"]
        lat = mine["Latitude"]
        
        with open(f"{path}/{ENO}.jpg", "bw") as f:
            f.write(get_tile(long, lat, zoom))