n, m = map(int, input().split())
dp = [0]*(m+1)

for i in range(n):
    w, v = map(int, input().split())

    for x in range(w, m+1):
        tmp = dp[x-w] + v 
        if tmp > dp[x]:
            dp[x]=tmp

print(dp[m])