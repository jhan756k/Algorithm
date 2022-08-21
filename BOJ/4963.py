from collections import deque
import sys
input = sys.stdin.readline
dQ = deque()

while True:
    w, h = map(int, input().split())
    if w ==0 and h == 0:
        break
    board = [list(map(int, input().split())) for _ in range(h)]
    dx = [1, 0, -1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, 1, -1, 1, -1]
    res = 0

    for x in range(h):
        for y in range(w):
            if board[x][y] == 1:
                dQ.append((x, y))
                board[x][y] = 0

                while dQ:
                    now = dQ.popleft()
                    
                    for i in range(8):
                        tmpx = now[0] + dx[i]
                        tmpy = now[1] + dy[i] 
                        if 0<=tmpx<h and 0<=tmpy<w and board[tmpx][tmpy] == 1:
                            dQ.append((tmpx, tmpy))
                            board[tmpx][tmpy] = 0

                res += 1

    print(res)


