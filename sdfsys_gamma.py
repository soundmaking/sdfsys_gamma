# sdfsys gamma
# by Samuel Freeman
# est. Aug 2017

from kivy.uix.widget import Widget
import thisis_gamma

rgba_list = [
    [1., 0., 0., 0.45],     # 0 red
    [1., 0.5, 0., 0.45],    # 1 orange
    [1., 1., 0., 0.45],     # 2 yellow
    [0., 1., 0., 0.45],     # 3 green
    [0., 1., 1., 0.45],     # 4 cyan
    [0., 0.5, 1., 0.45],    # 5 blue
    [0.375, 0., 1., 0.45],  # 6 purple
    [1., 0., 1., 0.45],     # 7 magenta
    [0.5, 0.5, 0.5, 0.45],  # 8 half-way grey
    [1., 1., 1., 0.45],     # 9 inverse  (full contrast to background)
    [0., 0., 0., 1.]        # 10 screen background
]

rgba = {
    0: rgba_list[0],
    1: rgba_list[1],
    2: rgba_list[2],
    3: rgba_list[3],
    4: rgba_list[4],
    5: rgba_list[5],
    6: rgba_list[6],
    7: rgba_list[7],
    8: rgba_list[8],
    9: rgba_list[9],
    10: rgba_list[10],
    'red': rgba_list[0],
    'r': rgba_list[0],
    'orange': rgba_list[1],
    'o': rgba_list[1],
    'yellow': rgba_list[2],
    'y': rgba_list[2],
    'green': rgba_list[3],
    'g': rgba_list[3],
    'cyan': rgba_list[4],
    'c': rgba_list[4],
    'blue': rgba_list[5],
    'b': rgba_list[5],
    'purple': rgba_list[6],
    'p': rgba_list[6],
    'magenta': rgba_list[7],
    'm': rgba_list[7],
    'half': rgba_list[8],
    'grey': rgba_list[8],
    'h': rgba_list[8],
    'inverse': rgba_list[9],
    'i': rgba_list[9],
    'full': rgba_list[9],
    'f': rgba_list[9],
    'screen': rgba_list[10],
    's': rgba_list[10],
    'bg': rgba_list[10]
}


class Bttn:

    x = 0.09  # size_hint value for width
    y = 0.06   # size_hint value for height

    hide = -1

    # Top Row Buttons
    txt_x_hint = x
    spaces_x_hint = 2*x
    i_x_hint = 3*x

    # Left Side Buttons
    prs_y_hint = 1-y

    get_i_x_hint = x/2
    get_i_y_hint = 1-(2*y)

    spc_n_pos_hint = {
        'opt': {'x': 0, 'top': 1-(2*y)},
        0: {'x': 0, 'top': 1-(3*y)},
        1: {'x': x/2, 'top': 1-(3*y)},
        2: {'x': 0, 'top': 1-(4*y)},
        3: {'x': x/2, 'top': 1-(4*y)},
        4: {'x': 0, 'top': 1-(5*y)},
        5: {'x': x/2, 'top': 1-(5*y)},
        6: {'x': 0, 'top': 1-(6*y)},
        7: {'x': x/2, 'top': 1-(6*y)},
        'hide': {'x': hide}
    }

    spc_bttn_text_state = {
        0: '[ ]',
        1: '[-]',
        2: '[=]'
    }

    spc_bttn_text_opt = {
        0: '[_]',
        1: '[+]'
    }



# end class Bttn()


class SysUi:
    bttn = Bttn()

    txt_rgba = rgba['g']
    i_rgba = rgba['m']

    textbox_size_x = 1-bttn.x
    textbox_size_y = 1-(bttn.y*2)

    infobox_size_x = 1-(4*bttn.x)
    infobox_size_y = 1-(bttn.y*2)
    infobox_pos_hint = {'x': 1-infobox_size_x,
                        'top': 1-(bttn.y*0.5)}

# end class SysUi()





