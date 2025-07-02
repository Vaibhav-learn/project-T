from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty
from widgets.product_card import ProductCard
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.app import App
from functools import partial

Factory.register('ProductCard', module='widgets.product_card')
Builder.load_file('widgets/product_card.kv')

class ProductListScreen(MDScreen):
    products = ListProperty([
        {'name': 'Urban Blaze: Lavender', 'category': 'Women Low Top Sneakers', 'price': '₹2599', 'image': 'assets/product1.png'},
        {'name': 'Pure Karisalankanni Oil', 'category': 'Herbal oils & Legiyams', 'price': '₹2,120.00', 'image': 'assets/product2.png'},
        {'name': 'Solids: Classic Black', 'category': 'Women Boxer Shorts', 'price': '₹499', 'image': 'assets/my_avatar.png'},
        {'name': 'Graphic Tee: Urban', 'category': 'Men Regular T-shirt', 'price': '₹699', 'image': 'assets/logo1.png'},
        {'name': 'Leaf Print Shorts', 'category': 'Casual Beachwear', 'price': '₹899', 'image': 'assets/leaf.png'},
        {'name': 'Classic Logo Sweatshirt', 'category': 'Winter Collection', 'price': '₹1499', 'image': 'assets/logo3.png'},
    ])

    def on_pre_enter(self, *args):
        print("on_pre_enter called")  # DEBUG
        """
        Called before the screen is displayed.
        Initializes or syncs the wishlist state with the app's persistent wishlist,
        and populates the product grid.
        """
        app = App.get_running_app()
        if not hasattr(app, 'wishlist'):
            app.wishlist = [False] * len(self.products)
        elif len(app.wishlist) != len(self.products):
            old_wishlist = app.wishlist
            app.wishlist = [old_wishlist[i] if i < len(old_wishlist) else False for i in range(len(self.products))]
        self.show_products(self.products)
        # Bind search bar events
        search_input = self.ids.get('search_input')
        if search_input:
            search_input.bind(text=self.on_search_text)
            search_input.bind(on_text_validate=self.on_search_enter)

    def on_leave(self, *args):
        # Unbind search bar events to avoid duplicate bindings
        search_input = self.ids.get('search_input')
        if search_input:
            search_input.unbind(text=self.on_search_text)
            search_input.unbind(on_text_validate=self.on_search_enter)

    def on_search_text(self, instance, value):
        if value.strip() == '':
            self.reset_product_filter()
        else:
            self.filter_products_by_search(value)

    def on_search_enter(self, instance):
        value = instance.text
        self.filter_products_by_search(value)

    def show_products(self, products_to_show=None):
        """
        Populates the product grid with a given list of products. If None, shows all products.
        """
        app = App.get_running_app()
        grid = self.ids.product_grid
        grid.clear_widgets()
        grid.cols = 2
        products = products_to_show if products_to_show is not None else self.products
        for idx, product in enumerate(self.products):
            if product not in products:
                continue
            card = ProductCard(
                image=product['image'],
                name=product['name'],
                category=product.get('category', ''),
                price=product['price'],
                is_favorite=app.wishlist[idx],
                on_favorite_toggle=self.make_favorite_callback(idx)
            )
            grid.add_widget(card)

    def filter_products_by_search(self, search_text):
        """
        Filters products by search text and displays them in the product grid.
        """
        search_text = search_text.strip().lower()
        if not search_text:
            self.show_products(self.products)
            return
        filtered = [p for p in self.products if search_text in p['name'].lower() or search_text in p['category'].lower()]
        self.show_products(filtered)

    def reset_product_filter(self):
        self.show_products(self.products)

    def make_favorite_callback(self, idx):
        return lambda card, fav: self.toggle_wishlist(idx, fav)

    def toggle_wishlist(self, idx, is_favorite):
        print(f"toggle_wishlist called for idx={idx}, is_favorite={is_favorite}")  # DEBUG
        app = App.get_running_app()
        app.wishlist[idx] = is_favorite
        print(f"Wishlist after toggle: {app.wishlist}")  # DEBUG
        """
        Toggles the wishlist status for a product at the given index.
        Updates the app-level wishlist, and refreshes the grid.
        """
        self.show_products()

    def go_back(self):
        """
        Navigates back to the home screen.
        """
        app = App.get_running_app()
        app.root.current = 'home'


    def remove_from_wishlist_by_name(self, product_name):
        """
        Removes a product from the wishlist by its name.
        Sets the corresponding wishlist entry to False and updates the app's persistent wishlist.
        """
        app = App.get_running_app()
        for idx, product in enumerate(self.products):
            if product['name'] == product_name:
                app.wishlist[idx] = False
                self.show_products()
                break 