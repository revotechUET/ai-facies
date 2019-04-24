from utilities import utils_func


def find_max_curve(row):
    max_value = 0
    lst = []
    for name in utils_func.NAMES:
        if int(row[name]) > max_value:
            max_value = int(row[name])

    if max_value > 0:
        for name in utils_func.NAMES:
            if int(row[name]) == max_value:
                lst.append({name: max_value})
    return lst


def find_max_radius_30(unit_index, data):
    unit_index = int(unit_index)
    lst = []

    if len(data[unit_index]["Special_lithology"]) > 0:
        return lst

    for i in range(unit_index, -1, -1):
        if abs(float(data[i]["TVD"]) - float(
                data[unit_index]["TVD"])) <= 30 and not len(data[i]["Special_lithology"]):
            lst.extend(find_max_curve(data[i]))
        else:
            break

    for i in range(unit_index + 1, len(data), 1):
        if abs(float(data[i]["TVD"]) - float(
                data[unit_index]["TVD"])) <= 30 and not len(data[i]["Special_lithology"]):
            lst.extend(find_max_curve(data[i]))
        else:
            break

    return lst


def divide_group(data):
    lst = []
    lst.append({"name": "Fluvial", "occurrence": 0, "points": 0})
    lst.append({"name": "Marginal_Marine", "occurrence": 0, "points": 0})
    lst.append({"name": "Shallow_Marine", "occurrence": 0, "points": 0})
    lst.append({"name": "Deep_Marine", "occurrence": 0, "points": 0})
    lst.append({"name": "Shallow_Lacustrine", "occurrence": 0, "points": 0})
    lst.append({"name": "Deep_Lacustrine", "occurrence": 0, "points": 0})

    for item in data:
        facy_name = None
        for key in item.keys():
            facy_name = key
        group_name = utils_func.get_group_name(facy_name)
        for l in lst:
            if l["name"] == group_name:
                l["occurrence"] += 1
                l["points"] += int(item[facy_name])

    return lst


def pick_group(data):
    idx = 0
    for i in range(len(data)):
        if int(data[i - idx]["occurrence"]) == 0:
            data.pop(i - idx)
            idx += 1
    if len(data) == 0:
        return data

    lst = sorted(data, key=lambda k: (k["occurrence"], k["points"]), reverse=True)

    return lst


def update_most_abundant(row, group):
    points = []
    if group["name"] == "Fluvial":
        points = [2, 0, -1, 0, -1, -2]

    if group["name"] == "Shallow_Lacustrine":
        points = [0, 2, 0, -1, -1, -2]

    if group["name"] == "Deep_Lacustrine":
        points = [-1, 0, 2, -2, -2, -2]

    if group["name"] == "Marginal_Marine":
        points = [0, -1, -2, 2, 0, -1]

    if group["name"] == "Shallow_Marine":
        points = [-1, -1, -2, 0, 2, 0]

    if group["name"] == "Deep_Marine":
        points = [-2, -1, -2, -1, 0, 2]

    for i in range(len(points)):
        utils_func.update_row_group(utils_func.GROUPS[i], row, points[i])


def update_second_most_abundant(row, group):
    points = []
    if group["name"] == "Fluvial":
        points = [1, 0, 0, 0, 0, -2]

    if group["name"] == "Shallow_Lacustrine":
        points = [0, 1, 0, 0, -1, -2]

    if group["name"] == "Deep_Lacustrine":
        points = [0, 0, 1, 1, -2, -2]

    if group["name"] == "Marginal_Marine":
        points = [0, 0, 1, 1, 0, -1]

    if group["name"] == "Shallow_Marine":
        points = [0, -1, -2, 0, 1, 0]

    if group["name"] == "Deep_Marine":
        points = [-2, -2, -2, -1, 0, 1]

    for i in range(len(points)):
        utils_func.update_row_group(utils_func.GROUPS[i], row, points[i])


def update_third_most_abundant(row, group):
    points = []
    if group["name"] == "Fluvial":
        points = [0, 0, 0, 0, 0, -1]

    if group["name"] == "Shallow_Lacustrine":
        points = [0, 0, 1, 0, 0, -1]

    if group["name"] == "Deep_Lacustrine":
        points = [0, 1, 0, 0, 0, -1]

    if group["name"] == "Marginal_Marine":
        points = [0, 0, 0, 0, 0, 0]

    if group["name"] == "Shallow_Marine":
        points = [0, 0, 0, 0, 0, 0]

    if group["name"] == "Deep_Marine":
        points = [-1, -1, -1, 0, 0, 0]

    for i in range(len(points)):
        utils_func.update_row_group(utils_func.GROUPS[i], row, points[i])


def update_4_6_most_abundant(row, group):
    points = []
    if group["name"] == "Fluvial":
        points = [-2, 0, 0, 0, 0, 0]

    if group["name"] == "Shallow_Lacustrine":
        points = [0, -2, 0, 0, 0, 0]

    if group["name"] == "Deep_Lacustrine":
        points = [0, 0, -2, 0, 0, 0]

    if group["name"] == "Marginal_Marine":
        points = [0, 0, 0, -2, 0, 0]

    if group["name"] == "Shallow_Marine":
        points = [0, 0, 0, 0, -2, 0]

    if group["name"] == "Deep_Marine":
        points = [0, 0, 0, 0, 0, -2]

    for i in range(len(points)):
        utils_func.update_row_group(utils_func.GROUPS[i], row, points[i])


def update_row(row, groups):
    if len(groups) > 0:
        update_most_abundant(row, groups[0])

    if len(groups) > 1:
        update_second_most_abundant(row, groups[1])

    if len(groups) > 2:
        update_third_most_abundant(row, groups[2])

    if len(groups) > 3:
        for i in range(3, len(groups)):
            update_4_6_most_abundant(row, groups[i])


def associated_facies(data, it):
    for row in reversed(data):
        groups = pick_group(divide_group(find_max_radius_30(row["Unit_index"], data)))
        tmp = []
        for item in groups:
            tmp.append(item["name"])
        if len(groups) > 0:
            update_row(row, groups)
            row.update({"Facies_group": tmp})

    utils_func.export_to_csv(data, f"csv/associated_facies{it}.csv")
