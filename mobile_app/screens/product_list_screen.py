from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ListProperty
from widgets.product_card import ProductCard

class ProductListScreen(MDScreen):
    active_tab = StringProperty('women')
    wishlist = ListProperty([False, False, False, False, False])  # One for each product
    products = ListProperty([
        {'name': 'Urban Blaze: Lavender', 'category': 'Women Low Top Sneakers', 'price': '₹2599', 'image': 'assets/product1.png'},
        {'name': 'Urban Blaze: Harley', 'category': 'Women Low Top Sneakers', 'price': '₹2499', 'image': 'assets/product2.png'},
        {'name': 'Urban Blaze: Mafia', 'category': 'Women Low Top Sneakers', 'price': '₹2699', 'image': 'assets/product3.png'},
        {'name': 'Supima: Tap Shoe', 'category': 'Women Supima Pants', 'price': '₹999', 'image': 'assets/product4.png'},
        {'name': 'New Product 5', 'category': 'New Category', 'price': '₹1999', 'image': 'assets/logo.png'}, # Placeholder for product 5
    ])

    def go_back(self):
        if self.manager:
            self.manager.current = 'home'

    def open_search(self):
        print('Search pressed')

    def open_wishlist(self):
        if self.manager:
            wishlist_products = [p for p, w in zip(self.products, self.wishlist) if w]
            wishlist_screen = self.manager.get_screen('wishlist')
            wishlist_screen.set_wishlist(wishlist_products)
            self.manager.current = 'wishlist'

    def open_cart(self):
        print('Cart pressed')

    def switch_tab(self, tab_name):
        self.active_tab = tab_name
        print(f'Switched to tab: {tab_name}')

    def toggle_wishlist(self, product_id):
        idx = product_id - 1
        if 0 <= idx < len(self.wishlist):
            self.wishlist[idx] = not self.wishlist[idx]
            self.property('wishlist').dispatch(self)

    def remove_from_wishlist_by_name(self, product_name):
        for idx, product in enumerate(self.products):
            if product['name'] == product_name:
                self.wishlist[idx] = False
                self.property('wishlist').dispatch(self)
                break 