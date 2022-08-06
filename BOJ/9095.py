t = int(input())
nlist = [int(input()) for _ in range(t)]
dp = [None, 1, 2, 4]
    
for n in nlist:

    while n+1 > len(dp):
        tmp = len(dp)
        dp.append(dp[tmp-1]+dp[tmp-2]+dp[tmp-3])

    print(dp[n])
