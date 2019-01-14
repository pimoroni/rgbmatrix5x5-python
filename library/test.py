import time

import rgbmatrix5x5


for x in range(rgbmatrix5x5.width):
    for y in range(rgbmatrix5x5.height):
        rgbmatrix5x5.set_pixel(x,y,255,0,0)
        rgbmatrix5x5.show()
        time.sleep(0.05)

time.sleep(0.1)
rgbmatrix5x5.clear()
rgbmatrix5x5.show()

for x in range(rgbmatrix5x5.width):
    for y in range(rgbmatrix5x5.height):
        rgbmatrix5x5.set_pixel(x,y,0,255,0)
        rgbmatrix5x5.show()
        time.sleep(0.05)

time.sleep(0.1)
rgbmatrix5x5.clear()
rgbmatrix5x5.show()

for x in range(rgbmatrix5x5.width):
    for y in range(rgbmatrix5x5.height):
        rgbmatrix5x5.set_pixel(x,y,0,0,255)
        rgbmatrix5x5.show()
        time.sleep(0.05)
