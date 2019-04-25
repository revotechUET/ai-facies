from .prepare_data.prepare_data import prepare_data, unit_breakdown as ub
from .initial_point.main import init_point
from .similar_unit.similar_unit import similar_unit
from .special_lithology.special_lithology import special_lithology
from .modifier_set1.modifier_set1 import modifier_set1
from .modifier_set2.modifier_set2 import modifier_set2
from .utilities import utils_func

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
    utils_func.convert_sample_by_sample(data, initial_data)
    end = time.time()
    print(f"convert_sample_by_sample execution time: {round(end - start, 2)}s\n")


    return data

    # start = time.time()
    # utils_func.export_to_csv(initial_data, "csv/final.csv")
    # end = time.time()
    # print(f"export_to_csv execution time: {round(end - start, 2)}s\n")


def unit_breakdown(gr, tvd):
    return ub(gr, tvd)
