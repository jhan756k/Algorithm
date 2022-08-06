from collections import deque 
n = int(input())
nlist = []
maxn = -2147000000
minn = 2147000000
dQ = deque()
res = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    tmp = list(map(int, input().split()))
    for j in tmp:
        if j > maxn:
            maxn = j
        
        elif j < minn:
            minn = j

    nlist.append(tmp)


for height in range(minn, maxn):
    ch = [[0]*n for _ in range(n)]
    cnt = 0

    for x in range(n):
        for y in range(n):
            if nlist[x][y] > height and ch[x][y] == 0:
                dQ.append((x,y))
                ch[x][y] = 1
                while dQ:   
                    now = dQ.popleft()
                    for i in range(4):
                        tx = now[0] + dx[i]
                        ty = now[1] + dy[i]
                        if 0<=tx<=n-1 and 0<=ty<=n-1 and nlist[tx][ty] > height and ch[tx][ty] == 0:
                            dQ.append((tx, ty))
                            ch[tx][ty] = 1
                cnt+=1

    res = max(res, cnt)

if res == 0:
    print(1)

else:
    print(res)
