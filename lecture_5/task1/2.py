"""f = open('w3res.txt','r')

print(f.readline())"""


def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('w3res.txt',2)
