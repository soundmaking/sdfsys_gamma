#

keyword_list = ['put']


class Thisis:
    has_been_put = {}


    # put is the fundamental thisis command with syntax structure:
    #     put <point name> <put type [at|on|where|group]> <(additional info to specify where)>
    def parse_line(self, line):
        kw = line[0]
        print('kw = ',kw)

        if kw == 'put':
            pnt_name = line[1]
            put_type = line[2]
            print('type = ', put_type)
            if put_type == 'at':
                x = float(line[3])
                y = float(line[4])
                print("x,y = ",[x,y])
                self.has_been_put[pnt_name] = [x,y]
                print('has_been_put = ', self.has_been_put)
            # end if put_type is 'at'

        # end if kw is 'put'
        else:
            print('?')
    # end def parse_line(self, line)