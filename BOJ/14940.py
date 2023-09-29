import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
bd = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
res = [[-1]*m for _ in range(n)]
vis = [[False]*m for _ in range(n)]
dQ = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for x in range(n):
    for y in range(m):
        if bd[x][y] == 2:
            dQ.append((x, y))
            res[x][y] = 0
            vis[x][y] = True
        if bd[x][y] == 0:
            res[x][y] = 0
while dQ:
    a, b = dQ.popleft()
    for i in range(4):
        tmpx = a + dx[i]
        tmpy = b + dy[i]
        if 0<=tmpx<n and 0<=tmpy<m and bd[tmpx][tmpy] == 1 and not vis[tmpx][tmpy]:
            dQ.append((tmpx, tmpy))
            vis[tmpx][tmpy] = True
            res[tmpx][tmpy] = res[a][b] + 1
for x in res:
    print(*x)