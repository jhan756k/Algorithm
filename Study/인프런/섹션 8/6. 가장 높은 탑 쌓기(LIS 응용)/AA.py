n = int(input())
nlist = [tuple(map(int, input().split())) for _ in range(n)]
nlist.sort(key= lambda x:(x[2]), reverse=True)
nlist.insert(0,0)
dp = [0]*(n+1)
dp[1]=nlist[1][1]

for x in range(2, n+1):     
    maxn=0
    for i in range(x-1, 0, -1):
        if nlist[x][0] < nlist[i][0]:
            if dp[i] > maxn:
                maxn=dp[i]

    dp[x] = maxn+nlist[x][1]

print(max(dp))
