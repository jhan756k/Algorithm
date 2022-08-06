import sys
sys.setrecursionlimit(10**6)
n = int(input())
dp = [0]*(n+1)

def DFS(v):
    if dp[v] > 0:
        return dp[v] 

    if v == 1 or v == 2:
        return v
    else:
        dp[v] = DFS(v-1)+DFS(v-2)
        return dp[v]

print(DFS(n))
