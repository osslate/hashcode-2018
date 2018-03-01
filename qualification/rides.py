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
FREE = 0
PICKUP = 1
TRANSIT = 2
personId = 0
class Car:

    def __init__(self, id):
        self.id = id
        self.col = 0
        self.row = 0
        self.ride = []
        self.status = FREE
        self.person = None

    def pick_up(self, person):
        self.person = person
        self.ride.append(person.id)
        person.hasCar = True
        self.status = PICKUP

    def move(self, step):
        if self.status == PICKUP:
            if self.row > self.person.startRow:
                self.row -= 1
            elif self.row < self.person.startRow:
                self.row += 1
            else:
                if self.col > self.person.startCol:
                    self.col -= 1
                elif self.col < self.person.startCol:
                    self.col += 1
            if self.row == self.person.startRow and self.col == self.person.startCol:
                if step >= self.person.startStep:
                    self.status = TRANSIT
        elif self.status == TRANSIT:
            if self.row > self.person.endRow:
                self.row -= 1
            elif self.row < self.person.endRow:
                self.row += 1
            else:
                if self.col > self.person.endCol:
                    self.col -= 1
                elif self.col < self.person.endCol:
                    self.col += 1
            if self.row == self.person.endRow and self.col == self.person.endCol:
                self.status = FREE
    



        

class Person:
    
    def __init__(self,a,b,x,y,s,f,personId):
        self.id = personId
        personId +=1
        self.startRow = a
        self.startCol = b
        self.endRow = x
        self.endCol = y
        self.startStep = s
        self.finishStep = f
        self.hasCar = False

# run
class Carpool:

    def __init__(self):
        self.vehicles = [Car(i) for i in range(0,parsed['num_vehicles'])]
        self.people = []
        for i in range(0,len(parsed['rides'])):
            ride = parsed['rides'][i]
            self.people.append(Person(ride[0],ride[1],ride[2],ride[3],ride[4],ride[5],i))

    def aval_cars(self):
        return filter(lambda car : car.status == FREE, self.vehicles)

    def move_cars(self,step):
        for car in self.vehicles:
            car.move(step)
    def get_next_person(self): 
        retval = filter(lambda p : p.hasCar == False, self.people)
        if len(retval):
            return retval[0]
        else:
            return None

parsed = parse_data("e_high_bonus.in")


def to_execute(read):
    pool = Carpool()
    for i in range(0,read['steps']):
        pool.move_cars(i)
        freeCars = pool.aval_cars()
        #print(i, len(freeCars))
        for car in freeCars:
            person = pool.get_next_person()
            if person:
                car.pick_up(person)
            else:
                break
    with  open("submition.in", 'w+') as file:
        output = ''
        for i in pool.vehicles:
            output += str(len(i.ride)) + ' '
            for k in i.ride:
                output += str(k) + ' '
            output += '\n'
        file.write(output)

    return 
to_execute(parsed)
# pool.vehicles.output()
# run




