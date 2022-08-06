n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0, -1, 1, 1, -1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]
cnt = 0

def DFS(x, y):
    for i in range(8):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0<=tx<=n-1 and 0<=ty<=n-1 and nlist[tx][ty] == 1:
            nlist[tx][ty] = 0
            DFS(tx, ty)

for x in range(n):
    for y in range(n):
        if nlist[x][y] == 1:
            nlist[x][y] = 0
            DFS(x, y)
            cnt+=1
            
print(cnt)
