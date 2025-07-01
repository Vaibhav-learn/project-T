from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.properties import ListProperty, NumericProperty
from kivymd.uix.card import MDCard
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.button import MDIconButton
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

class SavedAddressesScreen(MDScreen):
    addresses = ListProperty([])
    selected_index = NumericProperty(-1)

    def on_pre_enter(self, *args):
        self.update_addresses_list()

    def update_addresses_list(self):
        addresses_box = self.ids.addresses_box
        addresses_box.clear_widgets()
        for idx, address in enumerate(self.addresses):
            card = MDCard(orientation="vertical", padding="12dp", size_hint_y=None, height="110dp", radius=[12, 12, 12, 12], md_bg_color=(1,1,1,1))
            card_box = MDBoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")
            card_box.add_widget(
                MDLabel(text=address.get('name', ''), font_style="Subtitle1", bold=True, size_hint_x=0.8)
            )
            card_box.add_widget(
                MDIconButton(icon="pencil-outline", on_release=lambda x, i=idx: self.edit_address(i), theme_text_color="Custom", icon_color=(0,0,0,1))
            )
            card_box.add_widget(
                MDIconButton(icon="trash-can-outline", on_release=lambda x, i=idx: self.delete_address(i), theme_text_color="Custom", icon_color=(1,0,0,1))
            )
            card.add_widget(card_box)
            card.add_widget(MDLabel(text=self.format_address(address), font_style="Body2", size_hint_y=None, height="40dp"))
            check_box_row = MDBoxLayout(orientation="horizontal", size_hint_y=None, height="30dp")
            check_box_row.add_widget(MDCheckbox(active=(idx==self.selected_index), on_active=lambda cb, val, i=idx: self.set_shipping_address(i) if val else None))
            check_box_row.add_widget(MDLabel(text="Use as the shipping address", font_style="Caption", size_hint_x=1))
            card.add_widget(check_box_row)
            addresses_box.add_widget(card)

    def format_address(self, address):
        return f"{address.get('address', '')}\n{address.get('city', '')}, {address.get('state', '')} {address.get('zip', '')}, {address.get('country', '')}"

    def set_shipping_address(self, idx):
        self.selected_index = idx
        self.update_addresses_list()

    def delete_address(self, idx):
        if 0 <= idx < len(self.addresses):
            self.addresses.pop(idx)
            self.addresses = self.addresses  # Force update
            self.update_addresses_list()

    def edit_address(self, idx):
        if 0 <= idx < len(self.addresses):
            address = self.addresses[idx]
            add_screen = self.manager.get_screen('add_edit_address')
            name_parts = address.get('name', '').split(' ', 1)
            add_screen.ids.first_name.text = name_parts[0] if name_parts else ''
            add_screen.ids.last_name.text = name_parts[1] if len(name_parts) > 1 else ''
            add_screen.ids.mobile_number.text = address.get('mobile', '')
            add_screen.ids.pincode.text = address.get('pincode', '')
            add_screen.ids.state.text = address.get('state', '')
            add_screen.ids.city.text = address.get('city', '')
            add_screen.ids.country.text = address.get('country', '')
            add_screen.ids.house.text = address.get('house', '')
            add_screen.ids.road.text = address.get('road', '')
            add_screen.edit_index = idx
            self.manager.current = 'add_edit_address'

    def show_add_address_screen(self):
        add_screen = self.manager.get_screen('add_edit_address')
        add_screen.ids.first_name.text = ''
        add_screen.ids.last_name.text = ''
        add_screen.ids.mobile_number.text = ''
        add_screen.ids.pincode.text = ''
        add_screen.ids.state.text = ''
        add_screen.ids.city.text = ''
        add_screen.ids.country.text = ''
        add_screen.ids.house.text = ''
        add_screen.ids.road.text = ''
        add_screen.edit_index = -1
        self.manager.current = 'add_edit_address'

    def show_add_address_dialog(self):
        self.dialog = MDDialog(
            title="Add New Address",
            type="custom",
            content_cls=MDTextField(
                hint_text="Enter address",
                multiline=True,
            ),
            buttons=[
                MDFlatButton(text="CANCEL", on_release=self.close_dialog),
                MDFlatButton(text="ADD", on_release=self.add_address),
            ],
        )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

    def add_address(self, *args):
        address = self.dialog.content_cls.text.strip()
        if address:
            self.addresses.append(address)
            self.update_addresses_list()
        self.dialog.dismiss()

    def go_back(self):
        self.manager.current = 'profile' 