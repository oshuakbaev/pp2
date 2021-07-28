l = list(map(int, input().split()))
l.sort(key = lambda x: not x)
print(*l)
 