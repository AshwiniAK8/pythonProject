screen_helper = """
Screen:
   BoxLayout:
       orientation: 'vertical'
       MDToolbar:
           title:'Home Page'
           left_action_items: [["menu",lambda x:app.navigation_draw()]]
           right_action_items: [["clock",lambda x:app.navigation_draw()]]
           elevation:10
       MDLabel:
           text:'Hey guys'
           halign:'center'
       MDBottomAppBar:
           MDToolbar:
               left_action_items: [["coffee",lambda x:app.navigation_draw()]]
               elevation:10
               mode:'end'
               type:'bottom'
               on_action_button:app.navigation_draw()

"""
navigation_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        title:'Home Page'
                        left_action_items: [["menu",lambda x:nav_drawer.toggle_nav_drawer()]]
                        elevation:10
                    
                    Widget:
            MDNavigationDrawer:
                id:nav_drawer
"""
navigation1_helper = """
Screen:
   NavigationLayout:
       ScreenManager:
           Screen:
               BoxLayout:
                   orientation: 'vertical'
                   MDToolbar:
                       title:'Home Page'
                       left_action_items: [["menu",lambda x:nav_drawer.toggle_nav_drawer()]]
                       elevation:10

                   Widget:
       MDNavigationDrawer:
           id:nav_drawer
"""

