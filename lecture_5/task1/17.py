def remove_newlines(fname):
    flist = open(fname).readlines()
    return new_func(flist)

def new_func(flist):
    return [s.rstrip('\n') for s in flist]

print(remove_newlines("/Users/olzhas/Documents/GitHub/pp2/lecture_5/task1/w3res.txt"))