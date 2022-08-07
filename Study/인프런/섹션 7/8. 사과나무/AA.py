from collections import deque
n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
dQ = deque()
dQ.append((n//2, n//2))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ind = 0
tsum = 0

while dQ:
    if ind==n//2:
        break
    else:
        for s in range(len(dQ)):
            now = dQ.popleft()
            for a in range(4):
                tx = now[0]+dx[a]
                ty = now[1]+dy[a]
                if nlist[tx][ty] != "vis":
                    tsum+=nlist[tx][ty]
                    nlist[tx][ty] = "vis"
                    dQ.append((tx, ty))
        ind+=1

print(tsum) 
