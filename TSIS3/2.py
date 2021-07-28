a = input().split()
b = []

for i in range(len(a)):
    a[i] = int(a[i])
    if a[i]<0:
        continue
    else:
        b.append(a[i])

print(min(b))
