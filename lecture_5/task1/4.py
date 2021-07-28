n = int(input())

a_file = open("w3res.txt","r")

lines = a_file.readlines()

last_lines = lines[::-1]

for i in range(n):
    print(last_lines[i])
    
a_file.close()