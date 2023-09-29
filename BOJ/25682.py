import sys
n, m ,k = map(int, sys.stdin.readline().split())
board = []
tmpx = [0 if a%2==0 else 1 for a in range(m)]
tmpy = [1 if a%2==0 else 0 for a in range(m)]
ans1 = [tmpx if a%2==0 else tmpy for a in range(n)]
ans2 = [tmpy if a%2==0 else tmpx for a in range(n)]
ans = [ans1, ans2]
res = 4000001 
for x in range(n):
    tmp = list(str(sys.stdin.readline().rstrip()))
    tmp = [0 if a == 'B' else 1 for a in tmp]
    board.append(tmp)
for a in range(2):
    t, pf, p = [[0]*m for _ in range(n)], [[0]*m for _ in range(n)], [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            t[x][y] = abs(ans[a][x][y] - board[x][y])
    for x in range(n):
        for y in range(m):
            if y == 0:
                pf[x][y] = t[x][y]
            pf[x][y] = pf[x][y-1] + t[x][y]
    for y in range(m):
        for x in range(n):
            if x == 0:
                p[x][y] = pf[x][y]
            p[x][y] = p[x-1][y] + pf[x][y]
    for x in range(n):
        for y in range(m):
            if x+k-1 < n and y+k-1 < m:
                tmp = p[x+k-1][y+k-1]
                if x > 0:
                    tmp -= p[x-1][y+k-1]
                if y > 0:
                    tmp -= p[x+k-1][y-1]
                if x > 0 and y > 0:
                    tmp += p[x-1][y-1]
                if res > tmp:
                    res = tmp
print(res)