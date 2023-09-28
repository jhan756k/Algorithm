import sys
n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
res = -1
dp = [0]*n

for p in range(n): 
    dp[0] = 1
    for x in range(1, n):
        if x <= p:              
            maxn = 0
            for i in range(x-1, -1, -1):
                if m[i] < m[x] and dp[i] > maxn:
                    maxn = dp[i]
            dp[x] = maxn + 1
        else:
            maxn = 0
            for j in range(x-1, -1, -1):
                if m[j] > m[x] and dp[j] > maxn:
                    maxn = dp[j]
            dp[x] = maxn +1
    res = max(res, max(dp))
print(res)