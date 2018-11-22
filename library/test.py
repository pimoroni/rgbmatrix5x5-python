import time

import ledmatrix


for x in range(ledmatrix.width):
    ledmatrix.set_pixel(x,255,0,0)
    ledmatrix.show()
    time.sleep(0.05)

time.sleep(0.1)
ledmatrix.clear()
ledmatrix.show()

for x in range(ledmatrix.width):
    ledmatrix.set_pixel(x,0,255,0)
    ledmatrix.show()
    time.sleep(0.05)

time.sleep(0.1)
ledmatrix.clear()
ledmatrix.show()

for x in range(ledmatrix.width):
    ledmatrix.set_pixel(x,0,0,255)
    ledmatrix.show()
    time.sleep(0.05)
