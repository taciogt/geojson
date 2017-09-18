import unittest

from core.maps import hello, read_data


class TestHello(unittest.TestCase):

    def test_dumb(self):
        self.assertEqual(hello(), 'Hello World')


    def test_read_json(self):
        pdvs = read_data()['pdvs']
        assert len(pdvs) == 51
