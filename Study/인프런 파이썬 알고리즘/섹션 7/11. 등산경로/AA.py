n = int(input())
mt = []
maxn = -2147000000
minn = 2147000000

for x in range(n):
    tmp = list(map(int, input().split()))
    for a in range(n):
        if tmp[a] < minn:
            minn = tmp[a]
            sa = x
            sb = a
        if tmp[a] > maxn:
            maxn = tmp[a]
            ea = x
            eb = a
    mt.append(tmp)

cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
vis = [[0]*n for _ in range(n)]
vis[0][0] = 1

def DFS(x, y):
    global cnt
    if x==ea and y==eb:
        cnt+=1

    else:
        for i in range(4):
            tx = x+dx[i]
            ty = y+dy[i]
            if 0<=tx<=n-1 and 0<=ty<=n-1 and vis[tx][ty] == 0 and mt[tx][ty] > mt[x][y]:
                vis[tx][ty] = 1
                DFS(tx, ty)
                vis[tx][ty] = 0

DFS(sa, sb)
print(cnt)
