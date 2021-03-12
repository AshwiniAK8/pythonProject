from kivy.lang import Builder
screen_helper = """
ScreenManager:
    Login:
    Home:
    Schedule:
    Track:
    
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
    MDTextField:
        hint_text:"Enter username"
        helper_text_mode:"on_focus"
        pos_hint : {'center_x':0.5,'center_y':0.7}
        size_hint_x:None
        width:300
    MDTextField:
        hint_text:"Enter password"
        helper_text: "or click on forgot username password"
        helper_text_mode:"on_focus"
        pos_hint : {'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:300
        
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
                                text: "Activites"
                                on_press : root.manager.current='schedule'
                                IconLeftWidget:
                                    icon: "face-profile"
                            


                            OneLineIconListItem:
                                text: "Track"
                                on_press : root.manager.current='track'
                                
                                
                                IconLeftWidget:
                                    icon: "upload"


                            OneLineIconListItem:
                                text: "Logout"
                                on_press : root.manager.current='login'
                                IconLeftWidget:
                                    icon: "logout"
<Track>:
    name:'track'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Track'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:10
                    MDLabel:
                        text: lat1
                        halign:'center'
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
                                text: "Activites"
                                on_press : root.manager.current='schedule'
                                IconLeftWidget:
                                    icon: "face-profile"
                            


                            OneLineIconListItem:
                                text: "Track"

                                IconLeftWidget:
                                    icon: "upload"


                            OneLineIconListItem:
                                text: "Logout"
                                on_press : root.manager.current='login'
                                IconLeftWidget:
                                    icon: "logout"
                                    
<Schedule>:
    name:'schedule'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Activites'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:10
                    ScrollView:
                    DrawerList:
                        id: md_list

                        MDList:
                            TwoLineListItem:
                                text: "Brush Teeth"
                                secondary_text: "9:00"      
                            TwoLineListItem:
                                text: "Eat Breakfast"
                                secondary_text: "9:30" 
                            TwoLineListItem:
                                text: "Study time"
                                secondary_text: "10:00 - 11:00"
                            TwoLineListItem:
                                text: "Music session"
                                secondary_text: "11:30 - 12:30"
                            TwoLineListItem:
                                text: "Leisure time"
                                secondary_text: "12:30 - 1:00"    
                            TwoLineListItem:
                                text: "Eat Lunch"
                                secondary_text: "1:00"
                            TwoLineListItem:
                                text: "Nap Time"
                                secondary_text: "1:30 - 2:30"                           


                                                   
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
                                text: "Home"
                                on_press : root.manager.current='home'
                                IconLeftWidget:
                                    icon: "face-profile"
                            


                            OneLineIconListItem:
                                text: "Track"
                                on_press : root.manager.current='track'
                                

                                IconLeftWidget:
                                    icon: "upload"


                            OneLineIconListItem:
                                text: "Logout"
                                on_press : root.manager.current='login'
                                IconLeftWidget:
                                    icon: "logout"
       
       


"""