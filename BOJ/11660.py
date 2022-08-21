import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nlist = [list(map(int, input().split())) for _ in range(n)]

for x in range(n):
    for y in range(n):
        if x == 0 and y == 0:
            continue

        elif x == 0:
            nlist[x][y] = nlist[x][y-1] + nlist[x][y]

        elif y == 0:
            nlist[x][y] = nlist[x-1][y] + nlist[x][y]

        else:
            nlist[x][y] = nlist[x-1][y] + nlist[x][y-1] - nlist[x-1][y-1] + nlist[x][y]

nlist.insert(0, [0]*(n+1))

for x in nlist:
    x.insert(0, 0)

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    res = nlist[x2][y2] - nlist[x2][y1-1] - nlist[x1-1][y2] + nlist[x1-1][y1-1]
    print(res)
