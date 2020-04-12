web_root = public

pyfiles = coal/*.py

.PHONY: gallery
gallery: $(web_root)/index.html
$(web_root)/index.html: $(pyfiles) $(web_root)/tiles index.html.template
	python -m coal.gallery

$(web_root)/tiles: coal/config.py coal/tiles.py coal/mines.py
	python -m coal.tiles
	touch $(web_root)/tiles

.PHONY: clean
clean:
	rm -rf $(web_root)/tiles $(web_root)/index.html