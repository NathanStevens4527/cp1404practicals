"""
Program for simulating taxi use
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4),
             Taxi("cheap taxi", 100)]
    current_taxi = None
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            pass
        elif choice == "D":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()


main()