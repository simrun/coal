from bs4 import BeautifulSoup

from . import config, mines, tiles

def add_tile(soup, mine, lazy=False):
    fig_tag = soup.new_tag("figure", id=mine["ENO"])

    img_tag = soup.new_tag("img", src=f"{tiles.path}/{mine['ENO']}.jpg")
    if lazy:
        img_tag["loading"] = "lazy"
    fig_tag.append(img_tag)

    caption_tag = soup.new_tag("figcaption")
    caption_tag.string = mine["Name"] + ", " + mine["State"]
    
    fig_tag.append(caption_tag)

    soup.find("main").append(fig_tag)

if __name__ == "__main__":
    with open("templates/index.html", "r") as f:
        soup = BeautifulSoup(f, features="html.parser")

    top_row = [334195, 335034, 334708]

    for ENO in top_row:
        mine = mines.coal_mines[mines.coal_mines["ENO"] == ENO].squeeze()
        add_tile(soup, mine)
    
    rest_of_mines = mines.coal_mines[~mines.coal_mines["ENO"].isin(top_row)]

    for _, mine in rest_of_mines.sort_values("Interest").iterrows():
        # Sorting gives us "High" interest mines first
        add_tile(soup, mine, lazy=True)
        
    with open(f"{config.web_root}/index.html", "w") as f:
        f.write(str(soup))