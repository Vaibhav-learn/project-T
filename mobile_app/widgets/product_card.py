from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty

class ProductCard(MDCard):
    image = StringProperty()
    name = StringProperty()
    price = StringProperty()
    on_press_callback = ObjectProperty(None)
    show_heart = BooleanProperty(False)
    heart_filled = BooleanProperty(False)
    heart_press_callback = ObjectProperty(None)
    category = StringProperty('')
    secondary_label = StringProperty('')
    sold_out_text = StringProperty('')

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.on_press_callback:
                self.on_press_callback(self)
        return super().on_touch_down(touch) 