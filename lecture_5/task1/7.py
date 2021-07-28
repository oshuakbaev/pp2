def my_funct(object):
    array = [] # but we all know that is the list :)
    with open(object) as f: 
        for i in f: 
            array.append(i)
        print(array)
        


my_funct("w3res.txt")