n = int(input())
nlist = list(map(int, input().split()))
nlist.insert(0,0)
dp = [0]*(n+1)
dp[1]=1

for x in range(2, n+1):
    maxn=0
    for i in range(x-1, 0, -1):
        if nlist[x] > nlist[i]:
            if dp[i] > maxn:
                maxn = dp[i]
    dp[x] = maxn+1 

print(max(dp))
