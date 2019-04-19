from utilities import utils_func
from copy import deepcopy


def add_point_volcanics(row):
    return row


def add_point_marine_non_clastic(row):
    marines = ["Shallow_Marine", "Marginal_Marine", "Deep_Marine"]
    for group_name in marines:
        codes = utils_func.get_group_depofacies(group_name)
        for code in codes:
            name = utils_func.map_core_depofacies_code_to_name(code)
            if int(row[name]) > 0:
                row.update({name: int(row[name]) + 2})
    return row


def add_point_coal(row):
    for code in utils_func.get_group_depofacies("Fluvial"):
        name = utils_func.map_core_depofacies_code_to_name(code)
        if int(row[name]) > 0:
            row.update({name: int(row[name]) + 2})

    for code in utils_func.get_group_depofacies("Marginal_Marine"):
        name = utils_func.map_core_depofacies_code_to_name(code)
        if int(row[name]) > 0:
            row.update({name: int(row[name]) + 1})
    return row


def updateRow(row, litho_code):
    litho_code = int(litho_code)
    if litho_code in [1, 2]:
        return add_point_volcanics(row)
    if litho_code in range(3, 8):
        return add_point_marine_non_clastic(row)
    if litho_code == 8:
        return add_point_coal(row)
    return row


def find_adjacent_unit_special_lithology(unit_index, data):
    unit_index = int(unit_index)
    lithologies = data[unit_index]["Special_lithologies"]
    before = data[unit_index - 1 if unit_index > 0 else 0]["Special_lithologies"]
    after = data[unit_index + 1 if unit_index < len(data) - 1 else len(data) - 1]["Special_lithologies"]
    lithologies.extend(before)
    lithologies.extend(after)
    return utils_func.remove_duplicate(lithologies)


def simplify_data(data):
    lst = []
    lithos = []
    for i in range(len(data)):
        if data[i]["Special_lithology"] != "-9999":
            lithos.append(data[i]["Special_lithology"])
        if data[i]["Boundary_flag"]:
            final_lithologies = deepcopy(utils_func.remove_duplicate(lithos))
            lst.append({
                "Unit_index": data[i]["Unit_index"],
                "Special_lithologies": final_lithologies
            })
            lithos.clear()

    return lst


def special_lithology(data):
    simplified_unit = simplify_data(deepcopy(data))
    for i in range(len(data)):
        lithologies = find_adjacent_unit_special_lithology(data[i]["Unit_index"], simplified_unit)
        if len(lithologies) > 0:
            for lithology in lithologies:
                data[i].update(updateRow(data[i], lithology))

    utils_func.export_to_csv(data, f"csv/special_lithology.csv")
