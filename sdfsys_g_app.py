from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.uix.textinput import TextInput

import sdfsys_gamma as sdfsys


class MainScreen(Screen):
    txt = sdfsys.TextBuffer()




class OtherScreen(Screen):
    pass





class ScreenManagement(ScreenManager):
    pass

interface = Builder.load_file("sdfsys_g_ui.kv")

class SdfsysApp(App):
    def build(self):
        self.title = 'sdfsys gamma'
        return interface

SdfsysApp().run()

