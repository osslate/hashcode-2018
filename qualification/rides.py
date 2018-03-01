# imports

# import/export data (Fionn)

def parse_data(filename):
    data_file = open(filename, "r")
    data_lines = [line.rstrip("\n") for line in data_file]

    attributes = data_lines[0].split(" ")

    return {
        "num_rows": attributes[0],
        "num_cols": attributes[1],
        "num_vehicles": attributes[2],
        "num_rides": attributes[3],
        "bonus": attributes[4],
        "steps": attributes[5],
        "rows": data_lines[1:]
    }

# run

parsed = parse_data("a_example.in")
