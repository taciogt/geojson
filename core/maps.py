import json


MAPS_FILE = "./core/pdvs.json"


def hello():
    return "Hello World"


def read_data():
    with open(MAPS_FILE) as f:
        pdvs = json.load(f)
    return pdvs
