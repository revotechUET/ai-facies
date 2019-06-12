import unittest
import pandas as pd
import requests
import json
from services.utilities import utils_func
from copy import deepcopy


class MyTest(unittest.TestCase):
    def test_unit_breakdown(self):
        data = pd.read_csv("csv/initial_data.csv")

        gr = data.GR.values
        tvd = data.TVD.values

        data = {
            "GR": list(gr),
            "TVD": list(tvd)
        }

        for key in data.keys():
            for i in range(len(data[key])):
                if data[key][i] in [-9999, "-9999"]:
                    data[key][i] = -1

        headers = {'content-type': 'application/json'}
        url = 'http://127.0.0.1:9999/api/v1/unit-breakdown'

        res = requests.post(url, data=json.dumps(data), headers=headers)

        data = json.loads(res.text)

        print(data["content"])

    def test_expert_rule(self):
        initial_data = pd.read_csv("csv/initial_data.csv")

        gr = initial_data.GR.values
        tvd = initial_data.TVD.values

        data1 = {
            "GR": list(gr),
            "TVD": list(tvd)
        }

        for key in data1.keys():
            for i in range(len(data1[key])):
                if data1[key][i] in [-9999, "-9999"]:
                    data1[key][i] = -1

        headers = {'content-type': 'application/json'}
        url = 'http://127.0.0.1:9999/api/v1/unit-breakdown'

        res1 = requests.post(url, data=json.dumps(data1), headers=headers)

        ub = json.loads(res1.text)

        ub = ub["content"]

        dct = {}
        dct.update({"Boundary_flag": ub})
        for key, value in initial_data.items():
            dct.update({key: list(value)})

        url = 'http://0.0.0.0:9999/api/v1/expert-rule'

        for key in dct.keys():
            for i in range(len(dct[key])):
                if dct[key][i] in [-9999, "-9999"]:
                    dct[key][i] = -1

        res2 = requests.post(url, data=json.dumps(dct), headers=headers)

        data2 = json.loads(res2.text)

        content = data2["content"]

        tmp = []
        for i in range(len(content["Boundary_flag"])):
            t = {}
            for key in content.keys():
                t.update({key: content[key][i]})
            tmp.append(deepcopy(t))

        utils_func.export_to_csv(tmp, "csv/T2X.csv")

        # if data["success"]:
        #     headers = list(data["payload"][0].keys())
        #     print(data["payload"][0])


if __name__ == '__main__':
    unittest.main()
