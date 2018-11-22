LED Matrix
==========

|Build Status| |Coverage Status| |PyPi Package| |Python Versions|

https://shop.pimoroni.com/products/led-matrix

An adorably tiny 5x5 pixel Breakout Garden compatible LED matrix
breakout for adding status displays or fancy lighting to your project.

Installing
----------

Full install (recommended):
~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've created an easy installation script that will install all
pre-requisites and get your LED Matrix up and running with minimal
efforts. To run it, fire up Terminal which you'll find in Menu ->
Accessories -> Terminal on your Raspberry Pi desktop, as illustrated
below:

.. figure:: http://get.pimoroni.com/resources/github-repo-terminal.png
   :alt: Finding the terminal

   Finding the terminal
In the new terminal window type the command exactly as it appears below
(check for typos) and follow the on-screen instructions:

.. code:: bash

    curl https://get.pimoroni.com/ledmatrix | bash

Manual install:
~~~~~~~~~~~~~~~

Library install for Python 3:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

on Raspbian:

.. code:: bash

    sudo apt-get install python3-ledmatrix

other environments:

.. code:: bash

    sudo pip3 install ledmatrix

Library install for Python 2:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

on Raspbian:

.. code:: bash

    sudo apt-get install python-ledmatrix

other environments:

.. code:: bash

    sudo pip2 install ledmatrix

Development:
~~~~~~~~~~~~

If you want to contribute, or like living on the edge of your seat by
having the latest code, you should clone this repository, ``cd`` to the
library directory, and run:

.. code:: bash

    sudo python3 setup.py install

(or ``sudo python setup.py install`` whichever your primary Python
environment may be)

In all cases you will have to enable the i2c bus.

Documentation & Support
-----------------------

-  Guides and tutorials - https://learn.pimoroni.com/led-matrix
-  Function reference - http://docs.pimoroni.com/ledmatrix/
-  Get help - http://forums.pimoroni.com/c/support

.. |Build Status| image:: https://travis-ci.com/pimoroni/led-matrix.svg?branch=master
   :target: https://travis-ci.com/pimoroni/led-matrix
.. |Coverage Status| image:: https://coveralls.io/repos/github/pimoroni/led-matrix/badge.svg?branch=master
   :target: https://coveralls.io/github/pimoroni/led-matrix?branch=master
.. |PyPi Package| image:: https://img.shields.io/pypi/v/ledmatrix.svg
   :target: https://pypi.python.org/pypi/ledmatrix
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/ledmatrix.svg
   :target: https://pypi.python.org/pypi/ledmatrix
