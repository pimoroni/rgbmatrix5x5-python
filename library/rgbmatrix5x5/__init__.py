"""LED SHIM 28-pixel RGB LED display."""
from . import is31fl3731

__version__ = '0.0.1'

display = is31fl3731.LEDSHIM(None, address=0x74, gamma_table=is31fl3731.LED_GAMMA)

DISPLAY_HEIGHT = 5
DISPLAY_WIDTH = 5
NUM_PIXELS = DISPLAY_HEIGHT * DISPLAY_WIDTH

pixel = display.set_pixel
set_pixel_index = display.set_pixel
set_all = display.set_all
set_brightness = display.set_brightness
show = display.show
width = display.width
height = display.height
clear = display.clear
get_buffer_shape = display.get_shape
get_shape = display.get_shape
set_clear_on_exit = display.set_clear_on_exit


def set_pixel(x, y, r, g, b):
    """Set a single pixel.

    :param x: X position from 0 to 4
    :param y: Y position from 0 to 4
    :param r: Amount of red from 0 to 255
    :param g: Amount of green from 0 to 255
    :param b: Amount of blue from 0 to 255

    """
    x, y = y, x
    if x % 2 == 1:
        y = 4 - y
    display.set_pixel(y + (x * 5), r, g, b)


def set_multiple_pixels(indexes, from_colour, to_colour=None):
    """Set multiple pixels to a range of colours sweeping from from_colour to to_colour.

    :param from_colour: A tuple with 3 values representing the red, green and blue of the first colour
    :param to_colour: A tuple with 3 values representing the red, green and blue of the second colour

    """
    if to_colour is None:
        to_colour = from_colour

    length = float(len(indexes))
    step = 0
    from_r, from_g, from_b = from_colour
    to_r, to_g, to_b = to_colour
    step_r, step_g, step_b = to_r - from_r, to_g - from_g, to_b - from_b
    step_r /= length
    step_g /= length
    step_b /= length

    for index in indexes:
        display.set_pixel(index, from_r + (step_r * step), from_g + (step_g * step), from_b + (step_b * step))
        step += 1
