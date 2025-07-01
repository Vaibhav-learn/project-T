from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty
from widgets.product_card import ProductCard
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.app import App

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
    wishlist = ListProperty([])

    def on_pre_enter(self, *args):
        app = App.get_running_app()
        if not hasattr(app, 'wishlist') or not app.wishlist:
            app.wishlist = [False] * len(self.products)
        elif len(app.wishlist) != len(self.products):
            old_wishlist = app.wishlist
            app.wishlist = [old_wishlist[i] if i < len(old_wishlist) else False for i in range(len(self.products))]
        self.wishlist = app.wishlist
        self.populate_product_grid()

    def populate_product_grid(self):
        grid = self.ids.product_grid
        grid.clear_widgets()
        grid.cols = 2
        print(f"Populating grid with {len(self.products)} products")
        for idx, product in enumerate(self.products):
            # print(f"Adding product: {product['name']}, image: {product['image']}")
            card = ProductCard(
                image=product['image'],
                name=product['name'],
                category=product.get('category', ''),
                price=product['price'],
                is_favorite=self.wishlist[idx],
                on_favorite_toggle=lambda card, fav, i=idx: self.toggle_wishlist(i, fav)
            )
            grid.add_widget(card)

    def toggle_wishlist(self, idx, is_favorite):
        self.wishlist[idx] = is_favorite
        App.get_running_app().wishlist = self.wishlist

    def remove_from_wishlist_by_name(self, product_name):
        for idx, product in enumerate(self.products):
            if product['name'] == product_name:
                self.wishlist[idx] = False
                break
        # Optionally, update the product grid to reflect the change
        self.populate_product_grid() 