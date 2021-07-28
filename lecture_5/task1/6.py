def my_func(fname):
    with open(fname) as f: 
        a = f.readlines()
        print(a)
         
    
my_func('w3res.txt')