# LED Matrix

[![Build Status](https://travis-ci.com/pimoroni/rgbmatrix5x5-python.svg?branch=master)](https://travis-ci.com/pimoroni/rgbmatrix5x5-python)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/rgbmatrix5x5-python/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/rgbmatrix5x5-python?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/rgbmatrix5x5.svg)](https://pypi.python.org/pypi/rgbmatrix5x5)
[![Python Versions](https://img.shields.io/pypi/pyversions/rgbmatrix5x5.svg)](https://pypi.python.org/pypi/rgbmatrix5x5)

https://shop.pimoroni.com/products/5x5-rgb-matrix-breakout

An adorably tiny 5x5 pixel Breakout Garden compatible LED matrix breakout for adding status displays or fancy lighting to your project.

## Installing

### Full install (recommended):

We've created an easy installation script that will install all pre-requisites and get your LED Matrix
up and running with minimal efforts. To run it, fire up Terminal which you'll find in Menu -> Accessories -> Terminal
on your Raspberry Pi desktop, as illustrated below:

![Finding the terminal](http://get.pimoroni.com/resources/github-repo-terminal.png)

In the new terminal window type the command exactly as it appears below (check for typos) and follow the on-screen instructions:

```bash
curl https://get.pimoroni.com/rgbmatrix5x5 | bash
```

### Manual install:

#### Library install for Python 3:

```bash
sudo pip3 install rgbmatrix5x5
```

#### Library install for Python 2:

```bash
sudo pip2 install rgbmatrix5x5
```

### Development:

If you want to contribute, or like living on the edge of your seat by having the latest code, you should clone this repository, `cd` to the library directory, and run:

```bash
sudo python3 setup.py install
```
(or `sudo python setup.py install` whichever your primary Python environment may be)

In all cases you will have to enable the i2c bus.

## Documentation & Support

* Get help - http://forums.pimoroni.com/c/support
