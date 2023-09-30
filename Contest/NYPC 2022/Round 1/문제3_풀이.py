import sys
input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split()))

if n == 1:
    print(nlist[0])
    exit()

maxn = 0
dp = [0]*(n)

dp[0] = nlist[0]

for x in range(1, n): 
    dp[x] = max(dp[x-1]+nlist[x], nlist[x])

resm = max(dp)

for x in nlist:
    if x > 0:
        maxn+=x

for l in range(n): 
    for r in range(l+1, n):

        if nlist[r:l-1:-1] == nlist[l:r+1]:
            continue

        for x in range((r-l+1)//2): 
            nlist[l+x], nlist[r-x] = nlist[r-x], nlist[l+x]

        dp[0] = nlist[0]

        for x in range(1, n): 
            dp[x] = max(dp[x-1]+nlist[x], nlist[x])

        resm = max(resm, max(dp))
    
        if resm == maxn:
            print(resm)
            exit()

        for x in range((r-l+1)//2):
            nlist[l+x], nlist[r-x] = nlist[r-x], nlist[l+x]

print(resm)
        