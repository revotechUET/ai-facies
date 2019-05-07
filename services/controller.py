from .prepare_data.prepare_data import prepare_data, unit_breakdown as ub
from .initial_point.main import init_point
from .similar_unit.similar_unit import similar_unit
from .special_lithology.special_lithology import special_lithology
from .modifier_set1.modifier_set1 import modifier_set1
from .modifier_set2.modifier_set2 import modifier_set2
from .utilities import utils_func
from numpy import array

import time
from copy import deepcopy


def expert_rule(input_data):
    pop_history = []
    required = ["Boundary_flag", "TVD", "GR", "MUD_VOLUME"]
    index = 0

    while index < len(input_data["Boundary_flag"]):
        for item in required:
            if input_data[item][index] in utils_func.CLIENT_UNDEFINED:
                for it in required:
                    input_data[it].pop(index)
                pop_history.append(index + len(pop_history))
                index -= 1
                break
        index += 1

    print(pop_history)

    for key in input_data.keys():
        input_data.update({key: array(input_data[key])})

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

    for keys in final[0].keys():
        tmp = []
        for row in final:
            tmp.append(row[keys])

        if keys in ["Most_likely_facies", "Second_most_likely_facies", "Third_most_likely_facies"]:
            for idx in pop_history:
                tmp.insert(idx, 0)

        elif keys in ["Uncertainty_flag"]:
            for idx in pop_history:
                tmp.insert(idx, 3)

        else:
            for idx in pop_history:
                tmp.insert(idx, 0)

        output.update({keys: deepcopy(tmp)})
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

    for ind in pop_history:
        lst.insert(ind, "null")

    return lst
