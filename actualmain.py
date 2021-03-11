import serial
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

    pass
sm = ScreenManager()
sm.add_widget(Login(name='login'))
sm.add_widget(Home(name='home'))
sm.add_widget(Schedule(name='schedule'))
sm.add_widget(Track(name='track'))
class Autitech(MDApp):
    sensor1 = NumericProperty(0)
    sensor2 = NumericProperty(0)
    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

    def build(self):
        try:
            self.arduino = serial.Serial('COM4',9600)
        except:
        print("unable to connect to arduino :(")

        Clock.schedule_interval(self.update, 1)

        self.theme_cls.primary_palette = 'Green'
        screen = Builder.load_string(screen_helper)

        return screen

    def on_start(self):
        pass

    def update(self, *args):
        arduino = self.arduino
        data = arduino.read(arduino.inWaiting())

    def update(self, *args):
        arduino = self.arduino
        data = arduino.read(arduino.inWaiting())
        for line in data.split('\n'):
            try:
                sensor, value = line.strip().split(' ')
            except:
                print("parse error!")
                continue
            if sensor == 'A':
                self.sensor1 = float(value)
            elif sensor == 'B':
                self.sensor2 = float(value)
            else:
                print("unknown data! {}".format(line))




Autitech().run()