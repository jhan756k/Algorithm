str_1 = str(input())
str_2 = str(input())
a = len(str_1)
b = len(str_2)
dp = [[0]*(a+1) for _ in range(b+1)]
res = 0

for x in range(1, b+1):
    for y in range(1, a+1):
        if str_1[y-1] == str_2[x-1]:
            dp[x][y] = dp[x-1][y-1] + 1
        else:
            dp[x][y] = max(dp[x-1][y], dp[x][y-1])

        if dp[x][y] > res:
            res = dp[x][y]

print(res)
