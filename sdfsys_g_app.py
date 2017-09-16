from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.uix.textinput import TextInput

import sdfsys_gamma as sdfsys

sdfsysui = sdfsys.SysUi()

class SpaceStructure(Widget):
    def __init__(self, space_number, **kwargs):
        super(SpaceStructure, self).__init__(**kwargs)
        self.space_number = space_number
        self.rgba = sdfsys.rgba[space_number]
        self.active_state = 1

    def change_active_state(self, opt_val):
        if opt_val == 1:
            if self.active_state < 1:
                self.active_state = 2
            else:
                self.active_state = (-1*self.active_state)+3
        elif opt_val == 0:
            if self.active_state > 0:
                self.active_state = 0
            else:
                self.active_state = 1
        print('active state', self.active_state)

        # return text for the ui button
        bttn_txt = sdfsysui.bttn.spc_bttn_text_state[self.active_state]
        print(bttn_txt)
        return bttn_txt




class MainScreen(Screen):
    txt = sdfsys.TextArea()
    spaces_netwrk = []  # array of SpaceStructure widgets
    space_opt_value = 1

    for num in range(8):
        spaces_netwrk.append(SpaceStructure(num))

    def space_button_release(self, num):
        return self.spaces_netwrk[num].change_active_state(self.space_opt_value)


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

