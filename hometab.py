from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.uix.screenmanager import Screen,ScreenManager
from screen_helper import screen_helper

from navigation_drawer import navigation_helper

Window.size = (340, 580)
class Login(Screen):
    pass
class Home(Screen):
    pass

class Autitech(MDApp):

    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        screen = Builder.load_string(navigation_helper)
        return screen

    def on_start(self):
        pass




Autitech().run()