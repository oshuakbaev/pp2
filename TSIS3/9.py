def result(res):
    print(len(res))
    print(*[str(s) for s in sorted(res)])

N, M = [int(x) for x in input().split()]
Anya = set()
Borya = set()

for i in range(N):
    Anya.add(int(input()))
for i in range(M):
    Borya.add(int(input()))

result(Anya & Borya)
result(Anya - Borya)
result(Borya - Anya)