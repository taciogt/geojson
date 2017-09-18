import json


def hello():
    return "Hello World"


def read_data():
    with open("pdvs.json") as f:
        pdvs = json.load(f)
    return pdvs
