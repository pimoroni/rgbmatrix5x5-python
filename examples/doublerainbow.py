#!/usr/bin/env python

import colorsys
import time

from rgbmatrix5x5 import RGBMatrix5x5

rainbow1 = RGBMatrix5x5(0x74)
rainbow2 = RGBMatrix5x5(0x77)

spacing = 360.0 / 5.0
hue = 0

for rainbow in [rainbow1, rainbow2]:
    rainbow.set_clear_on_exit()
    rainbow.set_brightness(0.8)

while True:
    for x in range(rainbow1.width):
        for y in range(rainbow1.height):
            hue = int(time.time() * 100) % 360
            offset = (x * y) / 25.0 * spacing
            h = ((hue + offset) % 360) / 360.0
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
            rainbow1.set_pixel(x, y, r, g, b)
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h + 0.5, 1.0, 1.0)]
            rainbow2.set_pixel(x, y, r, g, b)

    rainbow1.show()
    rainbow2.show()
    time.sleep(0.0001)
