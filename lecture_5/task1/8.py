def max_function(object):
    with open(object) as f: 
        max = 0 
        a = f.readlines()

        for i in a: 
            if len(i)>max:
                max = len(i)
        print(max)



max_function("w3res.txt")