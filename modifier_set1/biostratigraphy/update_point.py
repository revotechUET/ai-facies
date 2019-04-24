from utilities import utils_func


def update_fluvial(row):
    points = []
    if int(row["Biostratigraphy"]) == 1:
        points = [6, 3, 1]
    elif int(row["Biostratigraphy"]) == 2:
        points = [4, 2, 1]
    elif int(row["Biostratigraphy"]) == 3:
        points = [2, 1, 0]
    elif int(row["Biostratigraphy"]) == 4:
        points = [-2, -1, 0]
    elif int(row["Biostratigraphy"]) == 5:
        points = ["x"]
    elif int(row["Biostratigraphy"]) == 6:
        points = ["x"]
    elif int(row["Biostratigraphy"]) == 7:
        points = ["x"]

    if len(points) > 0:
        if points[0] != "x":
            point = points[int(row["Reliability"]) - 1]
            for code in utils_func.get_group_depofacies("Fluvial"):
                name = utils_func.map_core_depofacies_code_to_name(code)
                if int(row[name]) > 0:
                    row.update({name: utils_func.handle_addition(int(row[name]) + int(point))})
        else:
            for code in utils_func.get_group_depofacies("Fluvial"):
                name = utils_func.map_core_depofacies_code_to_name(code)
                row.update({name: 0})

    return row


def update_shallow_lacustrine(row):
    points = []
    if int(row["Biostratigraphy"]) == 1:
        points = [-2, -1, 0]
    elif int(row["Biostratigraphy"]) == 2:
        points = [-2, -1, 0]
    elif int(row["Biostratigraphy"]) == 3:
        points = [6, 3, 1]
    elif int(row["Biostratigraphy"]) == 4:
        points = [-6, -3, -1]
    elif int(row["Biostratigraphy"]) == 5:
        points = ["x"]
    elif int(row["Biostratigraphy"]) == 6:
        points = ["x"]
    elif int(row["Biostratigraphy"]) == 7:
        points = ["x"]

    if len(points) > 0:
        if points[0] != "x":
            point = points[int(row["Reliability"]) - 1]
            for code in utils_func.get_group_depofacies("Shallow_Lacustrine"):
                name = utils_func.map_core_depofacies_code_to_name(code)
                if int(row[name]) > 0:
                    row.update({name: utils_func.handle_addition(int(row[name]) + int(point))})
        else:
            for code in utils_func.get_group_depofacies("Shallow_Lacustrine"):
                name = utils_func.map_core_depofacies_code_to_name(code)
                row.update({name: 0})

    return row


def update_deep_lacustrine(row):
    points = []
    if int(row["Biostratigraphy"]) == 1:
        points = [-6, -3, -1]
    elif int(row["Biostratigraphy"]) == 2:
        points = [-2, -1, 0]
    elif int(row["Biostratigraphy"]) == 3:
        points = [6, 3, 1]
    elif int(row["Biostratigraphy"]) == 4:
        points = [-6, -3, -1]
    elif int(row["Biostratigraphy"]) == 5:
        points = ["x"]
    elif int(row["Biostratigraphy"]) == 6:
        points = ["x"]
    elif int(row["Biostratigraphy"]) == 7:
        points = ["x"]

    if len(points) > 0:
        if points[0] != "x":
            point = points[int(row["Reliability"]) - 1]
            for code in utils_func.get_group_depofacies("Deep_Lacustrine"):
                name = utils_func.map_core_depofacies_code_to_name(code)
                if int(row[name]) > 0:
                    row.update({name: utils_func.handle_addition(int(row[name]) + int(point))})
        else:
            for code in utils_func.get_group_depofacies("Deep_Lacustrine"):
                name = utils_func.map_core_depofacies_code_to_name(code)
                row.update({name: 0})

    return row


def update_marginal_marine(row):
    points = []
    if int(row["Biostratigraphy"]) == 1:
        points = ["x"]
    elif int(row["Biostratigraphy"]) == 2:
        points = ["x"]
    elif int(row["Biostratigraphy"]) == 3:
        points = ["x"]
    elif int(row["Biostratigraphy"]) == 4:
        points = [3, 1, 0]
    elif int(row["Biostratigraphy"]) == 5:
        points = [3, 1, 0]
    elif int(row["Biostratigraphy"]) == 6:
        points = [3, 1, 0]
    elif int(row["Biostratigraphy"]) == 7:
        points = [-2, -1, 0]

    if len(points) > 0:
        if points[0] != "x":
            point = points[int(row["Reliability"]) - 1]
            for code in utils_func.get_group_depofacies("Marginal_Marine"):
                name = utils_func.map_core_depofacies_code_to_name(code)
                if int(row[name]) > 0:
                    row.update({name: utils_func.handle_addition(int(row[name]) + point)})
        else:
            for code in utils_func.get_group_depofacies("Marginal_Marine"):
                name = utils_func.map_core_depofacies_code_to_name(code)
                row.update({name: 0})

    return row


def update_shallow_marine(row):
    points = []
    if int(row["Biostratigraphy"]) == 1:
        points = ["x"]
    elif int(row["Biostratigraphy"]) == 2:
        points = ["x"]
    elif int(row["Biostratigraphy"]) == 3:
        points = ["x"]
    elif int(row["Biostratigraphy"]) == 4:
        points = [2, 1, 0]
    elif int(row["Biostratigraphy"]) == 5:
        points = [3, 1, 0]
    elif int(row["Biostratigraphy"]) == 6:
        points = [6, 3, 1]
    elif int(row["Biostratigraphy"]) == 7:
        points = [3, 1, 0]

    if len(points) > 0:
        if points[0] != "x":
            point = points[int(row["Reliability"]) - 1]
            for code in utils_func.get_group_depofacies("Shallow_Marine"):
                name = utils_func.map_core_depofacies_code_to_name(code)
                if int(row[name]) > 0:
                    row.update({name: utils_func.handle_addition(int(row[name]) + point)})
        else:
            for code in utils_func.get_group_depofacies("Shallow_Marine"):
                name = utils_func.map_core_depofacies_code_to_name(code)
                row.update({name: 0})

    return row


def update_deep_marine(row):
    points = []
    if int(row["Biostratigraphy"]) == 1:
        points = ["x"]
    elif int(row["Biostratigraphy"]) == 2:
        points = ["x"]
    elif int(row["Biostratigraphy"]) == 3:
        points = ["x"]
    elif int(row["Biostratigraphy"]) == 4:
        points = [0, 0, 0]
    elif int(row["Biostratigraphy"]) == 5:
        points = [-4, -2, 0]
    elif int(row["Biostratigraphy"]) == 6:
        points = [3, 1, 0]
    elif int(row["Biostratigraphy"]) == 7:
        points = [6, 3, 1]

    if len(points) > 0:
        if points[0] != "x":
            point = points[int(row["Reliability"]) - 1]
            for code in utils_func.get_group_depofacies("Deep_Marine"):
                name = utils_func.map_core_depofacies_code_to_name(code)
                if int(row[name]) > 0:
                    row.update({name: utils_func.handle_addition(int(row[name]) + point)})
        else:
            for code in utils_func.get_group_depofacies("Deep_Marine"):
                name = utils_func.map_core_depofacies_code_to_name(code)
                row.update({name: 0})

    return row
