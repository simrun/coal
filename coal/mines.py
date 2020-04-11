import numpy as np
import pandas as pd

mines = pd.read_excel("data/operating_mines_feb2015.xlsx")
coal_mines = mines.loc[mines["Commodities"].str.contains("coal", case=False)]