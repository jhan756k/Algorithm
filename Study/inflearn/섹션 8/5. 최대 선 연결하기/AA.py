n = int(input())
nlist = list(map(int, input().split()))
nlist.insert(0,0)
dp = [0]*(n+1)
dp[1] = 1

for x in range(2, n+1):
    maxn = 0
    for j in range(x-1, 0, -1):
        if nlist[j] < nlist[x] and dp[j] > maxn:
            maxn = dp[j]
    dp[x] = maxn+1

print(max(dp))
