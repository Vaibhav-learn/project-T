from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.scrollview import ScrollView
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior


# IconButton using Image + ButtonBehavior
class IconButton(ButtonBehavior, Image):
    pass


class ProductScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.bg_rect = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        self.cart_total = 0

        self.layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))

        # Top bar with back and cart
        top_bar = BoxLayout(size_hint_y=None, height=dp(40), padding=[dp(5), 0], spacing=dp(5))

        # ✅ Back icon using IconButton
        back_button = IconButton(
            source='Images/back.png',
            size_hint=(None, None),
            size=(dp(30), dp(30))
        )
        back_button.bind(on_press=self.go_back)

        title = Label(text="Product Detail", font_size=18, color=(0, 0, 0, 1))
        spacer = Widget(size_hint_x=None, width=dp(20))

        # Cart icon with badge
        cart_layout = RelativeLayout(size_hint=(None, None), size=(dp(30), dp(30)))
        cart_icon = Image(source='Images/cart.png', size_hint=(None, None), size=(dp(30), dp(30)))

        self.cart_count = Label(
            text=str(self.cart_total),
            color=(1, 1, 1, 1),
            font_size=12,
            size_hint=(None, None),
            size=(dp(18), dp(18)),
            pos_hint={"right": 1, "top": 1},
            halign='center', valign='middle'
        )
        with self.cart_count.canvas.before:
            Color(1, 0, 0, 1)
            self.cart_bg = RoundedRectangle(size=self.cart_count.size, pos=self.cart_count.pos, radius=[9])
        self.cart_count.bind(size=self._update_cart_badge, pos=self._update_cart_badge)

        cart_layout.add_widget(cart_icon)
        cart_layout.add_widget(self.cart_count)

        top_bar.add_widget(back_button)
        top_bar.add_widget(title)
        top_bar.add_widget(spacer)
        top_bar.add_widget(cart_layout)

        self.layout.add_widget(top_bar)

        # Product image
        self.image_container = RelativeLayout(size_hint_y=None, height=dp(260))
        self.image = Image(size_hint=(1, 1), allow_stretch=True, keep_ratio=True)
        with self.image.canvas.before:
            Color(1, 1, 1, 1)
            self.image_bg = RoundedRectangle(radius=[dp(10)], size=self.image.size, pos=self.image.pos)
        self.image.bind(size=self._update_img_bg, pos=self._update_img_bg)
        self.image_container.add_widget(self.image)
        self.layout.add_widget(self.image_container)

        # Name and price
        self.name_label = Label(font_size=20, bold=True, color=(0, 0, 0, 1), size_hint_y=None, height=dp(30))
        self.price_label = Label(font_size=18, color=(0.2, 0.6, 0.2, 1), size_hint_y=None, height=dp(25))
        self.layout.add_widget(self.name_label)
        self.layout.add_widget(self.price_label)

        # Scrollable description
        self.scroll = ScrollView(size_hint=(1, None), size=(dp(360), dp(120)))
        self.description_label = Label(
            text="",
            color=(0, 0, 0, 1),
            size_hint_y=None,
            text_size=(dp(320), None),
            halign='left',
            valign='top'
        )
        self.description_label.bind(texture_size=self._update_text_height)
        self.scroll.add_widget(self.description_label)
        self.layout.add_widget(self.scroll)

        # Quantity
        self.quantity = 1
        self.qty_layout = BoxLayout(size_hint_y=None, height=dp(40), spacing=dp(10))
        self.decrease_btn = Button(text="-", size_hint_x=0.2)
        self.qty_label = Label(text=str(self.quantity), size_hint_x=0.2,
                               halign='center', valign='middle', color=(0, 0, 0, 1))
        self.qty_label.bind(size=self._center_label)
        self.increase_btn = Button(text="+", size_hint_x=0.2)
        self.decrease_btn.bind(on_press=self.decrease_quantity)
        self.increase_btn.bind(on_press=self.increase_quantity)
        self.qty_layout.add_widget(self.decrease_btn)
        self.qty_layout.add_widget(self.qty_label)
        self.qty_layout.add_widget(self.increase_btn)
        self.layout.add_widget(self.qty_layout)

        # Action buttons
        self.button_layout = BoxLayout(size_hint_y=None, height=dp(50), spacing=dp(10))
        self.cart_btn = Button(text="Add to Cart", background_color=(0.1, 0.6, 0.1, 1), color=(1, 1, 1, 1))
        self.wishlist_btn = Button(text="Add to Wishlist", background_color=(0.2, 0.3, 0.6, 1), color=(1, 1, 1, 1))
        self.cart_btn.bind(on_press=self.add_to_cart)
        self.wishlist_btn.bind(on_press=self.add_to_wishlist)
        self.button_layout.add_widget(self.cart_btn)
        self.button_layout.add_widget(self.wishlist_btn)

        self.layout.add_widget(self.button_layout)
        self.add_widget(self.layout)

    def update_product(self, data):
        self.image.source = data["image"]
        self.name_label.text = data["name"]
        self.price_label.text = data["price"]
        self.description_label.text = (
            f"{data['name']} is a powerful Ayurvedic product made using traditional herbs.\n\n"
            f"• 100% Natural\n• No chemicals\n• Trusted for generations"
        )
        self.quantity = 1
        self.qty_label.text = str(self.quantity)
        self.scroll.scroll_y = 1

    def _update_text_height(self, instance, value):
        instance.height = instance.texture_size[1] + dp(10)

    def _center_label(self, instance, value):
        instance.text_size = instance.size

    def increase_quantity(self, instance):
        self.quantity += 1
        self.qty_label.text = str(self.quantity)

    def decrease_quantity(self, instance):
        if self.quantity > 1:
            self.quantity -= 1
            self.qty_label.text = str(self.quantity)

    def add_to_cart(self, instance):
        self.cart_total += self.quantity
        self.cart_count.text = str(self.cart_total)
        self._update_cart_badge()
        self.manager.get_screen('home').update_cart_count(self.cart_total)
        self.show_popup("Added to Cart", f"{self.name_label.text} x{self.quantity} added!")

    def add_to_wishlist(self, instance):
        self.show_popup("Wishlisted", f"{self.name_label.text} saved to wishlist!")

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        label = Label(text=message, halign='center', valign='middle', color=(0, 0, 0, 1))
        ok_button = Button(text="OK", size_hint_y=None, height=dp(40))
        content.add_widget(label)
        content.add_widget(ok_button)

        popup = Popup(
            title=title,
            content=content,
            size_hint=(None, None),
            size=(dp(280), dp(180)),
            auto_dismiss=False
        )
        ok_button.bind(on_press=popup.dismiss)
        popup.open()

    def go_back(self, instance):
        self.manager.current = 'home'

    def _update_bg(self, *args):
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos

    def _update_img_bg(self, *args):
        self.image_bg.size = self.image.size
        self.image_bg.pos = self.image.pos

    def _update_cart_badge(self, *args):
        self.cart_bg.size = self.cart_count.size
        self.cart_bg.pos = self.cart_count.pos
