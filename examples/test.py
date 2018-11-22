#!/usr/bin/env python
import time
import ledmatrix

for col in ((255, 0, 0), (0, 255, 0), (0, 0, 255)):
    r, g, b = col
    for x in range(ledmatrix.DISPLAY_WIDTH):
        for y in range(ledmatrix.DISPLAY_HEIGHT):
            ledmatrix.clear()
            ledmatrix.set_pixel(x, y, r, g, b)
            ledmatrix.show()
            time.sleep(0.2)
