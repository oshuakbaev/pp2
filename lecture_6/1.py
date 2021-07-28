import os 
def max_funct(n,k):
    if n>k:
        return n
    else:
        return k
def max_of_three(n,k,l):
    return max_funct(n,max_funct(k,l))


n,k,l = input(), input(), input()

print(max_of_three(n,k,l))

