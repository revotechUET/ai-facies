def add_unit_length(data):
    bound = 0
    for i in range(len(data)):
        if data[i]["Boundary_flag"] == "1":
            unit_thick = float(data[i]["TVD"]) - float(data[bound]["TVD"])
            for j in range(bound + 1 if bound > 0 else 0, i + 1):
                data[j].update({"Unit_Thick": unit_thick})
            bound = i
