from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from widgets.product_card import ProductCard

class SearchScreen(MDScreen):
    recent_searches = ListProperty([
        'Shoes',
        'Crop Red Tee',
        'Crop Tshirt For Women',
        'Crop Tshirt For Women',
        'Crop Red Tee',
    ])

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
        self.ids.recent_list.clear_widgets()
        if not search_text:
            # Show only the first 4 recent searches
            for item in self.recent_searches[:4]:
                list_item = OneLineIconListItem(text=item)
                list_item.add_widget(IconLeftWidget(icon="history"))
                self.ids.recent_list.add_widget(list_item)
        else:
            # Add to recent searches automatically
            self.add_search(self.ids.search_input.text.strip())
            # Search products from ProductListScreen
            product_list_screen = self.manager.get_screen('product_list')
            matches = [p for p in product_list_screen.products if search_text in p['name'].lower() or search_text in p['category'].lower()]
            if not matches:
                from kivymd.uix.label import MDLabel
                self.ids.recent_list.add_widget(MDLabel(text='No products found', halign='center', font_style='H6', size_hint_y=None, height='40dp'))
                return
            for product in matches:
                card = ProductCard(image=product['image'], name=product['name'], price=product['price'], on_press_callback=lambda c, n=product['name']: self.open_product_detail(n))
                self.ids.recent_list.add_widget(card)

    def open_product_detail(self, product_name):
        # Placeholder for navigation to product detail page
        print(f'Navigate to product detail for: {product_name}') 