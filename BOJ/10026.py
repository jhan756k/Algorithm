from collections import deque
n = int(input())
board = [list(input()) for _ in range(n)]
sboard = [[0]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if board[x][y] == 'G':
            sboard[x][y] = 'R'
        else:
            sboard[x][y] = board[x][y]
dQ = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
use = [board, sboard]

for times in range(2):
    tmpboard = use[times]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if tmpboard[x][y] != 0:
                dQ.append((x,y))
                tmp = tmpboard[x][y]
                tmpboard[x][y] = 0
                while dQ:
                    now = dQ.popleft()
                    for i in range(4):
                        tx = now[0] + dx[i]
                        ty = now[1] + dy[i]
                        if 0<=tx<=n-1 and 0<=ty<=n-1 and tmpboard[tx][ty] == tmp:
                            dQ.append((tx,ty))
                            tmp = tmpboard[tx][ty]
                            tmpboard[tx][ty] = 0
                cnt += 1
    print(cnt)
    