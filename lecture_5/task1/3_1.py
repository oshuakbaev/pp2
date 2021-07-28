def file_read(fname):
    from itertools import islice
    with open(fname,'w') as myfile:
            myfile.write("Python is the Best!\n")
            myfile.write("JavaScript is the language of allience!\n")

file_read('w3res.txt')