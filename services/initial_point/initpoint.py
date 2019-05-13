def init_alluvial_fan(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 5
            elif u_thick >= 4:
                point = 4
            else:
                point = 3
    return point


def init_marine_fan_delta(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 15:
            if u_thick >= 10:
                point = 6
            elif u_thick >= 5:
                point = 5
            else:
                point = 4
    return point


def init_lacustrine_fan_delta(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 15:
            if u_thick >= 10:
                point = 6
            elif u_thick >= 5:
                point = 5
            else:
                point = 4
    return point


def init_marine_delta(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 15:
            if u_thick >= 10:
                point = 7
            elif u_thick >= 5:
                point = 6
            else:
                point = 5
    return point


def init_progradational_lacustrine_delta(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 15:
            if u_thick >= 10:
                point = 7
            elif u_thick >= 5:
                point = 6
            else:
                point = 5
    return point


def init_progradational_marine_shoreface(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 6
            elif u_thick >= 4:
                point = 5
            else:
                point = 4

    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                return additional_point + 6
            elif u_thick >= 3:
                return additional_point + 5
            else:
                return additional_point + 4
    return point


def init_progradational_lacustrine_shoreface(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 5
            elif u_thick >= 5:
                point = 6
            else:
                point = 4
    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 5
            elif u_thick >= 3:
                point = 4
            else:
                point = 3
    return point


def init_proximal_sub_lacustrine_fan(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 10 <= u_thick < 30:
            if u_thick >= 22:
                point = 6
            elif u_thick >= 15:
                point = 5
            else:
                point = 4

    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 5 <= u_thick < 30:
            if u_thick >= 20:
                point = 5
            elif u_thick >= 12:
                point = 4
            else:
                point = 3
    return point


def init_proximal_submarine_fan(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 10 <= u_thick < 50:
            if u_thick >= 25:
                point = 7
            elif u_thick >= 15:
                point = 6
            else:
                point = 5

    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 5 <= u_thick < 50:
            if u_thick >= 25:
                point = 6
            elif u_thick >= 15:
                point = 5
            else:
                point = 4
    return point


def init_fluvial_channel(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 1:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 5
            elif u_thick >= 3:
                point = 6
            else:
                point = 3

    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 2:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 5
            elif u_thick >= 3:
                point = 6
            else:
                point = 3

    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 1:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 5
            elif u_thick >= 3:
                point = 6
            else:
                point = 3

    return point


def init_fluvial_point_bar(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 1:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 5
            elif u_thick >= 3:
                point = 6
            else:
                point = 3

    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 1:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 5
            elif u_thick >= 3:
                point = 6
            else:
                point = 3
    return point


def init_levee(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 1:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 2
            elif u_thick >= 3:
                point = 3
            else:
                point = 4
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 2:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 2
            elif u_thick >= 3:
                point = 3
            else:
                point = 4

    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 1:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 3
            elif u_thick >= 3:
                point = 4
            else:
                point = 5

    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 2:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 3
            elif u_thick >= 3:
                point = 4
            else:
                point = 5
    return point


def init_crevasse_splay(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 1:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 5:
            if u_thick >= 4:
                point = 2
            elif u_thick >= 2:
                point = 3
            else:
                point = 5
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 2:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 5:
            if u_thick >= 4:
                point = 2
            elif u_thick >= 2:
                point = 3
            else:
                point = 5
    return point


def init_tidal_channel_and_sand_flat(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 1:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 5:
            if u_thick >= 4:
                point = 3
            elif u_thick >= 2:
                point = 4
            else:
                point = 5
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 2:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 5:
            if u_thick >= 4:
                point = 3
            elif u_thick >= 2:
                point = 4
            else:
                point = 5
    return point


def init_transgressive_lacustrine_shoreface(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 1:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 4
            elif u_thick >= 3:
                point = 6
            else:
                point = 3

    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 1:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 4
            elif u_thick >= 3:
                point = 6
            else:
                point = 3
    return point


def init_transgressive_marine_shoreface(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 1:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 4
            elif u_thick >= 3:
                point = 6
            else:
                point = 3
    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 1:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 4
            elif u_thick >= 3:
                point = 6
            else:
                point = 3
    return point


def init_lacustrine_turbidite(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 1:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 5:
            if u_thick >= 4:
                point = 2
            elif u_thick >= 2:
                point = 3
            else:
                point = 4
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 2:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 5:
            if u_thick >= 4:
                point = 2
            elif u_thick >= 2:
                point = 3
            else:
                point = 4

    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 1:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 5:
            if u_thick >= 4:
                point = 2
            elif u_thick >= 2:
                point = 3
            else:
                point = 4

    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 2:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 5:
            if u_thick >= 4:
                point = 2
            elif u_thick >= 2:
                point = 3
            else:
                point = 4
    return point


def init_marine_turbidite(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 1:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 3
            elif u_thick >= 3:
                point = 4
            else:
                point = 5

    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 2:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 5:
            if u_thick >= 4:
                point = 3
            elif u_thick >= 2:
                point = 4
            else:
                point = 5

    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 1:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 3
            elif u_thick >= 3:
                point = 4
            else:
                point = 5

    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 2:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 3
            elif u_thick >= 3:
                point = 4
            else:
                point = 5
    return point


def init_aggradational_lacustrine_shoreface(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 2:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 4
            elif u_thick >= 3:
                point = 3
            else:
                point = 2

    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 2:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 5:
            if u_thick >= 3:
                point = 4
            else:
                point = 5

    return point


def init_aggradational_marine_shoreface(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 1 and data_set["GR_shape_code"] == 2:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 6
            elif u_thick >= 3:
                point = 5
            else:
                point = 4

    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 2:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 5:
            if u_thick >= 3:
                point = 4
            else:
                point = 5

    return point


def init_sandy_tidal_flat(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 1:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 5:
            if u_thick >= 4:
                point = 3
            elif u_thick >= 2:
                point = 4
            else:
                point = 5

    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 2:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 5:
            if u_thick >= 4:
                point = 3
            elif u_thick >= 2:
                point = 4
            else:
                point = 5
    return point


def init_lacustrine_offshore_transition(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 3:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 2
            elif u_thick >= 3:
                point = 3
            else:
                point = 4

    if data_set["Lithofacies_major"] == 3 and data_set["GR_shape_code"] == 3:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            point = 4

    return point


def init_marine_offshore_transition(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 3:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 4
            elif u_thick >= 3:
                point = 5
            else:
                point = 4
    if data_set["Lithofacies_major"] == 3 and data_set["GR_shape_code"] == 3:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            point = 5

    return point


def init_distal_lacustrine_turbidites(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 3:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 4
            elif u_thick >= 3:
                point = 5
            else:
                point = 4

    if data_set["Lithofacies_major"] == 3 and data_set["GR_shape_code"] == 3:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            point = 4

    return point


def init_distal_marine_turbidites(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 2 and data_set["GR_shape_code"] == 3:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                point = 6
            elif u_thick >= 3:
                point = 5
            else:
                point = 4

    if data_set["Lithofacies_major"] == 3 and data_set["GR_shape_code"] == 3:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 10:
            point = 5

    return point


def init_fluvial_floodplain(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 3 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 5

    if data_set["Lithofacies_major"] == 3 and data_set["GR_shape_code"] in [1, 2]:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 5

    if data_set["Lithofacies_major"] == 4 and data_set["GR_shape_code"] == 5:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 5

    return point


def init_lagoon(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 3 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 4
    if data_set["Lithofacies_major"] == 3 and data_set["GR_shape_code"] in [1, 2]:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 4
    if data_set["Lithofacies_major"] == 4 and data_set["GR_shape_code"] == 5:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 4

    return point


def init_lacustrine_shelf(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 3 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 5

    if data_set["Lithofacies_major"] == 3 and data_set["GR_shape_code"] in [1, 2]:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 5

    if data_set["Lithofacies_major"] == 4 and data_set["GR_shape_code"] == 5:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 5

    return point


def init_marine_shelf(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 3 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 5

    if data_set["Lithofacies_major"] == 3 and data_set["GR_shape_code"] in [1, 2]:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 5

    if data_set["Lithofacies_major"] == 4 and data_set["GR_shape_code"] == 5:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 5

    return point


def init_distal_sub_lacustrine_fan(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 3 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 4

    if data_set["Lithofacies_major"] == 3 and data_set["GR_shape_code"] in [1, 2]:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 4

    return point


def init_distal_submarine_fan(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 3 and data_set["GR_shape_code"] == 4:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 5

    if data_set["Lithofacies_major"] == 3 and data_set["GR_shape_code"] in [1, 2]:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 5

    return point


def init_mixed_tidal_flat(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 3 and data_set["GR_shape_code"] in [1, 2]:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 5:
            point = 5

    return point


def init_muddy_tidal_flat(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 4 and data_set["GR_shape_code"] == 5:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 5:
            point = 4
    return point


def init_lacustrine_deepwater(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 4 and data_set["GR_shape_code"] == 5:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 5
    return point


def init_marine_deepwater(data_set):
    point = 0
    if data_set["Lithofacies_major"] == 4 and data_set["GR_shape_code"] == 5:
        u_thick = data_set["Unit_thick"]
        if 1 <= u_thick < 30:
            point = 5
    return point
