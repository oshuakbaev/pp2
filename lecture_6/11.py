def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
if (perfect_number(6)) == True:
    print("OK")
else:
    print("Not OK")