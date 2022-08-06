t = int(input())

for _ in range(t):
    n = int(input())
    dp = [None, 1,1,1,2,2,3,4,5,7,9] + [0]*(n-9)

    for x in range(11, n+1):
        dp[x] = dp[x-1] + dp[x-5]

    print(dp[n])
