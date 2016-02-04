#!/usr/bin/python


import tempfile
import urllib2
import json

from io import BytesIO
from time import strptime, strftime, sleep
from os import system
from os.path import expanduser

from PIL import Image

from AppKit import NSWorkspace, NSScreen
from Foundation import NSURL

# Configuration
# =============

# Increases the quality and the size. Possible values: 4, 8, 16, 20
level = 4

# ==============================================================================

def main():
    width = 550
    height = 550

    print("Updating...")
    j = urllib2.urlopen("http://himawari8-dl.nict.go.jp/himawari8/img/D531106/latest.json")
    latest = strptime(json.load(j)["date"], "%Y-%m-%d %H:%M:%S")

    print("Latest version: {} GMT\n".format(strftime("%Y/%m/%d/%H:%M:%S", latest)))

    url_format = "http://himawari8.nict.go.jp/img/D531106/{}d/{}/{}_{}_{}.png"

    png = Image.new('RGB', (width*level, height*level))

    print("Downloading tiles: 0/{} completed".format(level*level))
    for x in range(level):
        for y in range(level):
            tile_w = urllib2.urlopen(url_format.format(level, width, strftime("%Y/%m/%d/%H%M%S", latest), x, y))
            tiledata = tile_w.read()

            tile = Image.open(BytesIO(tiledata))
            png.paste(tile, (width*x, height*y, width*(x+1), height*(y+1)))

            print("Downloading tiles: {}/{} completed".format(x*level + y + 1, level*level))
    print("\nDownloaded\n")

    output_file = tempfile.NamedTemporaryFile().name + ".png"
    png.save(output_file, "PNG")

    file_url = NSURL.fileURLWithPath_(output_file)
    options = {'NSImageScaleProportionallyUpOrDown': True}

    # get shared workspace
    ws = NSWorkspace.sharedWorkspace()

    # iterate over all screens
    for screen in NSScreen.screens():
        # tell the workspace to set the desktop picture
        (result, error) = ws.setDesktopImageURL_forScreen_options_error_(
                    file_url, screen, options, None)
        if error:
            print error
            exit(-1)

    print("Done!\n")

if __name__ == "__main__":
    main()
