from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line, Translate
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

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

    def add_to_drawing(self, new_stuff):
        self.canvas.add(new_stuff)

# end class SpaceStructure(Widget)



class MainScreen(Screen):
    txt = sdfsys.TextArea()
    spaces_netwrk = []  # array of SpaceStructure widgets
    space_opt_value = 1  # option value toggles {1:'[+]', 0:'[_]'}

    for num in range(8):
        spaces_netwrk.append(SpaceStructure(num))

    def space_button_release(self, num):
        return self.spaces_netwrk[num].change_active_state(self.space_opt_value)

    def parse_button_release(self):
        self.txt.process_text(self.ids.textbox.text)
        self.update_drawing_commands()

        # output text feedback
        self.ids.infobox.text = self.txt.i_txt_str

    def get_i_button_release(self):
        self.ids.textbox.insert_text(chr(10), from_undo=False)
        self.ids.textbox.insert_text(self.ids.infobox.text, from_undo=False)

    def update_drawing_commands(self):
        for command in self.txt.drawing_commands:
            kw = command[0]
            if kw == 'linesegment':
                with self.canvas:
                    # Color(1,0,0,0.45, mode="rgba")
                    Line(points=(
                        (command[1] * 200)+(Window.width / 2),
                        (command[2] * 200)+(Window.height / 2),
                        (command[3] * 200)+(Window.width / 2),
                        (command[4] * 200)+(Window.height / 2)
                    ))

# end class MainScreen(Screen)

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