class TextArea:
    text_data = []  # buffer for lines of text as lists of strings

    this_line = []  # buffer for one line of text as lists of strings
    this_word = []  # buffer for one word as a list of chars

    thisis = thisis_gamma.Thisis()

    text_parse_return = []  # buffer for messages returned by parse functions

    i_txt_str = ''  # string for output to 'infobox' widget on ui

    parse_is_in_block_comment = False

    drawing_commands = []  #

    def prep_text_data(self, text):
        # prep as in prepare, but also
        # prep as in pre-process...
        #     input text is expected as from a kivy TextInput widget
        #     output is to repopulate the text_data array
        print('prep text ...')

        self.text_data = []

        self.this_line = []
        this_line_is_empty = True

        self.this_word = []
        this_word_is_empty = True

        is_space = True
        is_endline = False

        for char in text:
            ascii_of_char = ord(char)

            if ascii_of_char is 10:
                is_endline = True
            else:
                is_endline = False

            if (ascii_of_char is 32) or (ascii_of_char is 9):
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
                if not this_word_is_empty:
                    # join word into a string and add it to line
                    self.this_line.append(''.join(self.this_word))
                    this_line_is_empty = False

                    # reset word
                    self.this_word = []
                    this_word_is_empty = True

                if not this_line_is_empty:
                    self.text_data.append(self.this_line)
                    # reset line
                    self.this_line = []
                    this_line_is_empty = True
        # end for char in text

        if not this_word_is_empty:
            # join word into a string and add it to line
            self.this_line.append(''.join(self.this_word))
            this_line_is_empty = False

        if not this_line_is_empty:
            self.text_data.append(self.this_line)

        print(len(self.text_data), ' lines found')

    # end def prep_text_data(self, text)

    def parse_line(self, line_index):
        num_lines = len(self.text_data)
        doing_recursion = False

        if line_index < num_lines:

            if line_index < 0:
                # negative number to parse all lines
                doing_recursion = True
                for index in range(num_lines):
                    self.parse_line(index)

            if not doing_recursion:
                if not self.parse_is_in_block_comment:
                    # Get Line to Parse
                    self.this_line = self.text_data[line_index]

                    # Get Keyword
                    kw = self.this_line[0]

                    if kw in thisis_gamma.to_start_block_comment:
                        # start comment block...
                        self.parse_is_in_block_comment = True
                    elif kw not in thisis_gamma.to_comment_line:
                        # line is not comment:

                        if False:
                            # todo implement sdfsys commands and parse for them before thisis
                            pass
                        # end if keyword matches sdfsys dict
                        else:
                            # parse line with thisis
                            print("parse line with thisis...")
                            parse_line_return = self.thisis.parse_line(self.this_line)

                        self.text_parse_return.append(parse_line_return)
                    # end if not comment line
                # end if not self.parse_is_in_block_comment
                else:
                    # is in comment block, so look for end of block
                    kw = self.text_data[line_index][0]
                    if kw in thisis_gamma.to_end_block_comment:
                        self.parse_is_in_block_comment = False
            # end if not doing_recursion
        # end if line_index < lines
        else:
            print('no line', line_index)
    # end def parse_line(self, line_index)

    def add_line_to_string(self, line, string):
        for word in line:
            string += str(word) + chr(32)
        string += chr(10)
        return string

    def process_text(self, text):
        # the text input here is expected as from a kivy TextInput widget

        # reset return buffer and infobox string
        self.text_parse_return = []
        self.i_txt_str = ''

        # pre-process the raw text (string)
        #     into cooked self.text_data (buffer)
        self.prep_text_data(text)

        # recursively parse all lines in self.text_data
        #     and populate self.text_parse_return buffer
        self.parse_line(-1)

        # process the messages returned by parse
        for line_return in self.text_parse_return:
            return_type = line_return[0]
            if return_type == '/_':
                # /_ is drawing data

                # delete the return_type
                del line_return[0]

                # add drawing command to drawing_list
                self.drawing_commands.append(line_return)

            # end if drawing data
            else:
                # add line to info box
                self.i_txt_str = self.add_line_to_string(line_return, self.i_txt_str)



# end class TextArea
