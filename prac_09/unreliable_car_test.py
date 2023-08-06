"""
program for testing unreliable car
"""
from prac_09.unreliable_car import UnreliableCar


my_unreliable_car = UnreliableCar("Good Car", 100, 50)
my_unreliable_car.drive(20)
print(f"{my_unreliable_car}")