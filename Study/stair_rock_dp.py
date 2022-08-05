''' ROCK BOTTON_UP
n = int(input())
dp = [0]*(n+2)
dp[1] = 1
dp[2] = 2

for x in range(3, n+2):
    dp[x] = dp[x-1]+dp[x-2]

print(dp[n+1])
'''

''' STAIR TOP_DOWN
n = int(input())
dp = [0]*(n+1)
dp[1]=1
dp[2] = 2

def DFS(v):
    if dp[v]>0:
        return dp[v]

    elif v == 1 or v == 2:
        return v

    else:
        dp[v] = DFS(v-1)+DFS(v-2)
        return dp[v]

DFS(n)
print(dp[n])
'''