from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.uix.textinput import TextInput

import sdfsys_gamma as sdfsys


class MainScreen(Screen):
    text_data = []
    this_line = []
    this_word = []

    def prep_text_data(self, text):
        print('parse text')

        self.text_data = []

        self.this_line = []
        this_line_is_empty = True

        self.this_word = []
        this_word_is_empty = True

        is_space = True
        is_endline = False

        for char in text:
            ascii = ord(char)

            if ascii is 10:
                is_endline = True
            else:
                is_endline = False

            if (ascii is 32) or (ascii is 9):
                is_space = True
            else:
                is_space = False

            if (not is_space) and (not is_endline):
                # build up word until next space or end of line
                self.this_word.append(char)
                this_word_is_empty = False

            if is_space and (not this_word_is_empty):
                # reached a space after a word
                # join word into a string and add it to line
                self.this_line.append(''.join(self.this_word))
                this_line_is_empty = False

                # reset word
                self.this_word = []
                this_word_is_empty = True


            if is_endline:
                if (not this_word_is_empty):
                    # join word into a string and add it to line
                    self.this_line.append(''.join(self.this_word))
                    this_line_is_empty = False

                    # reset word
                    self.this_word = []
                    this_word_is_empty = True

                if (not this_line_is_empty):
                    self.text_data.append(self.this_line)
                    # reset line
                    self.this_line = []
                    this_line_is_empty = True
        # end for char in text

        if (not this_word_is_empty):
            # join word into a string and add it to line
            self.this_line.append(''.join(self.this_word))
            this_line_is_empty = False

        if (not this_line_is_empty):
            self.text_data.append(self.this_line)

        print(self.text_data)

    # end def prep_text_data(self, text)

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

