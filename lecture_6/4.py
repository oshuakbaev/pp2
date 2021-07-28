string = "1234abcd"
def string_funct(string):
    string = list(string)

    return string[::-1]


print(''.join(string_funct(string)))
