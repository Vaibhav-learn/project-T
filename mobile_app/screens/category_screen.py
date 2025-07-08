from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.lang import Builder
from widgets.product_card import ProductCard
from kivy.app import App
from functools import partial
from screens.product_list_screen import ProductListScreen

# Example categories and products (replace with your real data)
categories =  {
    
    'Baby Care': [
        ("Kaayakalpaa Kit (225g)", "assets/herbal oils/1.png"),
        ("Kaasi Katti (10g)", "assets/baby care images/5.jpg"),
        ("Pure Karisalankanni Oil 225ml", "assets/herbal oils/7.png"),
        ("Black Bindi for Babies (1 piece)", "assets/baby care images/13.jpg"),
        ("Pillaivalathi Leaf (20g)", "assets/baby care images/8.jpg"),
        ("Vasambu Bangle (1 piece)", "assets/baby care images/12.jpg"),
        ("Muligai Saampirani Set (100g)", "assets/baby care images/9.jpg"),
        ("Spiked Ginger Lily (100g)", "assets/baby care images/2.jpg"),
        ("Urasu / Orasu Medicine (1 set)", "assets/baby care images/7.jpg"),
        ("Kaadhola / Kaadholai Karugamani (1 set)", "assets/baby care images/4.jpg"),
        ("Vasambu / Sweetflag (2 pieces)", "assets/baby care images/11.jpg"),
        ("Baby Care Combo (1 set)", "assets/baby care images/1.jpg"),
    ],
    'Bathing': [],
    'Beauty & Face': [],
    'Blood Purifier': [],
    'Body building': [],
    'Body Heat': [],
    'Birth Disorders': [],
    'Cold and Cough': [],
    'Combos': [],
    'Essentials': [],
    'Fever': [],
    'Hair Problems': [],
    'Hair Removal': [],
    'Head Ache': [],
    'Heart Problems': [],
    'Herbal oils': [
        ("Kaayakalpaa Kit", "assets/herbal oils/1.png"),
        ("Pure Karisalankanni Oil 225ml", "assets/herbal oils/7.png"),
        ("Eucalyptus Oil", "assets/herbal oils/4.jpg"),
        ("Sathuragiri Joint Pain Thailam 60g", "assets/herbal oils/2.jpg"),
        ("Karisalankanni Oil 90g", "assets/herbal oils/7.png"),
        ("Karisalankanni Oil 180ml", "assets/herbal oils/7.png"),
        ("Karunjeeragam Oil 50ml", "assets/herbal oils/6.jpg"),
        ("Prasava Legiyam 500g", "assets/herbal oils/8.jpg"),
    ],
    'Joint Pain': [],

    # ... add more categories as needed ...
}

class CategoryScreen(MDScreen):
    current_category = StringProperty()
    category_buttons = ListProperty()
    product_grid = ObjectProperty()
    sidebar_layout = ObjectProperty()

    def on_kv_post(self, base_widget):
        self.sidebar_layout = self.ids.sidebar_layout
        self.product_grid = self.ids.product_grid
        self.load_categories()
        # Select the first category by default
        if categories:
            first_category = next(iter(categories))
            self.select_category(first_category)

    def load_categories(self):
        self.sidebar_layout.clear_widgets()
        self.category_buttons = []
        for cat in categories:
            is_selected = cat == self.current_category
            btn = Button(
                text=cat,
                size_hint_y=None,
                height=dp(38),
                background_normal='',
                background_color=(0.2, 0.8, 0.2, 1) if is_selected else (1, 1, 1, 1),
                color=(1, 1, 1, 1) if is_selected else (0, 0, 0, 1),
                bold=True if is_selected else False
            )
            btn.bind(on_release=self.on_category_select)
            self.category_buttons.append(btn)
            self.sidebar_layout.add_widget(btn)

    def on_category_select(self, button):
        self.select_category(button.text)

    def select_category(self, cat_name):
        self.current_category = cat_name
        # Update button highlights
        for btn in self.category_buttons:
            is_selected = btn.text == cat_name
            btn.background_color = (0.2, 0.8, 0.2, 1) if is_selected else (1, 1, 1, 1)
            btn.color = (1, 1, 1, 1) if is_selected else (0, 0, 0, 1)
            btn.bold = True if is_selected else False
        self.show_products(cat_name)

    def show_products(self, cat_name):
        self.product_grid.clear_widgets()
        app = App.get_running_app()
        # Get the shared product list from the product_list screen instance
        product_list_screen = app.sm.get_screen('product_list')
        shared_products = product_list_screen.products
        # Build a lookup by name for fast access
        product_lookup = {p['name']: p for p in shared_products}
        for product in categories.get(cat_name, []):
            # product[0] is name
            name = product[0]
            product_info = product_lookup.get(name, {})
            img = product_info.get('image', product[1] if len(product) > 1 else "")
            price = product_info.get('price', product[2] if len(product) > 2 else "")
            description = product_info.get('description', "No description available.")
            images = product_info.get('images', [img])
            # Check if product is in wishlist by name
            is_favorite = False
            if hasattr(app, 'wishlist'):
                is_favorite = any(item.get('name') == name for item in app.wishlist)
            product_dict = {
                'name': name,
                'price': price,
                'image': img,
                'category': cat_name,
                'images': images,
                'description': description
            }
            card = Builder.load_string(f'''
CategoryProductCard:
    image: "{img}"
    name: "{name}"
''')
            card.bind(on_release=lambda instance, prod=product_dict: self.open_product_details(prod))
            self.product_grid.add_widget(card)

    def parse_price(self, price_str):
        if isinstance(price_str, str):
            cleaned = price_str.replace('₹','').replace(',','').replace('.00','').strip()
            try:
                return float(cleaned)
            except Exception:
                return 0
        return 0

    def open_product_details(self, product):
        app = App.get_running_app()
        app.last_screen = self.manager.current
        details_screen = app.sm.get_screen('product_details')
        details_screen.set_product(
            name=product['name'],
            price=self.parse_price(product.get('price', '')),
            images=product.get('images', [product.get('image', '')]),
            description=product.get('description', 'No description available.'),
            category=product.get('category', '')
        )
        app.sm.current = 'product_details'

    def toggle_wishlist(self, product_name, card, is_favorite):
        app = App.get_running_app()
        # Find the product in the current category
        for product in categories.get(self.current_category, []):
            if product[0] == product_name:
                name, img = product[:2]
                price = product[2] if len(product) > 2 else ""
                break
        else:
            return
        if not hasattr(app, 'wishlist'):
            app.wishlist = []
        if is_favorite:
            # Add to wishlist if not already present
            if not any(item.get('name') == name for item in app.wishlist):
                app.wishlist.append({'name': name, 'image': img, 'price': price, 'category': self.current_category})
        else:
            # Remove from wishlist
            app.wishlist = [item for item in app.wishlist if item.get('name') != name]
        # Optionally, refresh the grid to update favorite icons
        self.show_products(self.current_category)

    def switch_tab(self, tab_name):
        app = App.get_running_app()
        if tab_name == "home":
            app.sm.current = "home"
        elif tab_name == "list":
            app.sm.current = "category"
        elif tab_name == "profile":
            if App.get_running_app().user_logged_in:
                app.sm.current = "profile"
            else:
                app.sm.current = "account_prompt"
