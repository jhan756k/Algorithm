from collections import deque   
m, n = map(int, input().split())
nlist = [list(map(int, input().split())) for _ in range(n)]
dis = [[0]*m for _ in range(n)]
dQ = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for x in range(n):
    for y in range(m):
        if nlist[x][y] == 1:
            dQ.append((x, y))

while dQ:
    now = dQ.popleft()
    for i in range(4):
        tx = now[0] + dx[i]
        ty = now[1] + dy[i]
        if 0<=tx<=n-1 and 0<=ty<=m-1 and nlist[tx][ty] == 0:
            nlist[tx][ty] = 1
            dis[tx][ty] = dis[now[0]][now[1]] + 1
            dQ.append((tx, ty))

f = False
res = 0
for a in range(n):
    for b in range(m):
        if nlist[a][b] == 0:
            print(-1)
            f = True
            break
    if f:
        break
else:
    for c in range(n):
        for d in range(m):
            if dis[c][d] > res:
                res = dis[c][d]
    print(res)
