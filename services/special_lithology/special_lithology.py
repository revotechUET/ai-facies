from ..utilities import utils_func


def add_point_volcanics(row):
    return


def add_point_marine_non_clastic(row):
    marines = ["Shallow_Marine", "Marginal_Marine", "Deep_Marine"]
    for group_name in marines:
        codes = utils_func.get_group_depofacies(group_name)
        for code in codes:
            name = utils_func.map_core_depofacies_code_to_name(code)
            if int(row[name]) > 0:
                row.update({name: int(row[name]) + 2})


def add_point_coal(row):
    for code in utils_func.get_group_depofacies("Fluvial"):
        name = utils_func.map_core_depofacies_code_to_name(code)
        if int(row[name]) > 0:
            row.update({name: int(row[name]) + 2})

    for code in utils_func.get_group_depofacies("Marginal_Marine"):
        name = utils_func.map_core_depofacies_code_to_name(code)
        if int(row[name]) > 0:
            row.update({name: int(row[name]) + 1})


def update_row(row, litho_code):
    litho_code = int(litho_code)
    if litho_code in [1, 2]:
        return add_point_volcanics(row)
    if litho_code in range(3, 8):
        return add_point_marine_non_clastic(row)
    if litho_code == 8:
        return add_point_coal(row)


def find_adjacent_unit_special_lithology(unit_index, data):
    unit_index = int(unit_index)
    lst = []

    current = data[unit_index]["Special_lithology"]
    before = data[unit_index - 1 if unit_index > 0 else 0]["Special_lithology"]
    after = data[unit_index + 1 if unit_index < len(data) - 1 else len(data) - 1]["Special_lithology"]

    lst.extend(current)
    lst.extend(before)
    lst.extend(after)
    return utils_func.remove_duplicate(lst)


def special_lithology(data):
    for i in range(len(data)):
        lithos = find_adjacent_unit_special_lithology(data[i]["Unit_index"], data)
        for lithology in lithos:
            update_row(data[i], lithology)

