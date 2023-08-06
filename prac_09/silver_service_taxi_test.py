""""
programs for testing silver service taxi
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

my_silver_taxi = SilverServiceTaxi("Fancy taxi", 1000, 20)
my_silver_taxi.drive(30)
print(f"{my_silver_taxi} fare = {my_silver_taxi.calculate_silver_service_fare()}")