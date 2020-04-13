from bs4 import BeautifulSoup

from . import config, mines, tiles

if __name__ == "__main__":
    with open("templates/index.html", "r") as f:
        soup = BeautifulSoup(f, features="html.parser")

    for _, mine in mines.coal_mines.iterrows():
        ENO = mine["ENO"]
        img_tag = soup.new_tag("img", src=f"{tiles.path}/{ENO}.jpg")
        soup.body.find(id="tiles").append(img_tag)

    soup.body.h1.string = str(len(mines.coal_mines)) + " Australian coal mines"

    with open(f"{config.web_root}/index.html", "w") as f:
        f.write(soup.prettify())