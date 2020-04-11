import shutil

from bs4 import BeautifulSoup

import mines, tiles

if __name__ == "__main__":
    gallery_file = "index.html"
    shutil.copyfile("index.html.template", gallery_file)

    with open(gallery_file, "r") as f:
        gallery_soup = BeautifulSoup(f)

    for _, mine in mines.coal_mines.iterrows():
        ENO = mine["ENO"]
        img_tag = gallery_soup.new_tag("img", src=f"{tiles.path}/{ENO}.jpg")
        gallery_soup.body.append(img_tag)

    with open(gallery_file, "w") as f:
        f.write(gallery_soup.prettify())