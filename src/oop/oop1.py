# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
#base
class Vehicle():
    def __init__(self, Name = "asdf"):
        self.Name = Name
    def getflightVehicle(self):
        return self.Name

    def getStarShip(self):
        return self.Name
    pass
# Vehicle has a flight Vehicle
class FlightVehicle(Vehicle):
    def __init__(self, starship = "star2"):
        pass
    def getStarship(self):
        self.starship = starship
    pass
#Flight vehcile has a starship
class Starship(FlightVehicle):
    pass
#GroundVehicle inheritance Vehicle
class GroundVehicle(Vehicle):
    def __init__(self, Name = "toy", model = "h1"):
        self.Name = Name
        self.model=model
#a car is a ground vehicle
class Car(GroundVehicle):
    pass
#motorcycle is a ground vehicle
class Motorcycle(GroundVehicle):
    pass
#airplane is a flight vehicle
class Airplane(FlightVehicle):
    pass
