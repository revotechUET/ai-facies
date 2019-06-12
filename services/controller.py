from .prepare_data.prepare_data import prepare_data, unit_breakdown as ub
from .initial_point.main import init_point
from .machine_learning import ml
from .similar_unit.similar_unit import similar_unit
from .special_lithology.special_lithology import special_lithology
from .modifier_set1.modifier_set1 import modifier_set1
from .modifier_set2.modifier_set2 import modifier_set2
from .utilities import utils_func
from .prepare_data.core.units import UnitBreaker
from numpy import array

import time
from copy import deepcopy


def expert_rule(input_data):
    # sanitizing input

    for item in input_data["Boundary_flag"]:
        print(item)

    # Convert to numpy format
    for key in input_data.keys():
        input_data.update({key: array(input_data[key])})

    # Fill null values for optional field
    optional = ["ML", "Biostratigraphy", "Lateral_proximity", "Special_lithology", "Core_depofacies", "Reliability"]

    for item in optional:
        if item not in input_data.keys() or len(input_data[item]) == 0:
            input_data.update({item: [utils_func.UNDEFINED] * len(input_data["TVD"])})

    # Fill null values for required field
    required = ["TVD", "GR", "MUD_VOLUME", "Depth"]

    for key in required:
        data, _ = UnitBreaker.fill_null_values(input_data[key])
        input_data.update({key: data})

    # Fill default reliability = 2
    for i in range(len(input_data["Reliability"])):
        if input_data["Reliability"][i] == utils_func.UNDEFINED and \
                input_data["Biostratigraphy"][i] != utils_func.UNDEFINED:
            input_data["Reliability"][i] = 2

    # end sanitizing input

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
    ml.machine_learning(data)
    end = time.time()
    print(f"machine_learning execution time: {round(end - start, 2)}s\n")

    additional_point = 10
    for row in data:
        for key in utils_func.NAMES:
            if row[key] > 0:
                row[key] += additional_point

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

    output = {}

    output_curves = utils_func.OUTPUT + utils_func.OUTPUT_NUMPY_FORMAT
    output_curves.append("Boundary_flag")

    tmp = []
    for key in output_curves:
        for row in final:
            tmp.append(row[key])
        output.update({key: deepcopy(tmp)})
        tmp.clear()

    return output


def unit_breakdown(gr, tvd):
    gr = array(gr)
    tvd = array(tvd)

    gr, _ = UnitBreaker.fill_null_values(gr)
    tvd, _ = UnitBreaker.fill_null_values(tvd)

    lst = ub(gr, tvd)

    lst = list(lst)

    return lst
