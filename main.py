from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem, TwoLineListItem
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationDrawerItem, MDNavigationDrawerLabel, MDNavigationDrawerMenu
from kivymd.uix.toolbar import MDTopAppBar


# Carrega KV
Builder.load_file("screen.kv")

# Telas
class HomeScreen(Screen):
    pass

# App
class DripApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="Dripe"))
        return sm

    def login(self):
        self.root.current = "Dripe"

DripApp().run()
