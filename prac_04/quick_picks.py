"""
program for generating lines of random numbers
user inputs the number of lines they want
numbers are generated between 1 and 45
"""

import random

MAXIMUM_NUMBER = 45
MINIMUM_NUMBER = 1
quick_picks = []

number_of_lines = int(input("How many quick picks? "))
for i in range(0, number_of_lines):
    number_of_picks = 0
    line = []
    while number_of_picks != 6:
        quick_pick = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while quick_pick in line:
            quick_pick = 0
            quick_pick = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        line.append(quick_pick)
        number_of_picks += 1
    quick_picks.append(line)
    print(quick_picks)

