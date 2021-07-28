def my_funct(text):
    with open(text) as f: 
        a = f.readlines()
    print(a)
    

print(my_funct("/Users/olzhas/Documents/GitHub/pp2/lecture_5/task1/w3res.txt"))