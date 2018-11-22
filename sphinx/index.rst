.. role:: python(code)
   :language: python

Welcome
-------

This documentation will guide you through the methods available in the LED Matrix Python library.

LED Matrix Breakout provides 5x5 tiny RGB LEDs which you can light up with any colour you like!

* More information - https://shop.pimoroni.com/products/led-matrix
* Get the code - https://github.com/pimoroni/led-matrix
* Get help - http://forums.pimoroni.com/c/support

.. currentmodule:: ledmatrix.is31fl3731.Matrix

At A Glance
-----------

.. autoclassoutline:: ledmatrix.is31fl3731.Matrix
   :members:

.. toctree::
   :titlesonly:
   :maxdepth: 0

Set A Single Pixel In Buffer
----------------------------

When you set a pixel it will not immediately display on LED Matrix, you must call :python:`ledmatrix.show()`.

.. automethod:: ledmatrix.is31fl3731.Matrix.set_pixel
   :noindex:

Display Buffer
--------------

All of your changes to LED Matrix are stored in a Python buffer. To display them
on LED Matrix you must call :python:`ledmatrix.show()`.

.. automethod:: ledmatrix.is31fl3731.Matrix.show
   :noindex:

Clear Buffer
------------

.. automethod:: ledmatrix.is31fl3731.Matrix.clear
   :noindex:

Get The Display Size
--------------------

.. automethod:: ledmatrix.is31fl3731.Matrix.get_shape
   :noindex:

Set Multiple Pixels
-------------------

.. autofunction:: ledmatrix.set_multiple_pixels
