n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
for x in range(n):
    nlist[x].append(x+1)

nlist.sort(key= lambda x:(x[2]), reverse=True)
nlist.insert(0,0)
dp = [0]*(n+1)
dp[1]=nlist[1][1]
use=[0]*(n+1)
use[1] = [nlist[1][3]]

for x in range(2, n+1):     
    maxn=0
    tmp = -1
    for i in range(x-1, 0, -1):
        if nlist[x][0] < nlist[i][0]:
            if dp[i] > maxn:
                maxn=dp[i]
                tmp = i

    use[x] = [nlist[x][3]]
    if tmp !=-1:
        use[x]+=use[tmp]

    dp[x] = maxn+nlist[x][1]

ind = dp.index(max(dp)) 
res = use[ind]
print(len(res))

for x in res:
    print(x)
