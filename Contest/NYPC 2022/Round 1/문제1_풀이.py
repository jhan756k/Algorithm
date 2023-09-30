n, m = map(int, input().split())
nlist = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ddx = [1, 1, -1, -1]
ddy = [1, -1, 1, -1]
maxn = -1
maxdn = -1

for x in range(n):
    for y in range(n):

        sval = nlist[x][y]
        dval = nlist[x][y]

        for t in range(4): 
            for i in range(1, m+1):

                tmpdx = x + (dx[t])*i
                tmpdy = y + (dy[t])*i
                tmpddx = x + (ddx[t])*i
                tmpddy = y + (ddy[t])*i

                if 0<=tmpdx<n and 0<=tmpdy<n:
                    sval += nlist[tmpdx][tmpdy]

                if 0<=tmpddx<n and 0<=tmpddy<n:
                    dval += nlist[tmpddx][tmpddy]

        if sval > maxn:
            maxn = sval

        if dval > maxdn:
            maxdn = dval

print(max(maxn, maxdn))
