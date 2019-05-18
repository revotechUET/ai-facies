from .prepare_data.prepare_data import prepare_data, unit_breakdown as ub
from .initial_point.main import init_point
from .similar_unit.similar_unit import similar_unit
from .special_lithology.special_lithology import special_lithology
from .modifier_set1.modifier_set1 import modifier_set1
from .modifier_set2.modifier_set2 import modifier_set2
from .utilities import utils_func
from numpy import array
import math

import time
from copy import deepcopy


def expert_rule(input_data):
    # sanitizing input
    pop_history = []
    required = ["Boundary_flag", "TVD", "GR", "MUD_VOLUME", "Depth"]
    index = 0
    while index < len(input_data["Boundary_flag"]):
        for item in required:
            if input_data[item][index] is None or (
                    input_data[item][index] in utils_func.CLIENT_UNDEFINED) or math.isnan(input_data[item][index]) or \
                    input_data[item][index] == utils_func.UNDEFINED:
                for key in input_data.keys():
                    if len(input_data[key]) > 0:
                        input_data[key].pop(index)
                pop_history.append(index + len(pop_history))
                index -= 1
                break
        index += 1

    for key in input_data.keys():
        input_data.update({key: array(input_data[key])})

    optional = ["Biostratigraphy", "Lateral_proximity", "Special_lithology", "Core_depofacies", "Reliability"]

    for item in optional:
        if item not in input_data.keys() or len(input_data[item]) == 0:
            input_data.update({item: [utils_func.UNDEFINED] * len(input_data["TVD"])});

        else:
            for i in range(len(input_data[item])):
                if not input_data[item][i] or math.isnan(input_data[item][i]):
                    input_data[item][i] = utils_func.UNDEFINED

    for i in range(len(input_data["Reliability"])):
        if (input_data["Reliability"][i] is None or math.isnan(input_data["Reliability"][i]) or
            input_data["Reliability"][
                i] == utils_func.UNDEFINED or input_data["Reliability"][i] in utils_func.CLIENT_UNDEFINED) and \
                (input_data["Biostratigraphy"][i] != utils_func.UNDEFINED and input_data["Biostratigraphy"][
                    i] not in utils_func.CLIENT_UNDEFINED):
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

    for key in output_curves:
        tmp = []
        for row in final:
            tmp.append(row[key])
        for idx in pop_history:
            tmp.insert(idx, "")

        output.update({key: deepcopy(tmp)})
        tmp.clear()

    return output


def filter_null(item):
    if item == "null" or not item:
        return False
    return True


def unit_breakdown(gr, tvd):
    i = 0
    pop_history = []

    while i < len(gr):
        if gr[i] == "null" or gr[i] == "NaN" or not gr[i]:
            gr.pop(i)
            tvd.pop(i)
            pop_history.append(i + len(pop_history))
            i -= 1
        elif tvd[i] == "null" or not tvd[i]:
            tvd.pop(i)
            gr.pop(i)
            pop_history.append(i + len(pop_history))
            i -= 1
        i += 1

    gr = array(gr)
    tvd = array(tvd)

    lst = ub(gr, tvd)

    lst = list(lst)

    for ind in pop_history:
        lst.insert(ind, "null")

    return lst
