from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKilometersApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert_to_kilometers(self, miles):
        try:
            kilometers = float(miles) * 1.609
            self.root.ids.output_result.text = str(kilometers)
        except TypeError:
            self.root.ids.input_mile.text = '0'



ConvertMilesToKilometersApp().run()
