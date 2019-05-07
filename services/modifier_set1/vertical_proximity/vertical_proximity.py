from . import update_point
from ...utilities import utils_func


def vertical_proximity(data):
    for row in data:
        row.update({
            "Alluvial_Fan": update_point.update_alluvial_fan(row),
            "Fluvial_Channel": update_point.update_fluvial_channel(row),
            "Fluvial_Point_Bar": update_point.update_fluvial_point_bar(row),
            "Levee": update_point.update_levee(row),
            "Crevasse_Splay": update_point.update_crevasse_splay(row),
            "Fluvial_Floodplain": update_point.update_fluvial_floodplain(row),
            "Progradational_Lacustrine_Delta": update_point.update_progradational_lacustrine_delta(
                row),
            "Lacustrine_Fan_Delta": update_point.update_lacustrine_fan_delta(row),
            "Progradational_Lacustrine_Shoreface": update_point.update_progradational_lacustrine_shoreface(
                row),
            "Transgressive_Lacustrine_Shoreface": update_point.update_transgressive_lacustrine_shoreface(
                row),
            "Aggradational_Lacustrine_Shoreface": update_point.update_aggradational_lacustrine_shoreface(
                row),
            "Lacustrine_Offshore_Transition": update_point.update_lacustrine_offshore_transition(row),
            "Lacustrine_Shelf": update_point.update_lacustrine_shelf(row),
            "Proximal_Sub-Lacustrine_Fan": update_point.update_proximal_sub_lacustrine_fan(row),
            "Distal_Sub-Lacustrine_Fan": update_point.update_distal_sub_lacustrine_fan(row),
            "Lacustrine_Turbidite": update_point.update_lacustrine_turbidite(row),
            "Distal_Lacustrine_Turbidites": update_point.update_distal_lacustrine_turbidites(row),
            "Lacustrine_Deepwater": update_point.update_lacustrine_deepwater(row),
            "Marine_Delta": update_point.update_marine_delta(row),
            "Marine_Fan_Delta": update_point.update_marine_fan_delta(row),
            "Tidal_Channel_And_Sand_Flat": update_point.update_tidal_channel_and_sand_flat(row),
            "Sandy_Tidal_Flat": update_point.update_sandy_tidal_flat(row),
            "Mixed_Tidal_Flat": update_point.update_mixed_tidal_flat(row),
            "Muddy_Tidal_Flat": update_point.update_muddy_tidal_flat(row),
            "Lagoon": update_point.update_lagoon(row),
            "Progradational_Marine_Shoreface": update_point.update_progradational_marine_shoreface(
                row),
            "Transgressive_Marine_Shoreface": update_point.update_transgressive_marine_shoreface(row),
            "Aggradational_Marine_Shoreface": update_point.update_aggradational_marine_shoreface(row),
            "Marine_Offshore_Transition": update_point.update_marine_offshore_transition(row),
            "Marine_Shelf": update_point.update_marine_shelf(row),
            "Proximal_Submarine_Fan": update_point.update_proximal_submarine_fan(row),
            "Distal_Submarine_Fan": update_point.update_distal_submarine_fan(row),
            "Marine_Turbidite": update_point.update_marine_turbidite(row),
            "Distal_Marine_Turbidites": update_point.update_distal_marine_turbidites(row),
            "Marine_Deepwater": update_point.update_marine_deepwater(row)})
