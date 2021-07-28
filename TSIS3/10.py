n = int(input())

d = dict()

for i in range(n):
    syn1, syn2 = input().split()
    d[syn1] = syn2
    d[syn2] = syn1

print(d[input()])
