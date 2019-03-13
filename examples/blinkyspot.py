#!/usr/bin/env python

import time
import colorsys

try:
    import numpy
except ImportError:
    exit("This script requires the numpy module\nInstall with: sudo pip install numpy")

from rgbmatrix5x5 import RGBMatrix5x5

rgbmatrix5x5 = RGBMatrix5x5()

rgbmatrix5x5.set_clear_on_exit()
rgbmatrix5x5.set_brightness(0.8)

height = rgbmatrix5x5.height
width = rgbmatrix5x5.width

if height == width:
    delta = 0
else:
    delta = 2


def make_gaussian(fwhm):
    x = numpy.arange(0, 5, 1, float)
    y = x[:, numpy.newaxis]
    x0, y0 = 2, 2
    fwhm = fwhm
    gauss = numpy.exp(-4 * numpy.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)
    return gauss


while True:
    for z in list(range(1, 10)[::-1]) + list(range(1, 10)):
        fwhm = 5.0 / z
        gauss = make_gaussian(fwhm)
        start = time.time()
        for y in range(height):
            for x in range(width):
                h = 0.5
                s = 0.8
                if height <= width:
                    v = gauss[x, y + delta]
                else:
                    v = gauss[x + delta, y]
                rgb = colorsys.hsv_to_rgb(h, s, v)
                r = int(rgb[0] * 255.0)
                g = int(rgb[1] * 255.0)
                b = int(rgb[2] * 255.0)
                rgbmatrix5x5.set_pixel(x, y, r, g, b)
        rgbmatrix5x5.show()
        end = time.time()
        t = end - start
        if t < 0.04:
            time.sleep(0.04 - t)
