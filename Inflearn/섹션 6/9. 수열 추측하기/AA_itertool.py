import itertools as it 

n, f= map(int, input().split())
b = [1]*n
for x in range(1, n):
    b[x] = b[x-1]*(n-x)/x

a = list(range(1, n+1))

for tmp in it.permutations(a):
    t = 0
    for x in range(n):
        t+=b[x]*tmp[x]

    if t == f:
        for x in tmp:
            print(x, end = " ")
        print()
        break