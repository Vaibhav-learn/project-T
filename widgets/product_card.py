from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty

class ProductCard(MDCard):
    image = StringProperty()
    name = StringProperty()
    price = StringProperty()
    category = StringProperty()
    on_press_callback = ObjectProperty(None)
    is_favorite = BooleanProperty(False)
    on_favorite_toggle = ObjectProperty(None)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.on_press_callback:
                self.on_press_callback(self)
        return super().on_touch_down(touch)

    def toggle_favorite(self):
        self.is_favorite = not self.is_favorite
        if self.on_favorite_toggle:
            self.on_favorite_toggle(self, self.is_favorite) 