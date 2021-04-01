import serial
import webbrowser
import csv
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from kivy.properties import NumericProperty, StringProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.uix.screenmanager import Screen, ScreenManager
from screen_helper import screen_helper
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.clock import Clock
import random
from kivy.uix.popup import Popup

# from GPS import ss

# from Helper import username_helper,password_helper
# from navigation_drawer import navigation_helper
Window.size = (340, 580)
global ser
global i
i=0
class Login(Screen):
    pass


class Home(Screen):
    global i
    i = 0
    global ser
    ser = serial.Serial('COM4', 9600)
    number = NumericProperty()
    s = StringProperty()
    #number=8
    def __init__(self, **kwargs):
        # The super() builtin
        # returns a proxy object that
        # allows you to refer parent class by 'super'.
        super(Home, self).__init__(**kwargs)

        # Create the clock and increment the time by .1 ie 1 second.
        Clock.schedule_interval(self.increment_time, 0.3)

        #self.increment_time(0)

    # To increase the time / count
    def increment_time(self, interval):
        global ser
        print("RUN")
        a = str(ser.readline())
        b = str(ser.readline())
        bl = str(ser.readline())
        if a.find('Latitude') == -1:
            if a.find('Longitude') == -1:
                b1 = a.split()
                bl1 = b.split()
                a1 = bl.split()
            else:
                b1 = b.split()
                bl1 = bl.split()
                a1 = a.split()
        else:
            b1 = bl.split()
            bl1 = a.split()
            a1 = b.split()
        print(b1)
        BPM1 = b1[-1].split()[0].split('\\')[0]
        print(BPM1)
        if BPM1.find('*') != -1:
            return
        BPM = int(BPM1)
        df = pd.read_csv("HR.csv")
        X = df.iloc[0:, 0].to_numpy()
        print(BPM)
        if BPM>130:
            BPM = random.randint(100,130)
        self.number = BPM
        # X_last = X[-1]
        X[-1] = BPM
        iso = IsolationForest(contamination=0.1)
        prf = iso.fit_predict(X.reshape(-1, 1))
        if prf[-1] == -1:
            lat1 = bl1[-1]
            long1 = a1[-1]
            gps = 'https://www.google.com/maps/search/?api=1&query=' + lat1[:-5] + ',' + long1[:-5]
            self.s = "ALERT!"

    pass


class Schedule(Screen):

    pass


class Track(Screen):
    def val1(self):
        print("i am executed")
        webbrowser.open(
            "https://www.google.com/maps/place/Bengaluru,+Karnataka/@12.95396,77.4908527,11z/data=!3m1!4b1!4m5!3m4!1s0x3bae1670c9b44e6d:0xf8dfc3e8517e4fe0!8m2!3d12.9715987!4d77.5945627")

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

        global i
        #i=0




        self.theme_cls.primary_palette = 'Pink'
        screen = Builder.load_string(screen_helper)

        return screen

    def on_start(self):
        pass


Autitech().run()