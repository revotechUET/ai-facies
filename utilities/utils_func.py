from csv import DictWriter
from copy import deepcopy
from collections import Counter

CODE_TO_NAME = {
    "1.1": "Alluvial_Fan",
    "1.2": "Fluvial_Channel",
    "1.3": "Fluvial_Point_Bar",
    "1.4": "Levee",
    "1.5": "Crevasse_Splay",
    "1.6": "Fluvial_Floodplain",
    "2.1": "Progradational_Lacustrine_Delta",
    "2.2": "Lacustrine_Fan_Delta",
    "2.3": "Progradational_Lacustrine_Shoreface",
    "2.4": "Transgressive_Lacustrine_Shoreface",
    "2.5": "Aggradational_Lacustrine_Shoreface",
    "2.6": "Lacustrine_Offshore_Transition",
    "2.7": "Lacustrine_Shelf",
    "3.1": "Proximal_Sub-Lacustrine_Fan",
    "3.2": "Distal_Sub-Lacustrine_Fan",
    "3.3": "Lacustrine_Turbidite",
    "3.4": "Distal_Lacustrine_Turbidites",
    "3.5": "Lacustrine_Deepwater",
    "4.1": "Marine_Delta",
    "4.2": "Marine_Fan_Delta",
    "4.3": "Tidal_Channel_And_Sand_Flat",
    "4.4": "Sandy_Tidal_Flat",
    "4.5": "Mixed_Tidal_Flat",
    "4.6": "Muddy_Tidal_Flat",
    "4.7": "Lagoon",
    "5.1": "Progradational_Marine_Shoreface",
    "5.2": "Transgressive_Marine_Shoreface",
    "5.3": "Aggradational_Marine_Shoreface",
    "5.4": "Marine_Offshore_Transition",
    "5.5": "Marine_Shelf",
    "6.1": "Proximal_Submarine_Fan",
    "6.2": "Distal_Submarine_Fan",
    "6.3": "Marine_Turbidite",
    "6.4": "Distal_Marine_Turbidites",
    "6.5": "Marine_Deepwater"
}

GROUP_TO_FACIES = {
    "Fluvial": ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6"],
    "Shallow_Lacustrine": ["2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7"],
    "Deep_Lacustrine": ["3.1", "3.2", "3.3", "3.4", "3.5"],
    "Marginal_Marine": ["4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7"],
    "Shallow_Marine": ["5.1", "5.2", "5.3", "5.4", "5.5"],
    "Deep_Marine": ["6.1", "6.2", "6.3", "6.4", "6.5"]
}

NAMES = [
    "Alluvial_Fan",
    "Fluvial_Channel",
    "Fluvial_Point_Bar",
    "Levee",
    "Crevasse_Splay",
    "Fluvial_Floodplain",
    "Progradational_Lacustrine_Delta",
    "Lacustrine_Fan_Delta",
    "Progradational_Lacustrine_Shoreface",
    "Transgressive_Lacustrine_Shoreface",
    "Aggradational_Lacustrine_Shoreface",
    "Lacustrine_Offshore_Transition",
    "Lacustrine_Shelf",
    "Proximal_Sub-Lacustrine_Fan",
    "Distal_Sub-Lacustrine_Fan",
    "Lacustrine_Turbidite",
    "Distal_Lacustrine_Turbidites",
    "Lacustrine_Deepwater",
    "Marine_Delta",
    "Marine_Fan_Delta",
    "Tidal_Channel_And_Sand_Flat",
    "Sandy_Tidal_Flat",
    "Mixed_Tidal_Flat",
    "Muddy_Tidal_Flat",
    "Lagoon",
    "Progradational_Marine_Shoreface",
    "Transgressive_Marine_Shoreface",
    "Aggradational_Marine_Shoreface",
    "Marine_Offshore_Transition",
    "Marine_Shelf",
    "Proximal_Submarine_Fan",
    "Distal_Submarine_Fan",
    "Marine_Turbidite",
    "Distal_Marine_Turbidites",
    "Marine_Deepwater"
]

GROUPS = [
    "Fluvial",
    "Shallow_Lacustrine",
    "Deep_Lacustrine",
    "Marginal_Marine",
    "Shallow_Marine",
    "Deep_Marine"
]

UNDEFINED = "-9999"


def convert_name_to_number(data):
    tmp = deepcopy(CODE_TO_NAME)
    tmp.update({"0": "unknown"})
    for row in data:
        for key, value in row.items():
            if value in tmp.values():
                code = list(tmp.keys())[list(tmp.values()).index(value)]
                row.update({key: code})


def remove_duplicate(arr):
    arr.sort()
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            arr.pop(i)
            i -= 1
        i += 1
    return arr


def map_core_depofacies_code_to_name(code):
    try:
        return CODE_TO_NAME[code]
    except KeyError:
        return None


def convert_string_to_array(string):
    return string[1:-1].split(", ") if string != '[]' else []


def get_group_depofacies(name):
    try:
        return GROUP_TO_FACIES[name]
    except KeyError:
        return None


def get_group_name(facy_name):
    for key, item in CODE_TO_NAME.items():
        if item == facy_name:
            facy_code = key

    for key, item in GROUP_TO_FACIES.items():
        if facy_code in item:
            return key


def get_max_by_key(key, data):
    lst = []
    max = 0
    for item in data:
        if int(item[key]) > max:
            max = item[key]
    for item in data:
        if int(item[key]) == max:
            lst.append(item)
    return lst


