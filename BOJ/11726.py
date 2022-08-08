n = int(input())
dp = [0]*(n+5)
dp[1] = 1
dp[2] = 2
dp[3] = 3

for x in range(4, n+1):
    dp[x] = dp[x-1]+dp[x-2]

print(dp[n]%10007)