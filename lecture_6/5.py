n = int(input())

def factorial1(n):
    if n == 1:
        return 1 
    else:
        return (n*factorial1((n-1)))


print(factorial1(n))