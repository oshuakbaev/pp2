addr = list(input())

for x in addr:
    if x == ".":
        index = addr.index(x)
        addr.remove(x)
        addr.insert(index,'[.]')

addr2 = ''.join(addr)

print(addr2)

