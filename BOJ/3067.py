import sys
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    c = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    c = [a for a in c if a <= m]
    n = len(c)
    c.insert(0, 0)
    dp = [[0] * (m+1) for _ in range(n+1)]
    if len(c) == 1:
        print(0)
        continue
    for a in range(1, n+1):
        dp[a][c[a]] = 1
        for x in range(c[a]+1, m+1):
            dp[a][x] = dp[a][x-c[a]]
    for x in range(2, n+1):
        for b in range(1, c[x]):
            dp[x][b] = dp[x-1][b]
        for a in range(c[x], m+1):
            dp[x][a] = dp[x][a] + dp[x-1][a]
            tmpx = a - c[x] 
            while tmpx >= 0:
                dp[x][a] += dp[x-1][tmpx]
                tmpx -= c[x]
    print(dp[-1][-1])