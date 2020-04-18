web_root = public

.PHONY: all
all: tiles gallery

.PHONY: tiles
tiles:
	mkdir -p $(web_root)
	python -m coal.tiles

.PHONY: gallery
gallery:
	mkdir -p $(web_root)

	python -m coal.gallery
	cp templates/style.css $(web_root)
	cp templates/about.html $(web_root)
	cp templates/coal-in-parliament.jpg $(web_root)

	cp data/operating_mines_feb2015.xlsx $(web_root)

.PHONY: clean
clean:
	rm -rf $(web_root)