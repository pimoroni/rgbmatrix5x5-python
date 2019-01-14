#!/usr/bin/env python
import time
from rgbmatrix5x5 import RGBMatrix5x5

rgbmatrix5x5 = RGBMatrix5x5()

for col in ((255, 0, 0), (0, 255, 0), (0, 0, 255)):
    r, g, b = col
    for x in range(rgbmatrix5x5.width):
        for y in range(rgbmatrix5x5.height):
            rgbmatrix5x5.clear()
            rgbmatrix5x5.set_pixel(x, y, r, g, b)
            rgbmatrix5x5.show()
            time.sleep(0.2)