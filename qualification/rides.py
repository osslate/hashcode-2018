# imports

# import/export data (Fionn)

def parse_data(filename):
    data_file = open(filename, "r")
    data_lines = [line.rstrip("\n") for line in data_file]

    attributes = data_lines[0].split(" ")

    return {
        "num_rows": int(attributes[0]),
        "num_cols": int(attributes[1]),
        "num_vehicles": int(attributes[2]),
        "num_rides": int(attributes[3]),
        "bonus": int(attributes[4]),
        "steps": int(attributes[5]),
        "rides": [[int(i) for i in r.split(" ")] for r in data_lines[1:]]
    }


# run

parsed = print(parse_data("a_example.in"))
