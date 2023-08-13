"""
Program for simulating taxi use
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Main function for taxi simulator including menu loop"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4),
             Taxi("cheap taxi", 100)]
    current_taxi = None
    bill = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print_taxis(taxis)
            current_taxi = select_taxi(current_taxi, taxis)
        elif choice == "D":
            bill = drive_taxi(bill, current_taxi)
        else:
            print("Invalid choice")
        print(f"Bill to date: ${bill}")
        print(MENU)
        choice = input(">>> ").upper()
    print("taxis are now")
    print_taxis(taxis)


def select_taxi(current_taxi, taxis):
    """selects taxi from user input"""
    taxi_choice = int(input("Choose taxi: "))
    try:
        current_taxi = taxis[taxi_choice]
    except:
        print("Invalid choice")
    return current_taxi


def drive_taxi(bill, current_taxi):
    """ drives taxi and determines fair"""
    try:
        distance = int(input("Drive how far: "))
        current_taxi.drive(distance)
        print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare()}")
        bill += current_taxi.get_fare()
        current_taxi.start_fare()
    except:
        "Invalid Distance"
    return bill


def print_taxis(taxis):
    """ prints list of taxis"""
    taxi_number = 0
    for taxi in taxis:
        print(f"{taxi_number} - {taxi}")
        taxi_number += 1


main()