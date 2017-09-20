import pytest
import pprint

from core import maps
from core.maps import hello, read_data


@pytest.fixture(autouse=True)
def set_up_tests():
    print('set up class')
    maps.MAPS_FILE = "./core/pdvs_test.json"


def test_dumb():
    assert hello() == 'Hello World'


def test_read_json():
    pdvs = read_data()['pdvs']
    assert len(pdvs) == 51
    pprint.pprint(pdvs[0], indent=2)

