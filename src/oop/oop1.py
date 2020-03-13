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

class Vehicle():
    def __init__(self, Name = "asdf"):
        self.Name = Name
    def getflightVehicle(self):
        return self.Name

    def getStarShip(self):
        return self.Name
    pass

class FlightVehicle(Vehicle):
    def __init__(self, starship = "star2"):
        pass
    def getStarship(self):
        self.starship = starship
    pass

class Starship(FlightVehicle):
    pass

class GroundVehicle(Vehicle):
    def __init__(self, Name = "toy", model = "h1"):
        self.Name = Name
        self.model=model
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

class Airplane(FlightVehicle):
    pass
