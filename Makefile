# OSM Images
# A easy way to use Github Raw to host images for OSM
# Github: https://www.github.com/0x4248/OSM_Images
# Licence: GNU General Public License v3.0
# By: 0x4248

python = python3
tools = tools

all: add

add:
	$(python) $(tools)/main.py
