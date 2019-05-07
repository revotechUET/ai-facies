from .prepare_data.prepare_data import prepare_data, unit_breakdown as ub
from .initial_point.main import init_point
from .similar_unit.similar_unit import similar_unit
from .special_lithology.special_lithology import special_lithology
from .modifier_set1.modifier_set1 import modifier_set1
from .modifier_set2.modifier_set2 import modifier_set2
from .utilities import utils_func
import traceback

import time
from copy import deepcopy


def expert_rule(input_data):
    print("Execution breakdown\n")
    start = time.time()
    data = prepare_data(input_data)
    initial_data = deepcopy(data)
    end = time.time()
    print(f"prepare_data execution time: {round(end - start, 2)}s\n")

    start = time.time()
    data = utils_func.simplify_data(data)
    end = time.time()
    print(f"simplify_data execution time: {round(end - start, 2)}s\n")

    start = time.time()
    init_point(data)
    end = time.time()
    print(f"init_point execution time: {round(end - start, 2)}s\n")

    start = time.time()
    similar_unit(data)
    end = time.time()
    print(f"similar_unit execution time: {round(end - start, 2)}s\n")

    start = time.time()
    special_lithology(data)
    end = time.time()
    print(f"special_lithology execution time: {round(end - start, 2)}s\n")

    start = time.time()
    modifier_set1(data)
    end = time.time()
    print(f"modifier_set1 execution time: {round(end - start, 2)}s\n")

    start = time.time()
    modifier_set2(data)
    end = time.time()
    print(f"modifier_set2 execution time: {round(end - start, 2)}s\n")

    start = time.time()
    utils_func.convert_data(data)
    end = time.time()
    print(f"convert_data execution time: {round(end - start, 2)}s\n")

    start = time.time()
    final = utils_func.convert_sample_by_sample(data, initial_data)
    end = time.time()
    print(f"convert_sample_by_sample execution time: {round(end - start, 2)}s\n")

    utils_func.export_to_csv(final, "csv/final.csv")

    output = {}

    print("ok")

    print(final[14000])
    print(final[14000]["Most_likely_facies"])
    print(type(final[14000]["Most_likely_facies"]))

    # for keys in final[0].keys():
    #     tmp = []
    #     i = 0
    #     for row in final:
    #         tmp.append(row[keys])
    #         print(i)
    #         i += 1
    #     output.update({keys: deepcopy(tmp)})
    #     print(f"{keys} {len(output[keys])}")
    #     tmp.clear()
    #
    print("ok1")

    return output

    # start = time.time()
    # utils_func.export_to_csv(initial_data, "csv/final.csv")
    # end = time.time()
    # print(f"export_to_csv execution time: {round(end - start, 2)}s\n")


def filter_null(item):
    if item == "null" or not item:
        return False
    return True


def unit_breakdown(gr, tvd):
    gr = list(filter(filter_null, gr))
    tvd = list(filter(filter_null, tvd))
    return ub(gr, tvd)
