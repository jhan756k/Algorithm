n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
dp = [100]*(m+1)
dp[0] = 0 

for v in nlist:
    for x in range(v, m+1):
        tmp = dp[x-v] + 1
        if tmp < dp[x]:
            print(dp)
            dp[x] = tmp
    
print(dp[m])
