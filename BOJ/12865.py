n, k = map(int, input().split())
dp = [0]*(k+1)

for i in range(n):
    w, v = map(int, input().split())

    for x in range(k, w-1, -1):
        tmp = dp[x-w] + v
        if tmp > dp[x]:
            dp[x] = tmp
        print(dp)
            
print(dp[k])