import sys
sys.setrecursionlimit(10**6)
n = int(input().rstrip())
nlist = [list(map(int, input().rstrip())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = []

def DFS(x, y):
    global cnt
    for i in range(4):
        tx = x+dx[i]
        ty = y+dy[i]
        if 0<=tx<=n-1 and 0<=ty<=n-1 and nlist[tx][ty] == 1:
            cnt+=1
            nlist[tx][ty] = 0
            DFS(tx, ty)
    
for x in range(n):
    for y in range(n):
        if  nlist[x][y] == 1:
            nlist[x][y] = 0
            cnt = 1
            DFS(x, y)
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)
