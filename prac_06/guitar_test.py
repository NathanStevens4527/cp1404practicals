"""
program for testing guitar module
"""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(gibson)
gibson_age = gibson.get_age()
print(f"Gibson L-5 CES get_age() - Expected 100. Got {gibson_age}")
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {gibson.is_vintage(gibson_age)}")