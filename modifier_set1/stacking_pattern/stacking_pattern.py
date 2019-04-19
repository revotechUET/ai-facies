from modifier_set1.stacking_pattern import update_point
from utilities import utils_func


def stacking_pattern(data):
    for row in data:
        update_point.update_fluvial(row)
        update_point.update_deep_lacustrine(row)
        update_point.update_deep_marine(row)
        update_point.update_marginal_marine(row)
        update_point.update_shallow_lacustrine(row)
        update_point.update_shallow_marine(row)
    utils_func.export_to_csv(data, "csv/stacking_pattern.csv")
