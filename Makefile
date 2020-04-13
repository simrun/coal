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
	cp style.css $(web_root)

.PHONY: clean
clean:
	rm -rf $(web_root)