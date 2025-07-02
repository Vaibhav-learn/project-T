from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from Codes.home_screen import HomeScreen
from Codes.product_screen import ProductScreen

class AyurApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ProductScreen(name='product'))
        return sm

if __name__ == '__main__':
    AyurApp().run()