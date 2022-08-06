n = int(input())
nlist = [list(map(int, input())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
res = []

def DFS(x, y):
    global cnt
    cnt+=1
    nlist[x][y] = 0
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0<=tx<=n-1 and 0<=ty<=n-1 and nlist[tx][ty] == 1:
            DFS(tx, ty)

for x in range(n):
    for y in range(n):
        if nlist[x][y] == 1:
            cnt=0
            DFS(x, y)
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)      
