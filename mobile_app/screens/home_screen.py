from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.clock import Clock


class HomeScreen(MDScreen):
    active_tab = StringProperty("home")

    def on_kv_post(self, base_widget):
        # Start auto-sliding the promo banner
        self.carousel_event = Clock.schedule_interval(self.auto_slide_carousel, 3)
                                                      

    def auto_slide_carousel(self, dt):
        carousel = self.ids.get('promo_carousel')
        if carousel:
            if carousel.index == len(carousel.slides) - 1:
                carousel.load_slide(carousel.slides[0])
            else:
                carousel.load_next()

    def on_leave(self):
        # Stop the auto-slide when leaving the screen
        if hasattr(self, 'carousel_event'):
            self.carousel_event.cancel()

    def open_cart(self):
        if self.manager:
            self.manager.current = 'product_list'

    def open_search(self):
        if self.manager:
            self.manager.current = 'search'

    def switch_tab(self, tab_name):
        self.active_tab = tab_name
        if tab_name == "home":
            self.manager.current = "home"
        elif tab_name == "list":
            self.manager.current = "orders"
        elif tab_name == "profile":
            if App.get_running_app().user_logged_in:
                self.manager.current = "profile"
            else:
                self.manager.current = "account_prompt" 