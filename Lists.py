from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton,MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from Helper import username_helper,password_helper
from kivy.uix.image import Image
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
Window.size=(360,600)

class AutitechApp(MDApp):

    def build(self):
        screen = Screen()
        img =Image(source = "xx.png",pos_hint=
        {'center_x':0.5,'center_y':0.85},size_hint=(0.3,0.3))
        self.theme_cls.primary_palette="Red"
        #Self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style = "Light"
        # sername = MDTextField(text='Enter username',pos_hint=
        # {'center_x':0.5,'center_y':0.5},size_hint=(0.5,1))
        button = MDRaisedButton(text="Login",pos_hint=
        {'center_x':0.5,'center_y':0.5},size_hint=(0.2,0.08),on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        self.password = Builder.load_string(password_helper)
        #if(self.username.text is ""):
         #   check_string = "Please enter a valid username"
        #  self.dialog=MDDialog(title="Username Check", text = self.username.text,
         #                        size_hint = (0.7,1),buttons=[close_button])
         #   self.dialog.open()
        screen.add_widget(self.username)
        screen.add_widget(self.password)
        screen.add_widget(button)
        screen.add_widget(img)
        return screen
    def show_data(self,obj):
        print(self.username.text)

AutitechApp().run()
