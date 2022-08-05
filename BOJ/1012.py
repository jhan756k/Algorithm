import sys
sys.setrecursionlimit(10**6)
t = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = []

def DFS(x, y):
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0<=tx<=n-1 and 0<=ty<=m-1 and nlist[tx][ty] == 1:
            nlist[tx][ty] = 0
            DFS(tx, ty)

for times in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    nlist = [[0]*m for _ in range(n)]
    
    for b in range(k):
        tmpx, tmpy = map(int, input().split())
        nlist[tmpy][tmpx] = 1

    for x in range(n):
        for y in range(m):
            if nlist[x][y] == 1:
                nlist[x][y] = 0
                DFS(x, y)
                cnt+=1

    res.append(cnt)

for x in res:
    print(x)
