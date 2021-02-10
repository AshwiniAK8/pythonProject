from kivy.lang import Builder
screen_helper = """
ScreenManager:
    Login:
    Home:
    
<Login>:
    name:'login'
    Image:
        source: "xx.png"
        pos_hint:{'center_x':0.5,'center_y':0.85}
        size_hint:(0.3,0.3)
    MDRaisedButton:
        text:"Login"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint:(0.2,0.08)
        on_press : root.manager.current='home'
    self.username = Builder.load_string(username_helper)
    self.password = Builder.load_string(password_helper)
        
<Home>:
    name:'home'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Home'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:10
                    
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "profpic.png"
                MDLabel:
                    text: "Name"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: "email@gmail.com"
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]
                ScrollView:
                    DrawerList:
                        id: md_list

                        MDList:
                            OneLineIconListItem:
                                text: "Schedule"
                                on_press : root.manager.current='login'
                                IconLeftWidget:
                                    icon: "face-profile"
                            


                            OneLineIconListItem:
                                text: "Track"

                                IconLeftWidget:
                                    icon: "upload"


                            OneLineIconListItem:
                                text: "Logout"

                                IconLeftWidget:
                                    icon: "logout"
                    
"""