from .unit_matching import *
import math
from ..utilities import utils_func


def prepare_data(data):
    gr = data["GR"]
    v_mud = data["MUD_VOLUME"]
    tvd = data["TVD"]

    optional = ["Biostratigraphy", "Lateral_proximity", "Special_lithology", "Core_depofacies", "Reliability"]

    # # sanity optional input
    # for item in optional:
    #     if item not in data.keys() or len(data[item]) == 0:
    #         data.update({item: [utils_func.UNDEFINED] * len(gr)})
    #
    #     else:
    #         for i in range(len(data[item])):
    #             if not data[item][i] or math.isnan(data[item][i]):
    #                 data[item][i] = utils_func.UNDEFINED
    #
    # for i in range(len(data["Reliability"])):
    #     if (data["Reliability"][i] is None or math.isnan(data["Reliability"][i]) or data["Reliability"][
    #         i] == utils_func.UNDEFINED or data["Reliability"][i] in utils_func.CLIENT_UNDEFINED) and \
    #             (data["Biostratigraphy"][i] != utils_func.UNDEFINED and data["Biostratigraphy"][
    #                 i] not in utils_func.CLIENT_UNDEFINED):
    #         data["Reliability"][i] = 2
    #
    # # end

    shape_code = detect_label_shape_code(gr, v_mud, tvd)
    lithofacies = detect_lithofacies(gr, v_mud, tvd)
    sharp_boundary = detect_sharp_boundary(gr, tvd)
    stacking_pattern = detect_stacking_pattern(gr, tvd)
    boundary = data["Boundary_flag"]
    boundary[len(boundary) - 1] = 1
    boundary[0] = 0
    unit_index = detect_unit_index(boundary)
    unit_thick = detect_unit_length(boundary, tvd)

    number_of_similar_units_50, similar_units_50 = find_similar_unit(gr, tvd, boundary, lithofacies, shape_code,
                                                                     unit_thick, unit_index, 50, 0)

    number_of_similar_units_100, similar_units_100 = find_similar_unit(gr, tvd, boundary, lithofacies, shape_code,
                                                                       unit_thick, unit_index, 100, 50)

    data.update({"Boundary_flag": boundary})
    data.update({"Lithofacies_major": lithofacies})
    data.update({"Sharp_boundary": sharp_boundary})
    data.update({"Stacking_pattern": stacking_pattern})
    data.update({"GR_shape_code": shape_code})
    data.update({"Unit_thick": unit_thick})
    data.update({"Unit_index": unit_index})
    data.update({"Number_of_similar_units_50": number_of_similar_units_50})
    data.update({"Index_of_similar_units_50": similar_units_50})
    data.update({"Number_of_similar_units_100": number_of_similar_units_100})
    data.update({"Index_of_similar_units_100": similar_units_100})

    data_set = []

    for i in range(len(tvd)):
        row = {}
        for key, value in data.items():
            row.update({key: value[i]})
        data_set.append(row)

    return data_set


def unit_breakdown(gr, tvd):
    return select_boundary(gr, tvd)
