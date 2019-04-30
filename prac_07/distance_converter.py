from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class DistanceConverter(App):
    message = StringProperty()

    def build(self):
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('distance_converter.kv')
        return self.root

    def handle_calculate(self, value):
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, value, change):
        result = value * 1.60934 + change
        self.root.ids.input_number.text = str(result)

    def handle_press(self):
        self.message = self.root.ids.input_number.text


DistanceConverter().run()
