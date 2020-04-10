import numpy as np
import pandas as pd

# ENO is the Entity Number defined by Geoscience Australia
mines = pd.read_excel("data/operating_mines_feb2015.xlsx", index_col=0)

for _, mine in mines.iterrows():
    print(mine.name, mine.loc["Longitude"], mine.loc["Latitude"])