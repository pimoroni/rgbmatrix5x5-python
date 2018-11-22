# LED Matrix

[![Build Status](https://travis-ci.com/pimoroni/led-matrix.svg?branch=master)](https://travis-ci.com/pimoroni/led-matrix)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/led-matrix/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/led-matrix?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/ledmatrix.svg)](https://pypi.python.org/pypi/ledmatrix)
[![Python Versions](https://img.shields.io/pypi/pyversions/ledmatrix.svg)](https://pypi.python.org/pypi/ledmatrix)

https://shop.pimoroni.com/products/led-matrix

An adorably tiny 5x5 pixel Breakout Garden compatible LED matrix breakout for adding status displays or fancy lighting to your project.

## Installing

### Full install (recommended):

We've created an easy installation script that will install all pre-requisites and get your LED Matrix
up and running with minimal efforts. To run it, fire up Terminal which you'll find in Menu -> Accessories -> Terminal
on your Raspberry Pi desktop, as illustrated below:

![Finding the terminal](http://get.pimoroni.com/resources/github-repo-terminal.png)

In the new terminal window type the command exactly as it appears below (check for typos) and follow the on-screen instructions:

```bash
curl https://get.pimoroni.com/ledmatrix | bash
```

### Manual install:

#### Library install for Python 3:

on Raspbian:

```bash
sudo apt-get install python3-ledmatrix
```

other environments: 

```bash
sudo pip3 install ledmatrix
```

#### Library install for Python 2:

on Raspbian:

```bash
sudo apt-get install python-ledmatrix
```

other environments: 

```bash
sudo pip2 install ledmatrix
```

### Development:

If you want to contribute, or like living on the edge of your seat by having the latest code, you should clone this repository, `cd` to the library directory, and run:

```bash
sudo python3 setup.py install
```
(or `sudo python setup.py install` whichever your primary Python environment may be)

In all cases you will have to enable the i2c bus.

## Documentation & Support

* Guides and tutorials - https://learn.pimoroni.com/led-matrix
* Function reference - http://docs.pimoroni.com/ledmatrix/
* Get help - http://forums.pimoroni.com/c/support
