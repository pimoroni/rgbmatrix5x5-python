import mock
import sys


def test_setup():
    sys.modules['smbus'] = mock.Mock()
    from rgbmatrix5x5 import RGBMatrix5x5
    rgbmatrix5x5 = RGBMatrix5x5()
    rgbmatrix5x5.show()
