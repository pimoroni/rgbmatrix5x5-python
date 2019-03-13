#!/usr/bin/env python

import time

from rgbmatrix5x5 import RGBMatrix5x5


print("""
RGBMatrix5x5 - Set Multiple Pixels Demo

Uses `set_multiple_pixels` to display a chessboard pattern.

Press Ctrl+C to exit!
""")

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
    rgbmatrix5x5.set_multiple_pixels(list(range(1, 25, 2)), (r, g, b))
    rgbmatrix5x5.show()
    time.sleep(0.5)
