import random


 


## POSSIBLE PASSENGER NAMES ##
passenger_possible_names = [
    "John", "Smith", "Jane", "Doe", "Michael", "Johnson", "Emily", "Davis",
    "David", "Brown", "Sarah", "Wilson", "Christopher", "Martinez", "Jessica", "Taylor",
    "Daniel", "Anderson", "Laura", "Thomas", "James", "White", "Amanda", "Harris",
    "Robert", "Clark", "Megan", "Lewis", "William", "Walker", "Olivia", "Hall",
    "Matthew", "Allen", "Sophia", "Young", "Joseph", "King", "Isabella", "Wright",
    "Benjamin", "Scott", "Emma", "Green", "Andrew", "Baker", "Madison", "Adams",
    "Joshua", "Nelson", "Abigail", "Carter", "Ethan", "Mitchell", "Charlotte", "Perez",
    "Alexander", "Roberts", "Mia", "Turner", "Jacob", "Phillips", "Ava", "Campbell",
    "Henry", "Parker", "Ella", "Evans", "Samuel", "Edwards", "Chloe", "Collins",
    "Gabriel", "Stewart", "Lily", "Sanchez", "Anthony", "Morris", "Grace", "Rogers",
    "Nicholas", "Reed", "Victoria", "Cook", "Elijah", "Bell", "Hannah", "Murphy"
]
 
## Define Classes ##
class Passenger:
    def __init__(self, fname: str, lname: str, destination: int):
        self.fname = fname
        self.lname = lname
        self.destination = destination
    def __repr__(self):
        return f"'{self.fname}''{self.fname}':{self.destination}"
 
class Station:
    def __init__(self, name: str, passengers: list[Passenger]):
        self.name = name
        self.passengers = passengers
        self.destination_id = destination_id
    
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
    
    def __repr__(self):
        return f"'{self.name}: {self.passengers}'"
 
 
class Wagon:
    def __init__(self, passengers : list[Passenger]):
        self.passengers = passengers

    
    
 
 
 
 
class Train:
    def __init__(self, wagons: list[Wagon], line: int, position: int):
        self.wagons = wagons
        self.line = line
        self.position = position
 
 
class Line:
    def __init__(self, name: str, stops: list[int]):
        self.name = name
        self.stops = stops
 
 

train_line = [
    Line("Keleti", [1, 3, 5, 7, 9]), 
    Line("Kóny", [2, 4, 6, 8, 10]),
    Line("Romaji", [2, 3, 4, 5, 7, 8])
    ]

station_list = [
    Station("Helgez",[]),
    Station("Jelgeze",[]),
    Station("Kyoto", []),
    Station("Mensike",[]),
    Station("Sapporo",[]),
    Station("Meizéries Sur-Seine, La Paris", []),
    Station("Tokyo",[]),
    Station("Juville",[]),
    Station("Osaka", []),
    Station("Fuckville", []),
    ]

train_list = [ 
    Train([Wagon([]), 0, 1]),
    Train([Wagon([]), 0, 1]), 
    


]
unassigned_passengers = []
 
for x in range(4):
    first_name = random.choice(passenger_possible_names)
    last_name = random.choice(passenger_possible_names)
    spawning_station = random.choice(station_list)
    random.randint(0, len(station_list) -1 ) 
    spawning_station.add_passenger(first_name, last_name, spawning_station.destination_id)
print(station_list)
    

    




    
    
    






