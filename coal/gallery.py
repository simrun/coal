from bs4 import BeautifulSoup

from . import config, mines, tiles

def add_tile(soup, mine):
    ENO = mine["ENO"]
    img_tag = soup.new_tag("img", src=f"{tiles.path}/{ENO}.jpg")
    soup.find("main").append(img_tag)

if __name__ == "__main__":
    with open("templates/index.html", "r") as f:
        soup = BeautifulSoup(f, features="html.parser")

    top_row = [334195, 333791, 333502]

    for ENO in top_row:
        mine = mines.coal_mines[mines.coal_mines["ENO"] == ENO].squeeze()
        add_tile(soup, mine)
    
    rest_of_mines = mines.coal_mines[~mines.coal_mines["ENO"].isin(top_row)]

    for _, mine in rest_of_mines.sort_values("Interest").iterrows():
        # Sorting gives us "High" interest mines first
        add_tile(soup, mine)
        
    with open(f"{config.web_root}/index.html", "w") as f:
        f.write(soup.prettify())