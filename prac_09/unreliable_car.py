"""
Unreliable Car class
"""
from prac_09.car import Car
from random import randint

class UnreliableCar(Car):
    """   """

    def __init__(self, name, fuel, reliability):
        """   """
        super().__init__(name, fuel)
        self.reliability = reliability
        self.total_distance_driven = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, Probability of driving {self.reliability}, Distance driven = {self.total_distance_driven}"

    def drive(self, distance):
        chance_of_driving = randint(1,100)
        if chance_of_driving < self.reliability:
            self.total_distance_driven = super().drive(distance)
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven