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

        headers = {'content-type': 'application/json'}
        url = 'http://127.0.0.1:9999/api/v1/unit-breakdown'

        res = requests.post(url, data=json.dumps(data), headers=headers)

        data = json.loads(res.text)

        df = pd.DataFrame(data["content"], columns=["Boundary_flag"])
        df.to_csv("./csv/debug_ub1.csv", index=False)

        print(data)

    def test_expert_rule(self):
        initial_data = pd.read_csv("csv/initial_data.csv")

        gr = initial_data.GR.values
        tvd = initial_data.TVD.values

        data = {
            "GR": list(gr),
            "TVD": list(tvd)
        }

        headers = {'content-type': 'application/json'}
        url = 'http://127.0.0.1:9999/api/v1/unit-breakdown'

        res1 = requests.post(url, data=json.dumps(data), headers=headers)

        ub = json.loads(res1.text)

        ub = ub["content"]

        dct = {}
        dct.update({"Boundary_flag": ub})
        for key, value in initial_data.items():
            dct.update({key: list(value)})

        url = 'http://0.0.0.0:9999/api/v1/expert-rule'

        res2 = requests.post(url, data=json.dumps(dct), headers=headers)

        data1 = json.loads(res2.text)

        print(data1)

        data1 = data1["content"]


        tmp = []
        for i in range(len(data1["Boundary_flag"])):
            t = {}
            for key in data1.keys():
                t.update({key: data1[key][i]})

            tmp.append(deepcopy(t))

        utils_func.export_to_csv(tmp, "csv/T2X.csv")

        # print(data)

        # if data["success"]:
        #     headers = list(data["payload"][0].keys())
        #     print(data["payload"][0])
