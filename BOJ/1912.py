n = int(input())
nlist = list(map(int, input().split()))

for x in range(1, n):
    
    nlist[x] = max(nlist[x-1] + nlist[x], nlist[x])

print(max(nlist))