def update_row_group(group_name, row, point):
    for depofacy in get_group_depofacies(group_name):
        name = map_core_depofacies_code_to_name(depofacy)
        if int(row[name]) > 0:
            if point == "x":
                row.update({name: 0})
            else:
                row.update({name: handle_addition(int(row[name]) + point)})


def convert_unit_by_unit(data):
    lst = []
    lithos = []
    depos = []
    for i in range(0, len(data)):
        if data[i]["Special_lithology"] != UNDEFINED:
            lithos.append(float(data[i]["Special_lithology"]))
        if data[i]["Core_depofacies"] != UNDEFINED:
            depos.append((float(data[i]["Core_depofacies"])))
        if data[i]["Boundary_flag"] == "1":
            final_litho = deepcopy(remove_duplicate(lithos))
            final_depos = deepcopy(remove_duplicate(depos))
            data[i].update({"Special_lithology": final_litho, "Core_depofacies": final_depos})
            lst.append(data[i])
            lithos.clear()
            depos.clear()

    return lst


def contain_special_lithology(litho):
    if len(litho) > 0:
        return True
    return False


def get_key(lst, i):
    return [key for key in lst[i].keys()][0]


def calculate_uncertainty(row):
    if row["Most"] == "unknown" or not row["Most"]:
        return 1

    if row["Second_Most"] and row["Second_Most"] != "unknown" and float(row[row["Most"]]) - float(
            row[row["Second_Most"]]) < 0.1:
        return 1

    if row["Most"] and float(row[row["Most"]]) < 0.3:
        return 1

    return 0


def convert_data(data):
    curve = ["Most", "Second_Most", "Third_Most"]
    prob = ["Most_Prob", "Second_Most_Prob", "Third_Most_Prob"]

    for row in data:
        total = 0
        for key, value in CODE_TO_NAME.items():
            total += int(row[value])
        row.update({"Sum": total})

    for row in data:
        for key, value in CODE_TO_NAME.items():
            if int(row["Sum"]) != 0:
                row.update({value: float(row[value]) / float(row["Sum"])})

    for row in data:
        lst = []
        for key, value in CODE_TO_NAME.items():
            if float(row[value]) != 0:
                lst.append({value: float(row[value])})
        lst = sorted(lst, key=lambda it: it[[key for key in it.keys()][0]], reverse=True)
        for i in range(len(lst) - 1):
            if lst[i][get_key(lst, i)] == lst[i + 1][get_key(lst, i + 1)]:
                lst[i][get_key(lst, i)] = "unknown"
                lst[i + 1][get_key(lst, i + 1)] = "unknown"

        for i in range(len(curve)):
            if len(lst) > i:
                name = [key for key in lst[i].keys()][0]
                if row["Special_lithology"] != UNDEFINED:
                    row.update({curve[i]: ""})
                    row.update({prob[i]: ""})

                else:
                    row.update({curve[i]: name})
                    row.update({prob[i]: row[name]})
            else:
                row.update({curve[i]: ""})
                row.update({prob[i]: ""})

            if i == 2:
                break

    for row in data:
        row.update({"Uncertainty_flag": calculate_uncertainty(row)})

    convert_name_to_number(data)


def export_to_csv(data, filename):
    headers = []
    for row in data:
        for key in row.keys():
            if key not in headers:
                headers.append(key)
    with open(filename, "w") as o_file:
        csv_writer = DictWriter(o_file, fieldnames=headers)
        csv_writer.writeheader()
        for row in data:
            csv_writer.writerow(row)


def pick_most(data):
    if len(data) == 0:
        return None
    return sorted(data, key=Counter(data).get, reverse=True)[0]


def handle_addition(point):
    return point if int(point) >= 0 else 0


def simplify_data(data):
    core_depofacies = []
    biostrats = []
    reliabilities = []
    laterals = []
    special_lithologies = []

    simplified_data = []

    for row in data:
        if row["Core_depofacies"] != UNDEFINED:
            core_depofacies.append(row["Core_depofacies"])

        if row["Reliability"] != UNDEFINED:
            reliabilities.append(row["Reliability"])

        if row["Biostratigraphy"] != UNDEFINED:
            biostrats.append(row["Biostratigraphy"])

        if row["Special_lithology"] != UNDEFINED:
            special_lithologies.append(row["Special_lithology"])

        if row["Lateral_proximity"] != UNDEFINED:
            laterals.append(row["Lateral_proximity"])

        if int(row["Boundary_flag"]) == 1:
            depo = pick_most(core_depofacies)
            biostrat = pick_most(biostrats)
            reliability = pick_most(reliabilities)
            lateral = pick_most(laterals)
            lithos = remove_duplicate(deepcopy(special_lithologies))

            depo = depo if depo else UNDEFINED
            biostrat = biostrat if biostrat else UNDEFINED
            reliability = reliability if reliability else UNDEFINED
            lateral = lateral if lateral else UNDEFINED

            row.update({"Special_lithology": lithos})

            row.update({"Core_depofacies": depo})

            row.update({"Biostratigraphy": biostrat})

            row.update({"Reliability": reliability})

            row.update({"Lateral_proximity": lateral})

            simplified_data.append(deepcopy(row))
            core_depofacies.clear()
            special_lithologies.clear()

    return simplified_data
