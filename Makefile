include .env
export MAPBOX_TOKEN

pyfiles = coal/*.py

.PHONY: gallery
gallery: index.html
index.html: $(pyfiles) tiles
	python -m coal.gallery

tiles: $(pyfiles)
	python -m coal.tiles
	touch tiles

.PHONY: clean
clean:
	rm -rf tiles index.html