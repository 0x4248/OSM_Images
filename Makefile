# OSM Images
# A easy way to use Github Raw to host images for OSM
# Github: https://www.github.com/lewisevans2007/OSM_Images
# Licence: GNU General Public License v3.0
# By: Lewis Evans

python = python3

all: add

add:
	$(python) tools/main.py
