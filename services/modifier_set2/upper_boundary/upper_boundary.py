from ...utilities import utils_func


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


def find_max_upper(unit_index, data):
    unit_index = int(unit_index)
    lst = []

    if unit_index == 0 or len(data[unit_index]["Special_lithology"]) > 0 or len(
            data[unit_index - 1]["Special_lithology"]) > 0:
        return lst

    lst.extend(find_max_curve(data[unit_index - 1]))

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
        points = [[-2, -1], [2, 1], [2, 2], [-6, -3], [-6, -3], ["x", -4]]

    if group["name"] == "Marginal_Marine":
        points = [[-1, 0], [-2, -2], [-8, -2], [2, 2], [1, 1], [0, 0]]

    if group["name"] == "Shallow_Marine":
        points = [[-5, -2], [-3, -2], [-8], [1, 1], [2, 2], [1, 1]]

    if group["name"] == "Deep_Marine":
        points = [[-7, -3], [-6, -6], ["x", "x"], [-1, 1], [0, 1], [2, 2]]

    for i in range(len(points)):
        utils_func.update_row_group(utils_func.GROUPS[i], row, points[i][sharp_boundary])


def upper_boundary(data, it):
    for row in reversed(data):
        group = pick_group(divide_group(find_max_upper(row["Unit_index"], data)))
        if group:
            update_row(row, group)
            row.update({"Facies_above": group["name"] if group else None})

    utils_func.export_to_csv(data, f"csv/upper_boundary{it}.csv")
