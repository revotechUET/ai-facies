from .unit_matching import *
import math
from ..utilities import utils_func


def prepare_data(data):
    gr = data["GR"]
    v_mud = data["MUD_VOLUME"]
    tvd = data["TVD"]
    md = data["Depth"]

    shape_code = detect_label_shape_code(gr, v_mud, tvd, md)
    lithofacies = detect_lithofacies(gr, v_mud, tvd)
    sharp_boundary = detect_sharp_boundary(gr, tvd)
    stacking_pattern = detect_stacking_pattern(gr, tvd)
    boundary = data["Boundary_flag"]
    boundary[len(boundary) - 1] = 1
    boundary[0] = 0
<<<<<<< HEAD
=======

    # boundary = select_boundary(gr, tvd)
>>>>>>> master
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
