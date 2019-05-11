from . import update_point


def biostratigraphy(data):
    for row in data:
        row.update(update_point.update_fluvial(row))
        row.update(update_point.update_shallow_lacustrine(row))
        row.update(update_point.update_deep_lacustrine(row))
        row.update(update_point.update_marginal_marine(row))
        row.update(update_point.update_shallow_marine(row))
        row.update(update_point.update_deep_marine(row))
