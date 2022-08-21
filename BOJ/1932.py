n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*a for a in range(1, n+1)]
if n == 1:
    print(nlist[0][0])
    exit()

dp[0][0] = nlist[0][0]
dp[1][0] = nlist[1][0]+dp[0][0]
dp[1][1] = nlist[1][1]+dp[0][0]

for x in range(2, n):
    for a in range(x+1):
        if a == 0:
            dp[x][a] = dp[x-1][a]+nlist[x][a]

        elif a == x:
            dp[x][a] = dp[x-1][a-1]+nlist[x][a]
        
        else:
            dp[x][a] = max(dp[x-1][a-1]+nlist[x][a], dp[x-1][a]+nlist[x][a])

maxn = -1
for x in dp[-1]:
    if x > maxn:
        maxn = x
print(maxn)
