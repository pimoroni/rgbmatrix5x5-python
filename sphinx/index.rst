.. role:: python(code)
   :language: python

Welcome
-------

This documentation will guide you through the methods available in the LED Matrix Python library.

LED Matrix Breakout provides 5x5 tiny RGB LEDs which you can light up with any colour you like!

* More information - https://shop.pimoroni.com/products/5x5-rgb-matrix-breakout
* Get the code - https://github.com/pimoroni/rgbmatrix5x5-python
* Get help - http://forums.pimoroni.com/c/support

.. currentmodule:: rgbmatrix5x5.is31fl3731.Matrix

At A Glance
-----------

.. autoclassoutline:: rgbmatrix5x5.is31fl3731.Matrix
   :members:

.. toctree::
   :titlesonly:
   :maxdepth: 0

Set A Single Pixel In Buffer
----------------------------

When you set a pixel it will not immediately display on LED Matrix, you must call :python:`rgbmatrix5x5.show()`.

.. automethod:: rgbmatrix5x5.is31fl3731.Matrix.set_pixel
   :noindex:

Display Buffer
--------------

All of your changes to LED Matrix are stored in a Python buffer. To display them
on LED Matrix you must call :python:`rgbmatrix5x5.show()`.

.. automethod:: rgbmatrix5x5.is31fl3731.Matrix.show
   :noindex:

Clear Buffer
------------

.. automethod:: rgbmatrix5x5.is31fl3731.Matrix.clear
   :noindex:

Get The Display Size
--------------------

.. automethod:: rgbmatrix5x5.is31fl3731.Matrix.get_shape
   :noindex:

Set Multiple Pixels
-------------------

.. autofunction:: rgbmatrix5x5.set_multiple_pixels
