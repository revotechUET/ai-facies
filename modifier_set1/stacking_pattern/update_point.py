from utilities import utils_func


# AG 1
# FU 3
# CU 2
def update_fluvial(row):
    point = 0
    if int(row["Stacking_pattern"]) == 1:
        point = 3
    elif int(row["Stacking_pattern"]) == 2:
        point = -3

    codes = utils_func.get_group_depofacies("Fluvial")
    for code in codes:
        name = utils_func.map_core_depofacies_code_to_name(code)
        if int(row[name]) > 0:
            row.update({name: utils_func.handle_addition(int(row[name]) + point)})


def update_shallow_lacustrine(row):
    point = 0
    if int(row["Stacking_pattern"]) == 1:
        point = 3
    elif int(row["Stacking_pattern"]) == 2:
        point = 3

    codes = utils_func.get_group_depofacies("Shallow_Lacustrine")
    for code in codes:
        name = utils_func.map_core_depofacies_code_to_name(code)
        if int(row[name]) > 0:
            row.update({name: utils_func.handle_addition(int(row[name]) + point)})


def update_deep_lacustrine(row):
    point = -3
    if int(row["Stacking_pattern"]) == 1:
        point = 0
    elif int(row["Stacking_pattern"]) == 2:
        point = 3

    codes = utils_func.get_group_depofacies("Deep_Lacustrine")
    for code in codes:
        name = utils_func.map_core_depofacies_code_to_name(code)
        if int(row[name]) > 0:
            row.update({name: utils_func.handle_addition(int(row[name]) + point)})


def update_marginal_marine(row):
    point = 0
    if int(row["Stacking_pattern"]) == 1:
        point = 3
    elif int(row["Stacking_pattern"]) == 2:
        point = 3

    codes = utils_func.get_group_depofacies("Marginal_Marine")
    for code in codes:
        name = utils_func.map_core_depofacies_code_to_name(code)
        if int(row[name]) > 0:
            row.update({name: utils_func.handle_addition(int(row[name]) + point)})


def update_shallow_marine(row):
    point = 0
    if int(row["Stacking_pattern"]) == 1:
        point = 3
    elif int(row["Stacking_pattern"]) == 2:
        point = 3

    codes = utils_func.get_group_depofacies("Shallow_Marine")
    for code in codes:
        name = utils_func.map_core_depofacies_code_to_name(code)
        if int(row[name]) > 0:
            row.update({name: utils_func.handle_addition(int(row[name]) + point)})


def update_deep_marine(row):
    point = 0
    if int(row["Stacking_pattern"]) == 1:
        point = 0
    elif int(row["Stacking_pattern"]) == 2:
        point = 0

    codes = utils_func.get_group_depofacies("Deep_Marine")
    for code in codes:
        name = utils_func.map_core_depofacies_code_to_name(code)
        if int(row[name]) > 0:
            row.update({name: utils_func.handle_addition(int(row[name]) + point)})
