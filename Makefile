web_root = public

pyfiles = coal/*.py

.PHONY: gallery
gallery: $(web_root)/index.html
$(web_root)/index.html: $(pyfiles) $(web_root)/tiles index.html.template style.css
	python -m coal.gallery
	cp style.css $(web_root)

$(web_root)/tiles: coal/config.py coal/tiles.py coal/mines.py
	python -m coal.tiles
	touch $(web_root)/tiles

.PHONY: clean
clean:
	rm -rf $(web_root)/*