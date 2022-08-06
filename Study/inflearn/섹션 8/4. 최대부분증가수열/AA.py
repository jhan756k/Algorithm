n = int(input())
nlist = list(map(int, input().split()))
nlist.insert(0,0)
dp=[0]*(n+1)
dp[1] = 1

for i in range(2, n+1):
    maxn = 0
    for j in range(i-1, 0, -1):
        if nlist[j] < nlist[i] and dp[j]>maxn:
            maxn = dp[j]
    dp[i] = maxn+1 
    
print(max(dp))