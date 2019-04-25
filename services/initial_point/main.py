from . import initpoint


def init_point(data):
    for row in data:
        row.update({
            "Alluvial_Fan": initpoint.init_alluvial_fan(row),
            "Fluvial_Channel": initpoint.init_fluvial_channel(row),
            "Fluvial_Point_Bar": initpoint.init_fluvial_point_bar(row),
            "Levee": initpoint.init_levee(row),
            "Crevasse_Splay": initpoint.init_crevasse_splay(row),
            "Fluvial_Floodplain": initpoint.init_fluvial_floodplain(row),
            "Progradational_Lacustrine_Delta": initpoint.init_progradational_lacustrine_delta(row),
            "Lacustrine_Fan_Delta": initpoint.init_lacustrine_fan_delta(row),
            "Progradational_Lacustrine_Shoreface": initpoint.init_progradational_lacustrine_shoreface(row),
            "Transgressive_Lacustrine_Shoreface": initpoint.init_transgressive_lacustrine_shoreface(row),
            "Aggradational_Lacustrine_Shoreface": initpoint.init_aggradational_lacustrine_shoreface(row),
            "Lacustrine_Offshore_Transition": initpoint.init_lacustrine_offshore_transition(row),
            "Lacustrine_Shelf": initpoint.init_lacustrine_shelf(row),
            "Proximal_Sub-Lacustrine_Fan": initpoint.init_proximal_sub_lacustrine_fan(row),
            "Distal_Sub-Lacustrine_Fan": initpoint.init_distal_sub_lacustrine_fan(row),
            "Lacustrine_Turbidite": initpoint.init_lacustrine_turbidite(row),
            "Distal_Lacustrine_Turbidites": initpoint.init_distal_lacustrine_turbidites(row),
            "Lacustrine_Deepwater": initpoint.init_lacustrine_deepwater(row),
            "Marine_Delta": initpoint.init_marine_delta(row),
            "Marine_Fan_Delta": initpoint.init_marine_fan_delta(row),
            "Tidal_Channel_And_Sand_Flat": initpoint.init_tidal_channel_and_sand_flat(row),
            "Sandy_Tidal_Flat": initpoint.init_sandy_tidal_flat(row),
            "Mixed_Tidal_Flat": initpoint.init_mixed_tidal_flat(row),
            "Muddy_Tidal_Flat": initpoint.init_muddy_tidal_flat(row),
            "Lagoon": initpoint.init_lagoon(row),
            "Progradational_Marine_Shoreface": initpoint.init_progradational_marine_shoreface(row),
            "Transgressive_Marine_Shoreface": initpoint.init_transgressive_marine_shoreface(row),
            "Aggradational_Marine_Shoreface": initpoint.init_aggradational_marine_shoreface(row),
            "Marine_Offshore_Transition": initpoint.init_marine_offshore_transition(row),
            "Marine_Shelf": initpoint.init_marine_shelf(row),
            "Proximal_Submarine_Fan": initpoint.init_proximal_submarine_fan(row),
            "Distal_Submarine_Fan": initpoint.init_distal_submarine_fan(row),
            "Marine_Turbidite": initpoint.init_marine_turbidite(row),
            "Distal_Marine_Turbidites": initpoint.init_distal_marine_turbidites(row),
            "Marine_Deepwater": initpoint.init_marine_deepwater(row)
        })
