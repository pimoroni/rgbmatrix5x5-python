import mock
import sys


def test_setup():
    sys.modules['smbus'] = mock.Mock()
    import rgbmatrix5x5
    rgbmatrix5x5.show()
