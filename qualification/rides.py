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

class Car:

    def __init__(self, id):
        self.id = id
        self.free = False
        self.col = 0
        self.row = 0
        self.rides = []

class Carpool:

    def __init__(self):
        self.vehicles = [Car(i) for i in range(0,parsed['num_vehicles'])]


class Passengerpool:
    
    def __init__(self):
        print('aaaaa')
# run

parsed = parse_data("a_example.in")

x = Carpool()
print(x.vehicles)