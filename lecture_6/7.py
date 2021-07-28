import string


string1 = "The quick Brow Fox"

def upper_case(string1):
    res = 0
    for i in string1: 
        if ord(i)>=65 and ord(i)<=90:
            res+=1
    return res 

def lower_case(string1):
    res = 0
    for i in string1: 
        if ord(i)>=87 and ord(i)<=122:
            res+=1
    return res 
    


print(upper_case(string1))
print(lower_case(string1))