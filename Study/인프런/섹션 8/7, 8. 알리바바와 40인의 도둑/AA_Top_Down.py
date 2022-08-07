n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

def DFS(x, y):
    
    if dp[x][y]!=0:
        return dp[x][y]

    if x==0 and y==0:
        dp[x][y] = nlist[0][0]
        return dp[x][y]

    else:
        if y==0:
            dp[x][y] = DFS(x-1, y) + nlist[x][y]
            return dp[x][y]

        elif x==0:
            dp[x][y] = DFS(x, y-1) + nlist[x][y]
            return dp[x][y]

        else:
            dp[x][y] =  min(DFS(x,y-1), DFS(x-1,y))+nlist[x][y]
            return dp[x][y] 

print(DFS(n-1, n-1))