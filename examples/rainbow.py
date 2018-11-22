#!/usr/bin/env python

import colorsys
import time

import ledmatrix

spacing = 360.0 / 5.0
hue = 0

ledmatrix.set_clear_on_exit()
ledmatrix.set_brightness(0.8)

while True:
    for x in range(ledmatrix.DISPLAY_WIDTH):
        for y in range(ledmatrix.DISPLAY_HEIGHT):
            hue = int(time.time() * 100) % 360
            offset = (x * y) / 25.0 * spacing
            h = ((hue + offset) % 360) / 360.0
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
            ledmatrix.set_pixel(x, y, r, g, b)

    ledmatrix.show()
    time.sleep(0.0001)
