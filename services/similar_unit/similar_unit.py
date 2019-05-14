from ..utilities import utils_func


def find_unit_core_depofacies(unit_index, data_list):
    codes = []
    for u in unit_index:
        code = data_list[u]["Core_depofacies"]
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


def similar_unit(data):
    for i in range(len(data)):
        if data[i]["Number_of_similar_units_50"] != 0 or data[i]["Core_depofacies"] != utils_func.UNDEFINED:
            unit_index = data[i]["Index_of_similar_units_50"]
            if data[i]["Core_depofacies"] != utils_func.UNDEFINED:
                idx = data[i]["Unit_index"]
                unit_index.append(idx)
            codes = find_unit_core_depofacies(unit_index, data)
            for code in codes:
                name = utils_func.map_core_depofacies_code_to_name(code)
                if name:
                    new_point = handle_point(data[i][name], "0-50")
                    data[i].update({name: new_point})

        if data[i]["Number_of_similar_units_100"] != 0:
            unit_index = data[i]["Index_of_similar_units_100"]
            codes = find_unit_core_depofacies(unit_index, data)
            for code in codes:
                name = utils_func.map_core_depofacies_code_to_name(code)
                if name:
                    new_point = handle_point(data[i][name], "50-100")
                    data[i].update({name: new_point})
