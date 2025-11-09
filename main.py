from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem, TwoLineListItem
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
from kivymd.uix.fitimage import FitImage
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationDrawerItem, MDNavigationDrawerLabel, MDNavigationDrawerMenu
from kivymd.uix.toolbar import MDTopAppBar
import os
import requests
from pathlib import Path

# Telas
class HomeScreen(Screen):
    pass

class ShirtScreen(Screen):
    pass

class CapScreen(Screen):
    pass

class BagScreen(Screen):
    pass

class PantsScreen(Screen):
    pass

class ShusScreen(Screen):
    pass

class AbouteScreen(Screen):
    pass

# App
class DripApp(MDApp):
    def build(self):
        # Carrega KV
        Builder.load_file("screen.kv")

        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="Dripe"))
        sm.add_widget(ShirtScreen(name="shirt"))
        sm.add_widget(CapScreen(name="cap"))
        sm.add_widget(BagScreen(name="bag"))
        sm.add_widget(PantsScreen(name="pants"))
        sm.add_widget(ShusScreen(name="shus"))
        sm.add_widget(AbouteScreen(name="aboute"))
        return sm
    
    def show_about(self):
        self.root.current = "aboute"
    
    def api_images(self, tipo=None):
        tipo = tipo or "shoes"
        # requisicao a api
        headers = {"Authorization": "KGAQpaPYQYpIu66870EZigV3B0h5XMrZQICjT7sofJgUs5Lbyuq9KZgk"}
        url = f"https://api.pexels.com/v1/search?query={tipo}&per_page=10"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            fotos = r.json()["photos"]
            return fotos
        else:
            return f"Erro", r.status_code

    def login(self):
        self.root.current = "Dripe"
    
    def go_back(self):
        self.root.current = "Dripe"

    def shirt(self):
        self.root.current = "shirt"
        fotos = self.api_images("shirt")
        container = self.root.get_screen("shirt").ids.cards_container

        for f in fotos:
            card = MDCard(
                size_hint=(None, None),
                size=("350dp", "700dp"),
                orientation="vertical",
                padding="10dp",
                md_bg_color=(1, 1, 1, 1),
                elevation=1,
                radius=[12, 12, 12, 12]
            )
            # Conteúdo do card
            card.add_widget(FitImage(source=f["src"]["large"], size_hint_y=0.6, radius=[12, 12, 0, 0]))
            container.add_widget(card)

    def cap(self):
        self.root.current = "cap"
        fotos = self.api_images("cap")
        container = self.root.get_screen("cap").ids.cards_cap_container
        for f in fotos:
            card = MDCard(
                size_hint=(None, None),
                size=("350dp", "700dp"),
                orientation="vertical",
                padding="10dp",
                md_bg_color=(1, 1, 1, 1),
                elevation=1,
                radius=[12, 12, 12, 12]
            )
            # Conteúdo do card
            card.add_widget(FitImage(source=f["src"]["large"], size_hint_y=0.6, radius=[12, 12, 0, 0]))
            container.add_widget(card)

    def bag(self):
        self.root.current = "bag"
        fotos = self.api_images("bag")
        container = self.root.get_screen("bag").ids.cards_bag_container
        for f in fotos:
            card = MDCard(
                size_hint=(None, None),
                size=("350dp", "700dp"),
                orientation="vertical",
                padding="10dp",
                md_bg_color=(1, 1, 1, 1),
                elevation=1,
                radius=[12, 12, 12, 12]
            )
            # Conteúdo do card
            card.add_widget(FitImage(source=f["src"]["large"], size_hint_y=0.6, radius=[12, 12, 0, 0]))
            container.add_widget(card)

    def pants(self):
        self.root.current = "pants"
        fotos = self.api_images("pants")
        container = self.root.get_screen("pants").ids.cards_pants_container
        for f in fotos:
            card = MDCard(
                size_hint=(None, None),
                size=("350dp", "700dp"),
                orientation="vertical",
                padding="10dp",
                md_bg_color=(1, 1, 1, 1),
                elevation=1,
                radius=[12, 12, 12, 12]
            )
            # Conteúdo do card
            card.add_widget(FitImage(source=f["src"]["large"], size_hint_y=0.6, radius=[12, 12, 0, 0]))
            container.add_widget(card)

    def shus(self):
        self.root.current = "shus"
        fotos = self.api_images("shoes")
        container = self.root.get_screen("shus").ids.cards_shus_container
        for f in fotos:
            card = MDCard(
                size_hint=(None, None),
                size=("350dp", "700dp"),
                orientation="vertical",
                padding="10dp",
                md_bg_color=(1, 1, 1, 1),
                elevation=1,
                radius=[12, 12, 12, 12]
            )
            # Conteúdo do card
            card.add_widget(FitImage(source=f["src"]["large"], size_hint_y=0.6, radius=[12, 12, 0, 0]))
            container.add_widget(card)


if __name__ == "__main__":
    DripApp().run()
