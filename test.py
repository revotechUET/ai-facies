import unittest
import pandas as pd
import requests
import json


class MyTest(unittest.TestCase):
    def test_unit_breakdown(self):
        data = pd.read_csv("csv/initial_data.csv")

        gr = data.GR.values
        tvd = data.TVD.values

        data = {
            "GR": list(gr),
            "TVD": list(tvd)
        }

        headers = {'content-type': 'application/json'}
        url = 'http://127.0.0.1:9999/api/v1/unit-breakdown'

        res = requests.post(url, data=json.dumps(data), headers=headers)

        data = json.loads(res.text)

        print(data)

    def test_expert_rule(self):
        data = pd.read_csv("csv/initial_data.csv")

        dct = {}

        for key, value in data.items():
            dct.update({key: list(value)})

        headers = {'content-type': 'application/json'}
        url = 'http://127.0.0.1:9999/api/v1/expert-rule'

        res = requests.post(url, data=json.dumps(dct), headers=headers)

        print(res)