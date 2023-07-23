"""
estimated completion time: 1 hour
"""
from datetime import date


class Project:

    def __init__(self, name="", start_date=date, priority=0, cost_estimate=0, completion_percentage=0):
        """Stores fields for project object"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """generates string for project"""
        return f"{self.name}, Started on {self.start_date},priority = {self.priority}, Estimated cost : {self.cost_estimate}, {self.completion_percentage}% completed"

    def is_completed(self, completion_percentage):
        """returns boolean for if project is completed"""
        if self.completion_percentage == 100:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.priority < other.priority
