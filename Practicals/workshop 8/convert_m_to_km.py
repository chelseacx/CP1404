from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (850, 350)

class ConvertMToKm(App):

    def build(self):
        self.title = "Convert m to km"
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root

    def convert_m_to_km(self):
        m = float(self.root.ids.input_m.text)
        km = "{:.3f}".format(m / 1000)
        self.root.ids.display_result.text = str(km)

    def increment(self):
        try:
            input_num = float(self.root.ids.input_m.text)
            input_num += 1
            self.root.ids.input_m.text = str(input_num)
        except ValueError:
            pass

    def decrement(self):
        try:
            input_num = float(self.root.ids.input_m.text)
            input_num -= 1
            self.root.ids.input_m.text = str(input_num)
        except ValueError:
            pass


ConvertMToKm().run()