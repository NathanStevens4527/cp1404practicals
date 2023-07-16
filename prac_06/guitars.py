"""
Program for allowing users to store guitar information in a list
"""

from prac_06.guitar import Guitar

guitars = []
print("My guitars!")
name = input("Name: ")
while name.isalnum():
    valid_year = False
    try:
        while not valid_year:
            year = int(input("Year: "))
            valid_year = True
    except ValueError:
        print("year must be an integer")
    valid_cost = False
    try:
        while not valid_cost:
            cost = float(input("cost: "))
            valid_cost = True
    except ValueError:
        print("cost must be a number")
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print(f"{new_guitar} added.")
    name = input("Name: ")

