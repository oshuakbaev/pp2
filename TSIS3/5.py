n = input().split()
k = int(input())
k = k%len(n)
if k<0:
    k = abs(k)
    print(*n[k:],end =' ')
    print(*n[0:k])
    exit()
 
if k>=0:
    k = abs(k)
    print(*n[-k:],end =' ')
    print(*n[0:-k])
    exit()