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
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
#from GPS import ss
import csv
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
#from Helper import username_helper,password_helper
#from navigation_drawer import navigation_helper
Window.size = (340, 580)
class Login(Screen):
    pass
class Home(Screen):
    #def sensorrun(self):

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
        ser = serial.Serial('COM4', 9600)
        while (1):
            print("RUN")
            a = str(ser.readline())
            b = str(ser.readline())
            bl = str(ser.readline())
            b1 = bl.split()
            BPM = int(b1[-1].split()[0].split('\\')[0])
            df = pd.read_csv("HR.csv")
            X = df.iloc[0:, 0].to_numpy()
            print(BPM)
            # X_last = X[-1]
            X[-1] = BPM
            iso = IsolationForest(contamination=0.1)
            prf = iso.fit_predict(X.reshape(-1, 1))
            if prf[-1] == -1:
                bl1 = b.split()
                a1 = a.split()
                lat1 = bl1[-1]
                long1 = a1[-1]
                gps = 'https://www.google.com/maps/search/?api=1&query=' + lat1[:-5] + ',' + long1[:-5]
                print("ALERT!")

        return screen

    def on_start(self):
        pass




Autitech().run()