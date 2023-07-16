"""
Module for storing attributes for guitars
Estimated completion time 50 minutes
actual completion time: 1 hour and 25 minutes
"""
class Guitar:
    """Represents a guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Stores name, year and cost for guitar object"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Generates string for guitar object"""
        return f"{self.name}({self.year}) : ${self.cost}"

    def get_age(self):
        """Calculates the age for a guitar"""
        return 2022 - self.year

    def is_vintage(self, age):
        """Determines if a guitar is vintage"""
        if age >= 50:
            return True
        else:
            return False