from initial_point import initpoint


def init_point(data):
    for row in data:
        row.update({
            "Alluvial_Fan": initpoint.init_alluvial_fan(row) + 10,
            "Fluvial_Channel": initpoint.init_fluvial_channel(row) + 10,
            "Fluvial_Point_Bar": initpoint.init_fluvial_point_bar(row) + 10,
            "Levee": initpoint.init_levee(row) + 10,
            "Crevasse_Splay": initpoint.init_crevasse_splay(row) + 10,
            "Fluvial_Floodplain": initpoint.init_fluvial_floodplain(row) + 10,
            "Progradational_Lacustrine_Delta": initpoint.init_progradational_lacustrine_delta(row) + 10,
            "Lacustrine_Fan_Delta": initpoint.init_lacustrine_fan_delta(row) + 10,
            "Progradational_Lacustrine_Shoreface": initpoint.init_progradational_lacustrine_shoreface(row) + 10,
            "Transgressive_Lacustrine_Shoreface": initpoint.init_transgressive_lacustrine_shoreface(row) + 10,
            "Aggradational_Lacustrine_Shoreface": initpoint.init_aggradational_lacustrine_shoreface(row) + 10,
            "Lacustrine_Offshore_Transition": initpoint.init_lacustrine_offshore_transition(row) + 10,
            "Lacustrine_Shelf": initpoint.init_lacustrine_shelf(row) + 10,
            "Proximal_Sub-Lacustrine_Fan": initpoint.init_proximal_sub_lacustrine_fan(row) + 10,
            "Distal_Sub-Lacustrine_Fan": initpoint.init_distal_sub_lacustrine_fan(row) + 10,
            "Lacustrine_Turbidite": initpoint.init_lacustrine_turbidite(row) + 10,
            "Distal_Lacustrine_Turbidites": initpoint.init_distal_lacustrine_turbidites(row) + 10,
            "Lacustrine_Deepwater": initpoint.init_lacustrine_deepwater(row) + 10,
            "Marine_Delta": initpoint.init_marine_delta(row) + 10,
            "Marine_Fan_Delta": initpoint.init_marine_fan_delta(row) + 10,
            "Tidal_Channel_And_Sand_Flat": initpoint.init_tidal_channel_and_sand_flat(row) + 10,
            "Sandy_Tidal_Flat": initpoint.init_sandy_tidal_flat(row) + 10,
            "Mixed_Tidal_Flat": initpoint.init_mixed_tidal_flat(row) + 10,
            "Muddy_Tidal_Flat": initpoint.init_muddy_tidal_flat(row) + 10,
            "Lagoon": initpoint.init_lagoon(row) + 10,
            "Progradational_Marine_Shoreface": initpoint.init_progradational_marine_shoreface(row) + 10,
            "Transgressive_Marine_Shoreface": initpoint.init_transgressive_marine_shoreface(row) + 10,
            "Aggradational_Marine_Shoreface": initpoint.init_aggradational_marine_shoreface(row) + 10,
            "Marine_Offshore_Transition": initpoint.init_marine_offshore_transition(row) + 10,
            "Marine_Shelf": initpoint.init_marine_shelf(row) + 10,
            "Proximal_Submarine_Fan": initpoint.init_proximal_submarine_fan(row) + 10,
            "Distal_Submarine_Fan": initpoint.init_distal_submarine_fan(row) + 10,
            "Marine_Turbidite": initpoint.init_marine_turbidite(row) + 10,
            "Distal_Marine_Turbidites": initpoint.init_distal_marine_turbidites(row) + 10,
            "Marine_Deepwater": initpoint.init_marine_deepwater(row) + 10
        })
    return data
