import thisis_gamma

thisis = thisis_gamma.Thisis()

print('before:')
print(thisis.has_been_put)


line = ['put','z','at','0','0']

thisis.parse_line(line)


print('after:')
print(thisis.has_been_put)

ret = thisis_gamma.return_types_dict

print('ret keys:', ret.keys())

print('\n ... \n')

com = thisis_gamma.to_comment_line

print('com:', com)
