import numpy as np
import pandas as pd

mines = pd.read_excel("data/operating_mines_feb2015.xlsx")
coal_mines = mines[mines["Commodities"].str.contains("coal", case=False)]

curation = pd.read_csv("curation.csv")
coal_mines = pd.merge(coal_mines, curation, how='left', on="ENO", validate="1:1")

coal_mines = coal_mines[coal_mines["Interest"].isin({"High", "Med"})]
coal_mines = coal_mines[coal_mines["Dupe"] != "Yes"]