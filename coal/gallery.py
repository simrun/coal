from bs4 import BeautifulSoup

from . import config, mines, tiles

if __name__ == "__main__":
    with open("templates/index.html", "r") as f:
        soup = BeautifulSoup(f, features="html.parser")

    for _, mine in mines.coal_mines.sort_values("Interest").iterrows():
        # Sorting gives us "High" interest mines first
        ENO = mine["ENO"]
        img_tag = soup.new_tag("img", src=f"{tiles.path}/{ENO}.jpg")
        soup.find("main").append(img_tag)

    with open(f"{config.web_root}/index.html", "w") as f:
        f.write(soup.prettify())