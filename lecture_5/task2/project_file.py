import os

"""" 
1. Your current location is disk C directory. (or home directory for Mac OS, Linux)

2. Each time there are two options: you are either work with directory, or with file.

3. If your current location is file you have several options:

a) delete file

b) rename file

c) add content to this file

d) rewrite content of this file

e) return to the parent directory

"""


os.remove("/Users/olzhas/Documents/GitHub/pp2/lecture_5/task2/text.txt")
os.rename(r"/Users/olzhas/Documents/GitHub/pp2/lecture_5/task2/text.txt",r"/Users/olzhas/Documents/GitHub/pp2/lecture_5/task2/text_changed.txt")

with open("example.txt","a") as f:
    f.write("Python bomba)))))")


file = open("example.txt","r+")
file.truncate(0)
file.close()

file = open('example.txt','w')

file.write("Changeable")

print(os.getcwd())




