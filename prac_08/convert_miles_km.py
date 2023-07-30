"""
program for converting miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.609

class ConvertMilesToKilometersApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert_to_kilometers(self, miles):
        """Converts passed in miles to kilometers"""
        try:
            kilometers = float(miles) * MILES_TO_KM
            self.root.ids.output_result.text = str(kilometers)
        except ValueError:
            self.root.ids.input_mile.text = '0'

    def handle_increment(self, miles, increment):
        """adds or subtracts increment from miles"""
        try:
            miles = float(miles) + float(increment)
            self.root.ids.input_mile.text = str(miles)
        except ValueError:
            self.root.ids.input_mile.text = '0'



ConvertMilesToKilometersApp().run()
