#!/usr/bin/env python

import random
from sys import exit

try:
    import numpy
except ImportError:
    exit('This script requires the numpy module\nInstall with: sudo pip install numpy')

from rgbmatrix5x5 import RGBMatrix5x5

rgbmatrix5x5 = RGBMatrix5x5()

rgbmatrix5x5.set_clear_on_exit()
rgbmatrix5x5.set_brightness(0.8)

height = rgbmatrix5x5.height
width = rgbmatrix5x5.width

forest_width = width
forest_height = height

hood_size = 3

def get_neighbours(x, y, z):
    return [(x2, y2) for x2 in range(x - (z - 1), x + z) for y2 in range(y - (z - 1), y + z) if (-1 < x < forest_width and -1 < y < forest_height and (x != x2 or y != y2) and (0 <= x2 < forest_width) and (0 <= y2 < forest_height))]


initial_trees = 0.55
p = 0.01
f = 0.001

tree = [0, 255, 0]
burning = [255, 0, 0]
space = [0, 0, 0]


def initialise():
    forest = [[tree if random.random() <= initial_trees else space for x in range(forest_width)] for y in range(forest_height)]
    return forest


def update_forest(forest):
    new_forest = [[space for x in range(forest_width)] for y in range(forest_height)]
    for x in range(forest_width):
        for y in range(forest_height):
            if forest[x][y] == burning:
                new_forest[x][y] = space
            elif forest[x][y] == space:
                new_forest[x][y] = tree if random.random() <= p else space
            elif forest[x][y] == tree:
                neighbours = get_neighbours(x, y, hood_size)
                new_forest[x][y] = (burning if any([forest[n[0]][n[1]] == burning for n in neighbours]) or random.random() <= f else tree)
    return new_forest


def show_forest(forest):
    for x in range(width):
        for y in range(height):
            r, g, b = forest[x][y]
            rgbmatrix5x5.set_pixel(x, y, int(r), int(g), int(b))

    rgbmatrix5x5.show()


forest = initialise()

while True:
    show_forest(forest)
    forest = update_forest(forest)
