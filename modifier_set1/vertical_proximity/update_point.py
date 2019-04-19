from utilities import utils_func


def get_idx(number_of_similar_unit):
    number_of_similar_unit = int(number_of_similar_unit)
    if number_of_similar_unit == 0:
        return 0
    elif number_of_similar_unit in [1, 2]:
        return 1
    elif number_of_similar_unit in [3, 4, 5]:
        return 2
    elif number_of_similar_unit > 5:
        return 3


def update_alluvial_fan(data_set):
    curve_name = "Alluvial_Fan"
    if data_set[curve_name] == 0:
        return 0
    points = [-1, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_fluvial_channel(data_set):
    curve_name = "Fluvial_Channel"
    if data_set[curve_name] == 0:
        return 0
    points = [-2, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_fluvial_point_bar(data_set):
    curve_name = "Fluvial_Point_Bar"
    if data_set[curve_name] == 0:
        return 0
    points = [-2, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_levee(data_set):
    curve_name = "Levee"
    if data_set[curve_name] == 0:
        return 0
    points = [-1, 1, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_crevasse_splay(data_set):
    curve_name = "Crevasse_Splay"
    if data_set[curve_name] == 0:
        return 0
    points = [-1, 1, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_fluvial_floodplain(data_set):
    curve_name = "Fluvial_Floodplain"
    if data_set[curve_name] == 0:
        return 0
    points = [-3, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_progradational_lacustrine_delta(data_set):
    curve_name = "Progradational_Lacustrine_Delta"
    if data_set[curve_name] == 0:
        return 0
    points = [-3, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_lacustrine_fan_delta(data_set):
    curve_name = "Lacustrine_Fan_Delta"
    if data_set[curve_name] == 0:
        return 0
    points = [-2, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_progradational_lacustrine_shoreface(data_set):
    curve_name = "Progradational_Lacustrine_Shoreface"
    if data_set[curve_name] == 0:
        return 0
    points = [-2, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_transgressive_lacustrine_shoreface(data_set):
    curve_name = "Transgressive_Lacustrine_Shoreface"
    if data_set[curve_name] == 0:
        return 0
    points = [-1, 1, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_aggradational_lacustrine_shoreface(data_set):
    curve_name = "Aggradational_Lacustrine_Shoreface"
    if data_set[curve_name] == 0:
        return 0
    points = [-2, 1, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_lacustrine_offshore_transition(data_set):
    curve_name = "Lacustrine_Offshore_Transition"
    if data_set[curve_name] == 0:
        return 0
    points = [-1, 1, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_lacustrine_shelf(data_set):
    curve_name = "Lacustrine_Shelf"
    if data_set[curve_name] == 0:
        return 0
    points = [-2, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_proximal_sub_lacustrine_fan(data_set):
    curve_name = "Proximal_Sub-Lacustrine_Fan"
    if data_set[curve_name] == 0:
        return 0
    points = [-1, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_distal_sub_lacustrine_fan(data_set):
    curve_name = "Distal_Sub-Lacustrine_Fan"
    if data_set[curve_name] == 0:
        return 0
    points = [-1, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_lacustrine_turbidite(data_set):
    curve_name = "Lacustrine_Turbidite"
    if data_set[curve_name] == 0:
        return 0
    points = [-2, 1, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_distal_lacustrine_turbidites(data_set):
    curve_name = "Distal_Lacustrine_Turbidites"
    if data_set[curve_name] == 0:
        return 0
    points = [-2, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_lacustrine_deepwater(data_set):
    curve_name = "Lacustrine_Deepwater"
    if data_set[curve_name] == 0:
        return 0
    points = [-3, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_marine_delta(data_set):
    curve_name = "Marine_Delta"
    if data_set[curve_name] == 0:
        return 0
    points = [-3, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_marine_fan_delta(data_set):
    curve_name = "Marine_Fan_Delta"
    if data_set[curve_name] == 0:
        return 0
    points = [-2, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_tidal_channel_and_sand_flat(data_set):
    curve_name = "Tidal_Channel_And_Sand_Flat"
    if data_set[curve_name] == 0:
        return 0
    points = [-1, 1, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_sandy_tidal_flat(data_set):
    curve_name = "Sandy_Tidal_Flat"
    if data_set[curve_name] == 0:
        return 0
    points = [-1, 1, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_mixed_tidal_flat(data_set):
    curve_name = "Mixed_Tidal_Flat"
    if data_set[curve_name] == 0:
        return 0
    points = [-1, 1, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_muddy_tidal_flat(data_set):
    curve_name = "Muddy_Tidal_Flat"
    if data_set[curve_name] == 0:
        return 0
    points = [-1, 1, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_lagoon(data_set):
    curve_name = "Lagoon"
    if data_set[curve_name] == 0:
        return 0
    points = [-2, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_progradational_marine_shoreface(data_set):
    curve_name = "Progradational_Marine_Shoreface"
    if data_set[curve_name] == 0:
        return 0
    points = [-2, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_transgressive_marine_shoreface(data_set):
    curve_name = "Transgressive_Marine_Shoreface"
    if data_set[curve_name] == 0:
        return 0
    points = [-1, 1, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_aggradational_marine_shoreface(data_set):
    curve_name = "Aggradational_Marine_Shoreface"
    if data_set[curve_name] == 0:
        return 0
    points = [-2, 1, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_marine_offshore_transition(data_set):
    curve_name = "Marine_Offshore_Transition"
    if data_set[curve_name] == 0:
        return 0
    points = [-1, 1, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_marine_shelf(data_set):
    curve_name = "Marine_Shelf"
    if data_set[curve_name] == 0:
        return 0
    points = [-2, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_proximal_submarine_fan(data_set):
    curve_name = "Proximal_Submarine_Fan"
    if data_set[curve_name] == 0:
        return 0
    points = [-1, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_distal_submarine_fan(data_set):
    curve_name = "Distal_Submarine_Fan"
    if data_set[curve_name] == 0:
        return 0
    points = [-1, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_marine_turbidite(data_set):
    curve_name = "Marine_Turbidite"
    if data_set[curve_name] == 0:
        return 0
    points = [-2, 1, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_distal_marine_turbidites(data_set):
    curve_name = "Distal_Marine_Turbidites"
    if data_set[curve_name] == 0:
        return 0
    points = [-2, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))


def update_marine_deepwater(data_set):
    curve_name = "Marine_Deepwater"
    if data_set[curve_name] == 0:
        return 0
    points = [-3, 0, 2, 3]
    return utils_func.handle_addition(
        points[get_idx(data_set["Number_of_similar_units_50"])] + int(data_set[curve_name]))
