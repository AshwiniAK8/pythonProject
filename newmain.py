import serial
import webbrowser
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.uix.screenmanager import Screen,ScreenManager
from screen_helper import screen_helper
from kivy.uix.label import Label
#from GPS import ss

#from Helper import username_helper,password_helper
#from navigation_drawer import navigation_helper
Window.size = (340, 580)
class Login(Screen):
    pass
class Home(Screen):
    pass
class Schedule(Screen):
    pass
class Track(Screen):
    def val1(self):
        print("i am executed")
        webbrowser.open("https://www.google.com/maps/place/Bengaluru,+Karnataka/@12.95396,77.4908527,11z/data=!3m1!4b1!4m5!3m4!1s0x3bae1670c9b44e6d:0xf8dfc3e8517e4fe0!8m2!3d12.9715987!4d77.5945627")

    pass
sm = ScreenManager()
sm.add_widget(Login(name='login'))
sm.add_widget(Home(name='home'))
sm.add_widget(Schedule(name='schedule'))
sm.add_widget(Track(name='track'))
class Autitech(MDApp):
    d = 120
    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

    def build(self):

        self.theme_cls.primary_palette = 'Green'
        screen = Builder.load_string(screen_helper)

        return screen

    def on_start(self):
        pass




Autitech().run()