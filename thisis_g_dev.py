import thisis_gamma
thisis = thisis_gamma.Thisis()

print('before:')
print(thisis.has_been_put)


line = ['put','z','at','0','0']

thisis.parse_line(line)


print('after:')
print(thisis.has_been_put)