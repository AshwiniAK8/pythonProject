import serial
import webbrowser
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.uix.screenmanager import Screen,ScreenManager
from testt import d
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
        ser = serial.Serial('COM4', 9600)
        # b = 'b Latitude in Decimal Degrees : 13.025846\r\n'
        # a= 'b Longitude in Decimal Degrees : 43.245\r\n'
        b = str(ser.readline())
        a = str(ser.readline())
        print(b)
        print(a)
        b1 = b.split()
        a1 = a.split()
        lat1 = b1[-1]
        long1 = a1[-1]
        webbrowser.open('https://www.google.com/maps/search/?api=1&query='+lat1[:-5]+','+long1[:-5])

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