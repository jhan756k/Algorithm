n = int(input())
stair = [int(input()) for _ in range(n)]
stair.insert(0,0)
stair +=[0]*4
dp = [0]*(n+5)

dp[1] = stair[1]
dp[2] = max(stair[1] + stair[2], stair[2])
dp[3] = max(stair[1] + stair[3], stair[2]+stair[3])

for x in range(4, n+1):
    dp[x] = max(stair[x]+dp[x-2], stair[x]+stair[x-1]+dp[x-3])

print(dp[n])
