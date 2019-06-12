from ..utilities import utils_func

def machine_learning(data):
    for row in data:
        code = row["ML"]
        if code != -1:
            facies = utils_func.map_core_depofacies_code_to_name(code)
            if facies and row[facies] > 0:
                row.update({facies: row[facies] + 2})