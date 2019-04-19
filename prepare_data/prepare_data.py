from prepare_data.unit_matching import unit_matching
from prepare_data.add_unit_length import add_unit_length
from csv import DictReader


def prepare_data():
    unit_matching()
    with open("csv/data.csv") as i_file:
        dict_reader = DictReader(i_file)
        data = list(dict_reader)
    add_unit_length(data)

    return data

