include .env
export MAPBOX_TOKEN

pyfiles = coal/*.py

.PHONY: gallery
gallery: index.html
index.html: $(pyfiles) tiles index.html.template
	python -m coal.gallery

tiles: coal/tiles.py coal/mines.py
	python -m coal.tiles
	touch tiles

.PHONY: clean
clean:
	rm -rf tiles index.html