import sys
n, m = map(int, sys.stdin.readline().split())
bsize = 11
ans = -bsize
dp = [[0 for i in range(bsize)] for j in range(bsize)]

for _ in range(n):
  x, y = map(int, sys.stdin.readline().split())
  dp[x][y] = m-x-y

for i in range(bsize):
  for j in range(bsize):
    if i==0 and j==0:
      continue 
    dp[i][j] = max(dp[i-1][j] + dp[i][j], dp[i][j-1] + dp[i][j])

for i in dp:
  ans = max(ans, max(i))

print(ans)