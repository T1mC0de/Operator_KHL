import kivy
kivy.require("1.10.1")
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.app import App
from kivy.lang import Builder

kv = Builder.load_file('test.kv')

class Screen1(Screen):
    def functionname(self):
        self.manager.get_screen('scr2').ids.text.text = "whatever you want here"

class Screen2(Screen):
    pass


class Select_text(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(Screen1(name = "scr1"))
        sm.add_widget(Screen2(name = "scr2"))
        
        return sm

app = Select_text()
app.run()