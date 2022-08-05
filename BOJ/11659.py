import sys
n, m = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))
slist = [0]

tmp = 0
for a in nlist:
    tmp+=a
    slist.append(tmp)

for x in range(m):
    tx, ty = map(int, sys.stdin.readline().split())
    print(slist[ty] - slist[tx-1])