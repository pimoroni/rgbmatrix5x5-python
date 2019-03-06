import mock
import sys


def test_set_all():
    sys.modules['smbus'] = mock.Mock()
    from rgbmatrix5x5 import RGBMatrix5x5
    rgbmatrix5x5 = RGBMatrix5x5()
    rgbmatrix5x5.set_all(255, 0, 0)
    rgbmatrix5x5.show()
    assert rgbmatrix5x5.buf == [(255, 0, 0, 1.0)] * 5 * 5
