"""
program for testing unreliable car
"""
from prac_09.unreliable_car import Unreliable_Car


my_unreliable_car = Unreliable_Car("Good Car", 100, 50)
my_unreliable_car.drive(20)
print(f"{my_unreliable_car}")