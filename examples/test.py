#!/usr/bin/env python
import time
import rgbmatrix5x5

for col in ((255, 0, 0), (0, 255, 0), (0, 0, 255)):
    r, g, b = col
    for x in range(rgbmatrix5x5.DISPLAY_WIDTH):
        for y in range(rgbmatrix5x5.DISPLAY_HEIGHT):
            rgbmatrix5x5.clear()
            rgbmatrix5x5.set_pixel(x, y, r, g, b)
            rgbmatrix5x5.show()
            time.sleep(0.2)
