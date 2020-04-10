import os
import pathlib

import numpy as np
import pandas as pd

from tqdm import tqdm

import tiles

# ENO is the Entity Number defined by Geoscience Australia
mines = pd.read_excel("data/operating_mines_feb2015.xlsx")

for _, mine in tqdm(mines.iterrows(), total=len(mines)):
    ENO = mine.loc["ENO"]
    long = mine.loc["Longitude"]
    lat = mine.loc["Latitude"]
    zoom = 14

    path = f"tiles/{zoom}/"
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    
    with open(f"{path}{ENO}.jpg", "bw") as f:
        f.write(tiles.get_tile(long, lat, zoom))
