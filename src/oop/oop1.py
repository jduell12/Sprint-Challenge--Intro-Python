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

# Vechicle is base class for everything
class Vehicle:
    pass

# inherits from vehicle


class GroundVehicle(Vehicle):
    pass


class FlightVehicle(Vehicle):
    pass

# inherits from groundVehicle


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass

# inherits from flightvehicle


class Airplane(FlightVehicle):
    pass


class Starship(FlightVehicle):
    pass
