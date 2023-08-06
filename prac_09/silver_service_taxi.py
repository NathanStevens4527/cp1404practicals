"""
class for silver service taxi
"""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """   """
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.price_per_km *= fanciness

    def __str__(self):
        """returns string representation for silver service taxi"""
        return f"{super().__str__()} Plus flagfall of ${self.flagfall}"

    def calculate_silver_service_fare(self):
        """method for calculating the fare including flagfall fee"""
        return self.flagfall + super().get_fare()