n, m = map(int, input().split())
dp = [0]*(m+1)

for i in range(n):
    pv, pt = map(int, input().split())
    for j in range(m, pt-1, -1):
        tmp = dp[j-pt]+pv
        if dp[j] < tmp:
            dp[j] = tmp

print(dp[m])    