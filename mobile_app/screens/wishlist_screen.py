from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from widgets.product_card import ProductCard
from kivy.factory import Factory
from kivy.app import App

class WishlistScreen(MDScreen):
    previous_screen = None

    def go_back(self):
        app = App.get_running_app()
        if hasattr(app, 'last_screen') and app.last_screen:
            self.manager.current = app.last_screen
        else:
            self.manager.current = 'home'

    def set_wishlist(self, products):
        grid = self.ids.wishlist_grid
        grid.clear_widgets()
        if not products:
            from kivymd.uix.label import MDLabel
            grid.add_widget(MDLabel(text='No items in wishlist', halign='center', font_style='H6', size_hint_y=None, height='40dp'))
            return
        for product in products:
            card = ProductCard(
                image=product['image'],
                name=product['name'],
                price=product['price'],
                category=product.get('category', ''),
                is_favorite=True,
                on_favorite_toggle=lambda card, fav, name=product['name']: self.remove_from_wishlist(name) if not fav else None
            )
            grid.add_widget(card)
        # Center single product in grid
        if len(products) == 1:
            grid.add_widget(Widget())

    def remove_from_wishlist(self, product_name):
        app = App.get_running_app()
        product_list_screen = self.manager.get_screen('product_list')
        product_list_screen.remove_from_wishlist_by_name(product_name)
        # Refresh the wishlist
        wishlist_products = [p for p, w in zip(product_list_screen.products, app.wishlist) if w]
        self.set_wishlist(wishlist_products)

    def on_pre_enter(self, *args):
        app = App.get_running_app()
        # Track the previous screen
        if self.manager:
            self.previous_screen = self.manager.current_screen.name if self.manager.current_screen.name != 'wishlist' else self.previous_screen
        product_list_screen = self.manager.get_screen('product_list')
        wishlist_products = [p for p, w in zip(product_list_screen.products, app.wishlist) if w]
        self.set_wishlist(wishlist_products) 