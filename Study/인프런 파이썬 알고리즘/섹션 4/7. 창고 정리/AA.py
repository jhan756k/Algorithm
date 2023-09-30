n = int(input())
nlist = list(map(int, input().split()))
times = int(input())

for x in range(times):
    nlist.sort()
    nlist[0]+=1
    nlist[-1]-=1

print(max(nlist)-min(nlist))

