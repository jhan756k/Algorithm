n, x = map(int, input().split())
board = [0]*(65)
dp = [0]*(65)
c1 = [8, 17, 20, 31, 37, 39, 44, 49, 60, 63]
c2 = [2, 6, 10, 19, 23, 25, 27, 43]
c3 = [13, 33, 41, 52, 53, 54]
c5 = [55, 64]
reslist = []
short = [12, 32, 39, 49]

for x in c1:
    board[x] = 1
for x in c2:
    board[x] = 2
for x in c3:
    board[x] = 3
for x in c5:
    board[x] = 5

dp[1] = 0
dp[2] = 2
dp[3] = 2   
dp[4] = 2
dp[5] = 2
dp[6] = 4

for x in range(7, 65):
    if x not in short:
        dp[x] = max(dp[x-6]+board[x], dp[x-5]+board[x], dp[x-4]+board[x], dp[x-3]+board[x], dp[x-2]+board[x], dp[x-1]+board[x])

print(dp[64])
