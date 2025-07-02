from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.relativelayout import RelativeLayout
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle
from kivy.animation import Animation
from kivy.uix.button import Button


class ImageButton(ButtonBehavior, Image):
    pass


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cart_total = 0
        root = RelativeLayout()
        self.root_layout = root

        # ⚪️ Background White
        with root.canvas.before:
            Color(1, 1, 1, 1)
            self.bg_rect = RoundedRectangle(size=root.size, pos=root.pos)
        root.bind(size=self._update_bg, pos=self._update_bg)

        # 🔳 Touch-blocker (initially hidden)
        self.touch_blocker = Button(
            background_color=(0, 0, 0, 0.4),
            size_hint=(1, 1),
            opacity=0,
            disabled=True
        )
        self.touch_blocker.bind(on_press=self.toggle_menu)
        root.add_widget(self.touch_blocker)

        # Main vertical layout
        main_layout = BoxLayout(orientation='vertical', padding=[0, dp(10), dp(10), 0], spacing=10)

        # Top bar
        top_bar = BoxLayout(size_hint_y=None, height=dp(40), spacing=10, padding=[dp(10), 0, 0, 0])

        self.menu_button = ImageButton(source='Images/menu.jpg', size_hint=(None, None), size=(dp(30), dp(30)))
        self.menu_button.bind(on_press=self.toggle_menu)

        spacer = Widget()
        self.cart_label = Label(text=f"Cart: {self.cart_total}", size_hint=(None, None),
                                size=(dp(80), dp(30)), color=(0, 0, 0, 1), font_size=14)

        top_bar.add_widget(self.menu_button)
        top_bar.add_widget(spacer)
        top_bar.add_widget(self.cart_label)
        main_layout.add_widget(top_bar)

        # Product scroll
        scroll = ScrollView()
        layout = GridLayout(cols=2, spacing=10, size_hint_y=None, padding=10)
        layout.bind(minimum_height=layout.setter('height'))

        self.products = [
            {"name": "Kaayakalpaa Kit", "image": "Images/homepage/Kaayakalpaa_kit.jpg", "price": "₹399"},
            {"name": "Karisalankanni Oil", "image": "Images/homepage/Karisalankanni_Karisilankanni_Oil.jpg", "price": "₹250"},
            {"name": "Eucalyptus Oil", "image": "Images/homepage/Eucalyptus_Oil.jpg", "price": "₹199"},
            {"name": "Sathuragiri Oil", "image": "Images/homepage/Sathuragiri_Oil.jpg", "price": "₹230"},
            {"name": "Nalangu Maavu Powder", "image": "Images/homepage/Nalangu_Maavu_Powder.jpg", "price": "₹99"},
            {"name": "Aadutheendapalai Powder", "image": "Images/homepage/Aadutheendapalai_Powder.jpg", "price": "₹149"},
            {"name": "Pure K. Oil", "image": "Images/homepage/Pure_K_Oil.jpg", "price": "₹199"},
            {"name": "Manjal-Turmeric Powder", "image": "Images/homepage/Manjal_Turmeric_Powder.jpg", "price": "₹89"},
            {"name": "Spl. Arokiya Podi", "image": "Images/homepage/Spl_Arokiya_Podi_Powder.jpg", "price": "₹149"},
            {"name": "Sukku Powder", "image": "Images/homepage/Sukku_Powder.jpg", "price": "₹90"},
            {"name": "Scool Rice", "image": "Images/homepage/Scool_Rice.jpg", "price": "₹199"},
            {"name": "Naaval Seed Powder", "image": "Images/homepage/Naaval_Seed_Powder.jpg", "price": "₹140"},
            {"name": "Multhani Mitty Powder", "image": "Images/homepage/Multhani_Mitty_Powder.jpg", "price": "₹70"},
            {"name": "Kalarchikai Powder", "image": "Images/homepage/Kalarchikai_Klachikai_Powder.jpg", "price": "₹150"},
            {"name": "Arugampul Podi", "image": "Images/homepage/Arugampul_Podi_Powder.jpg", "price": "₹99"},
            {"name": "Ashwagandha Powder", "image": "Images/homepage/Spl_Amukkara_Powder_Spl_Ashwagandha.jpg", "price": "₹170"},
        ]

        for product in self.products:
            box = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(220), spacing=5, padding=5)
            img = ImageButton(source=product["image"], allow_stretch=True, keep_ratio=False,
                              size_hint=(1, 0.75))
            img.bind(on_press=lambda instance, p=product: self.open_product(p))

            name = Label(text=product["name"], size_hint_y=None, height=30,
                         color=(0, 0, 0, 1), font_size=14, halign='center', text_size=(dp(160), None))
            price = Label(text=product["price"], size_hint_y=None, height=20,
                          color=(0.2, 0.6, 0.2, 1), font_size=13)

            box.add_widget(img)
            box.add_widget(name)
            box.add_widget(price)
            layout.add_widget(box)

        scroll.add_widget(layout)
        main_layout.add_widget(scroll)
        root.add_widget(main_layout)

        # 🔲 Sliding Menu
        self.menu_panel = BoxLayout(orientation='vertical', size_hint=(None, 1), width=dp(180))
        self.menu_panel.x = -self.menu_panel.width
        with self.menu_panel.canvas.before:
            Color(1, 1, 1, 1)
            self.menu_bg = RoundedRectangle(size=self.menu_panel.size, pos=self.menu_panel.pos)
        self.menu_panel.bind(pos=self._update_menu_bg, size=self._update_menu_bg)
        root.add_widget(self.menu_panel)

        self.add_widget(root)

    def _update_bg(self, *args):
        self.bg_rect.size = self.root_layout.size
        self.bg_rect.pos = self.root_layout.pos

    def open_product(self, product_data):
        product_screen = self.manager.get_screen('product')
        product_screen.update_product(product_data)
        self.manager.current = 'product'

    def update_cart_count(self, count):
        self.cart_total = count
        self.cart_label.text = f"Cart: {self.cart_total}"

    def toggle_menu(self, instance=None):
        if self.menu_panel.x < 0:
            Animation(x=0, d=0.3).start(self.menu_panel)
            self.touch_blocker.disabled = False
            self.touch_blocker.opacity = 1
        else:
            Animation(x=-self.menu_panel.width, d=0.3).start(self.menu_panel)
            self.touch_blocker.disabled = True
            self.touch_blocker.opacity = 0

    def _update_menu_bg(self, *args):
        self.menu_bg.size = self.menu_panel.size
        self.menu_bg.pos = self.menu_panel.pos
