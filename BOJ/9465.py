import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*(n) for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    dp[0][1] = dp[1][0] + sticker[0][1]
    dp[1][1] = dp[0][0] + sticker[1][1]
    maxn = -2147000000

    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    for x in range(2, n):
        for y in range(2):
            dp[y][x] = max(dp[abs(1-y)][x-1]+sticker[y][x], dp[abs(1-y)][x-2]+sticker[y][x])
            if dp[y][x]>maxn:
                maxn = dp[y][x]

    print(maxn)
