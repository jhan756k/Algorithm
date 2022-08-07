n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n) for _ in range(n)]
dp[0][0] = nlist[0][0]
for x in range(1, n):
    dp[0][x] = dp[0][x-1]+nlist[0][x]
    dp[x][0] = dp[x-1][0]+nlist[x][0]

for x in range(1, n):
    for y in range(1, n):
        if dp[x-1][y] < dp[x][y-1]:
            dp[x][y] = dp[x-1][y]+nlist[x][y]
        else:
            dp[x][y] = dp[x][y-1]+nlist[x][y]
    
print(dp[n-1][n-1])

