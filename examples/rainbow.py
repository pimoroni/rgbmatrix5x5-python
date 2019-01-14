#!/usr/bin/env python

import colorsys
import time

from rgbmatrix5x5 import RGBMatrix5x5

rgbmatrix5x5 = RGBMatrix5x5()

spacing = 360.0 / 5.0
hue = 0

rgbmatrix5x5.set_clear_on_exit()
rgbmatrix5x5.set_brightness(0.8)

while True:
    for x in range(rgbmatrix5x5.width):
        for y in range(rgbmatrix5x5.height):
            hue = int(time.time() * 100) % 360
            offset = (x * y) / 25.0 * spacing
            h = ((hue + offset) % 360) / 360.0
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
            rgbmatrix5x5.set_pixel(x, y, r, g, b)

    rgbmatrix5x5.show()
    time.sleep(0.0001)
