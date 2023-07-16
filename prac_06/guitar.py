"""
Module for storing attributes for guitars
Estimated completion time 50 minutes
"""
class Guitar:
    """Represents a guitar object"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}({self.year}) : ${self.cost}"

    def get_age(self):
        return 2022 - self.year

    def is_vintage(self, age):
        if age >= 50:
            return True
        else:
            return False