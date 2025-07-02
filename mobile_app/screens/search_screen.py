from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from widgets.product_card import ProductCard
from kivy.app import App

class SearchScreen(MDScreen):
    recent_searches = ListProperty([])
     

    def go_back(self):
        if self.manager:
            self.ids.search_input.text = ''
            self.show_results()
            self.manager.current = 'home'

    def add_search(self, text):
        if text and text not in self.recent_searches:
            self.recent_searches.insert(0, text)
            if len(self.recent_searches) > 10:
                self.recent_searches = self.recent_searches[:10]

    def on_pre_enter(self, *args):
        # Bind Enter key to search
        self.ids.search_input.bind(on_text_validate=self.on_enter_search)
        self.show_results()

    def on_leave(self, *args):
        # Unbind Enter key
        self.ids.search_input.unbind(on_text_validate=self.on_enter_search)

    def on_enter_search(self, instance):
        self.show_results()

    def show_results(self):
        search_text = self.ids.search_input.text.strip().lower()
        # Use a grid layout for product cards, similar to product list page
        scrollview = self.ids.search_scroll
        from kivymd.uix.gridlayout import MDGridLayout
        # Remove all children from the ScrollView (so only one widget is present)
        for child in list(scrollview.children):
            scrollview.remove_widget(child)
        self.search_grid = MDGridLayout(cols=2, spacing='8dp', padding=['8dp', '8dp', '8dp', '8dp'], size_hint_y=None)
        self.search_grid.bind(minimum_height=self.search_grid.setter('height'))
        scrollview.add_widget(self.search_grid)
        if not search_text:
            # Show only the first 4 recent searches
            for item in self.recent_searches[:4]:
                list_item = OneLineIconListItem(text=item)
                list_item.add_widget(IconLeftWidget(icon="history"))
                self.search_grid.add_widget(list_item)
        else:
            # Add to recent searches automatically
            self.add_search(self.ids.search_input.text.strip())
            # Search products from ProductListScreen
            product_list_screen = self.manager.get_screen('product_list')
            matches = [p for p in product_list_screen.products if search_text in p['name'].lower() or search_text in p['category'].lower()]
            if not matches:
                from kivymd.uix.label import MDLabel
                self.search_grid.add_widget(MDLabel(text='No products found', halign='center', font_style='H6', size_hint_y=None, height='40dp'))
                return
            for product in matches:
                # Find the index of the product in the main product list
                try:
                    idx = product_list_screen.products.index(product)
                except ValueError:
                    idx = -1
                is_favorite = App.get_running_app().wishlist[idx] if idx != -1 else False
                def make_favorite_callback(idx):
                    return lambda card, fav: product_list_screen.toggle_wishlist(idx, fav)
                card = ProductCard(
                    image=product['image'],
                    name=product['name'],
                    price=product['price'],
                    category=product.get('category', ''),
                    is_favorite=is_favorite,
                    on_favorite_toggle=make_favorite_callback(idx) if idx != -1 else None,
                    on_press_callback=lambda c, n=product['name']: self.open_product_detail(n)
                )
                self.search_grid.add_widget(card)
            # Center single product in grid
            if len(matches) == 1:
                from kivy.uix.widget import Widget
                self.search_grid.add_widget(Widget())

    def open_product_detail(self, product_name):
        # Placeholder for navigation to product detail page
        print(f'Navigate to product detail for: {product_name}') 

    def open_wishlist(self):
        app = App.get_running_app()
        app.last_screen = self.manager.current_screen.name
        app.root.current = 'wishlist'

    def open_cart(self):
        """
        Navigates to the cart screen.
        """
        print('Open cart')
        # app = App.get_running_app()
        # app.root.current = 'cart'