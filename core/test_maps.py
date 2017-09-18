import unittest

from core.maps import hello


class TestHello(unittest.TestCase):

    def test_dumb(self):
        self.assertEqual(hello(), 'Hello World')


def test_dumb():
    assert hello() == 'Hello World'
