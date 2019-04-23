from utilities import utils_func


def find_max_curve(row):
    max = 0
    lst = []
    for name in utils_func.NAMES:
        if int(row[name]) > max:
            max = int(row[name])

    if max > 0:
        for name in utils_func.NAMES:
            if int(row[name]) == max:
                lst.append({name: max})
    return lst


def find_max_lower(unit_index, data):
    unit_index = int(unit_index)
    lst = []

    if unit_index == len(data) - 1 or len(data[unit_index]["Special_lithology"]) > 0 or len(
            data[unit_index + 1]["Special_lithology"]) > 0:
        return lst

    lst.extend(find_max_curve(data[unit_index + 1]))

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
    if len(data) == 1:
        return data[0]
    return None


def update_row(row, group):
    points = []
    sharp_boundary = int(row["Sharp_boundary"])

    if group["name"] == "Fluvial":
        points = [[2, 2], [-1, -1], [-2, 0], [-1, 0], [-1, 0], ["x", -3]]

    if group["name"] == "Shallow_Lacustrine":
        points = [[-1, 0], [2, 2], [-1, -1], [0, 0], [0, 0], ["x", -3]]

    if group["name"] == "Deep_Lacustrine":
        points = [[-2, -1], [2, 1], [2, 2], ["x", -3], ["x", -3], ["x", -4]]

    if group["name"] == "Marginal_Marine":
        points = [["x", 0], ["x", -2], ["x", -2], [2, 2], [1, 1], [0, 0]]

    if group["name"] == "Shallow_Marine":
        points = [["x", -2], ["x", -2], ["x", "x"], [1, 1], [2, 2], [1, 1]]

    if group["name"] == "Deep_Marine":
        points = [["x", -3], ["x", "x"], ["x", "x"], [-1, 1], [1, 1], [2, 2]]

    for i in range(len(points)):
        utils_func.update_row_group(utils_func.GROUPS[i], row, points[i][sharp_boundary])


def lower_boundary(data, iter):
    for row in reversed(data):
        group = pick_group(divide_group(find_max_lower(row["Unit_index"], data)))
        if group:
            update_row(row, group)
            row.update({"Facies_below": group["name"] if group else None})

    utils_func.export_to_csv(data, f"csv/lower_boundary{iter}.csv")
