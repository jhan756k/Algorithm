from collections import deque
n = int(input())
nlist =[list(map(int, input())) for _ in range(n)]
dQ = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = []

def BFS():
    global cnt
    while dQ:
        now = dQ.popleft()
        for i in range(4):
            tx = now[0] + dx[i]
            ty = now[1] + dy[i]
            if 0<=tx<=n-1 and 0<=ty<=n-1 and nlist[tx][ty] == 1 :
                dQ.append((tx, ty))
                nlist[tx][ty] = 0
                cnt+=1

    res.append(cnt)

for x in range(n):
    for y in range(n):
        if nlist[x][y] == 1:
            nlist[x][y] = 0
            cnt = 1
            dQ.append((x, y))
            BFS()

res.sort()
print(len(res))
for x in res:
    print(x)
