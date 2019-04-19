from modifier_set1.biostratigraphy import update_point
from utilities import utils_func


def biostratigraphy(data):
    for row in data:
        row.update(update_point.update_fluvial(row))
        row.update(update_point.update_shallow_lacustrine(row))
        row.update(update_point.update_deep_lacustrine(row))
        row.update(update_point.update_marginal_marine(row))
        row.update(update_point.update_shallow_marine(row))
        row.update(update_point.update_deep_marine(row))
    utils_func.export_to_csv(data, f"csv/biostratigraphy.csv")
