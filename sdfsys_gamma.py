# sdfsys gamma
# by Samuel Freeman
# est. Aug 2017

rgba_list = [
    [1., 0., 0., 0.45],    # red
    [1., 0.5, 0., 0.45],   # orange
    [1., 1., 0., 0.45],    # yellow
    [0., 1., 0., 0.45],    # green
    [0., 1., 1., 0.45],    # cyan
    [0., 0.5, 1., 0.45],   # blue
    [0.375, 0., 1., 0.45], # purple
    [1., 0., 1., 0.45],    # magenta
    [0.5, 0.5, 0.5, 0.45], # half-way grey
    [1., 1., 1., 0.45],    # inverse  (full contrast to background)
    [0.,0.,0.,1.]          # screen background
]

rgba = {
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




class Bttn():

    x = 0.15  # size_hint value for width
    y = 0.1   # size_hint value for height

    hide = -1

    # Top Row Buttons
    txt_x_hint = x
    i_x_hint = 3*x

    # Left Side Buttons
    prs_y_hint = 1-y
    get_i_y_hint = 1-(2*y)



class SysUi():
    bttn = Bttn()

    txt_rgba = rgba['g']
    i_rgba = rgba['m']

    textbox_size_x = 1-(bttn.x)
    textbox_size_y = 1-(bttn.y*2)

    infobox_size_x = 0.4
    infobox_size_y = 1-(bttn.y)


class TextBuffer():
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