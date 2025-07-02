from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from widgets.product_card import ProductCard

class WishlistScreen(MDScreen):
    def go_back(self):
        if self.manager:
            self.manager.current = 'product_list'

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
                secondary_label='MRP incl. of all taxes',
                show_heart=True,
                heart_filled=True,
                heart_press_callback=self._make_remove_callback(product['name'])
            )
            grid.add_widget(card)

    def _make_remove_callback(self, product_name):
        def callback(card):
            self.remove_from_wishlist(product_name)
        return callback

    def remove_from_wishlist(self, product_name):
        product_list_screen = self.manager.get_screen('product_list')
        product_list_screen.remove_from_wishlist_by_name(product_name)
        # Refresh the wishlist
        wishlist_products = [p for p, w in zip(product_list_screen.products, product_list_screen.wishlist) if w]
        self.set_wishlist(wishlist_products) 