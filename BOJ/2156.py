import sys
n = int(sys.stdin.readline())
wine = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0]*(n+1)
dp[0] = wine[0]
if n>1:
    dp[1] = wine[1] + dp[0]
if n>2:
    dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], dp[1])

for x in range(3, n):
    dp[x] = max(dp[x-1], dp[x-2] + wine[x], wine[x]+wine[x-1]+dp[x-3])
print(dp[n-1])