import sys
n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
pf = []
cnt = [0] * (m+1)
res = 0
for x in range(n):
    if x == 0:
        tmp = l[x]
    else:
        tmp = pf[x-1] + l[x]
    if tmp%m == 0:
        res+=1
    pf.append(tmp)
for x in range(n):
    cnt[pf[x]%m] += 1
for x in cnt:
    if x!=0:
        res += (x*(x-1)//2)
print(res)