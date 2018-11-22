import mock
import sys


def test_setup():
    sys.modules['smbus'] = mock.Mock()
    import ledmatrix
    ledmatrix.show()
