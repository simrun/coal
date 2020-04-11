import os
import pathlib

import numpy as np
import pandas as pd

from tqdm import tqdm

import tiles

mines = pd.read_excel("data/operating_mines_feb2015.xlsx")
coal_mines = mines.loc[mines["Commodities"].str.contains("coal", case=False)]

for _, mine in tqdm(coal_mines.iterrows(), total=len(coal_mines)):
    # ENO is the Entity Number defined by Geoscience Australia
    ENO = mine.loc["ENO"]
    long = mine.loc["Longitude"]
    lat = mine.loc["Latitude"]
    zoom = 10

    path = f"tiles/{zoom}/"
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    
    with open(f"{path}{ENO}.jpg", "bw") as f:
        f.write(tiles.get_tile(long, lat, zoom))
