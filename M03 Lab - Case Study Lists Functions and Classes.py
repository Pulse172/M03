#Jerron Jones
#M03 Lab- Case Study Lists Functions and Classes.py
#The program asks user for information about a vehicle and stores it in classes
#the program then prints out the data at the end
#the data inclues the type, year, make, model, year, doors, and roof of a vehicle

class Vehicle: #superclass that holds the data for the vehicles type
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):#subclass that holds data for the specs ofs of the vehicle
    def __init__(self, year, make, model, doors, roof, vehicle_type):
        super().__init__(vehicle_type) 
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
vehicle_type = input("What is the type of vehicle (Example: car, truck, plane, boat.): ") #user types in the vehicle type along with all of its specs
year = input(f"What is the year of the {vehicle_type}: ")
make = input(f"What is the make of the {vehicle_type}: ")
model = input(f"What is the model of the {vehicle_type}: ")
doors = input(f"How many doors will the {vehicle_type} have (2 or 4): ")
roof = input(f"What type of roof will the {vehicle_type} have (solid or sun roof): ")

automobile = Automobile(year, make, model, doors, roof,vehicle_type)#makes a variable that contains the data of the Automobile class
print(f"Vehicle type: {automobile.vehicle_type}")#prints all the data using classes
print(f"Year: {automobile.year}")
print(f"Make: {automobile.make}")
print(f"Model: {automobile.model}")
print(f"Number of doors: {automobile.doors}")
print(f"Type of roof: {automobile.roof}")