from kivymd.app import MDApp
from kivymd.uix.widget import Widget
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang.builder import Builder
from kivy.uix.image import Image

screens = """
ScreenManager:
    MainScreen:
    HomeScreen:

############# Contine pagina principala a aplicatiei, acolo unde se afla o imagine reprezentativa si un buton care in urma apasarii user-ul poate incepe navigarea prin aplicatie ########################  
<MainScreen>
    name:'main'
    Image:
        pos: self.pos
        size_hint: None, None
        size: root.size
        allow_stretch: True
        keep_ratio: False
        source:"images/MainScreenImage.png"
    MDRaisedButton:
        text: 'Descopera Romania'
        md_bg_color:'red'
        pos_hint: {'center_x' :0.5, 'center_y':0.4}
        on_press: root.manager.current  = 'home'

############# Contine pagina principala din interiorul aplicatiei, acolo unde se va gasi un nav-drawe
<HomeScreen>
    name:'home'
"""

class MainScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MainScreen(name = 'main'))
sm.add_widget(HomeScreen(name = 'home'))

class MainApp(MDApp):
    def build(self):
        screen = Builder.load_string(screens)
        return screen

MainApp().run()