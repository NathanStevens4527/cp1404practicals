"""
Program for allowing users to store guitar information in a list
"""

from prac_06.guitar import Guitar
from operator import attrgetter


def main():
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
    print_guitars(guitars)


def print_guitars(guitars):
    guitars.sort(key=attrgetter("year"))
    longest_guitar = 0
    for guitar in guitars:
        guitar_length = len(guitar.name)
        if guitar_length > longest_guitar:
            longest_guitar = guitar_length
    number = 0
    for guitar in guitars:
        number += 1
        vintage_string = "(vintage)" if guitar.is_vintage(guitar.get_age()) else ""
        print(
            f"Guitar {number}: {guitar.name:>{longest_guitar}} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()


