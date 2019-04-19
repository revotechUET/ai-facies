from utilities import utils_func
from copy import deepcopy


def find_unit_core_depofacies(unit_index, data_list):
    codes = []
    for u in unit_index:
        code = utils_func.pick_most(data_list[int(u)]["Core_depofacies"])
        codes.append(code)
    return codes


def handle_point(current_point, radius):
    current_point = int(current_point)
    if current_point == 0:
        current_point = 5
    elif radius == "0-50":
        current_point += 4
    elif radius == "50-100":
        current_point += 2
    return current_point


def simplify_data(data):
    lst = []
    core_depos = []
    for i in range(len(data)):
        if float(data[i]["Core_depofacies"]) != -9999:
            core_depos.append(data[i]["Core_depofacies"])
        if data[i]["Boundary_flag"] == "1":
            final_depofacies = deepcopy(utils_func.remove_duplicate(core_depos))
            data[i].update({"Core_depofacies": final_depofacies})
            lst.append(data[i])
            core_depos.clear()

    return lst


def similar_unit(data):
    simplified = simplify_data(deepcopy(data))

    for i in range(len(data)):
        if data[i]["Number_of_similar_units_50"] != "0" or data[i]["Core_depofacies"] != "-9999":
            unit_index = utils_func.convert_string_to_array(data[i]["Index_of_similar_units_50"])
            idx = data[i]["Unit_index"]
            unit_index.append(idx)
            codes = find_unit_core_depofacies(unit_index, simplified)
            for code in codes:
                name = utils_func.map_core_depofacies_code_to_name(code)
                if name:
                    new_point = handle_point(data[i][name], "0-50")
                    data[i].update({name: new_point})

        if data[i]["Number_of_similar_units_100"] != "0":
            unit_index = utils_func.convert_string_to_array(data[i]["Index_of_similar_units_100"])
            codes = find_unit_core_depofacies(unit_index, simplified)
            for code in codes:
                name = utils_func.map_core_depofacies_code_to_name(code)
                if name:
                    new_point = handle_point(data[i][name], "50-100")
                    data[i].update({name: new_point})
