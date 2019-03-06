#!/usr/bin/env python

import colorsys
import time

from rgbmatrix5x5 import RGBMatrix5x5

rgbmatrix5x5 = RGBMatrix5x5()

rgbmatrix5x5.set_clear_on_exit()
rgbmatrix5x5.set_brightness(0.8)

colours = [
    (0xff, 0x00, 0x00),
    (0x00, 0xff, 0x00),
    (0x00, 0x00, 0xff)
]

while True:
    r, g, b = colours.pop(0)
    colours.append((r, g, b))
    rgbmatrix5x5.set_all(r, g, b)
    rgbmatrix5x5.show()
    time.sleep(0.5)
