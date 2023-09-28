from collections import deque
n, m = map(int, input().split())
board = []
dQ = deque()
res = -1
for _ in range(n): board.append([int(x) for x in str(input())])
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for x in range(n):
    for y in range(m):
        if board[x][y] == 1:
            board[x][y] = 0

            dQ.append((0, 0))
            pathlength = [[0]*m for _ in range(n)]
            pathlength[0][0] = 1
            while dQ:
                a, b = dQ.popleft()
                if a == n-1 and b == m-1:
                    break

                for i in range(4):
                    tmpx = a + dx[i]
                    tmpy = b + dy[i]
                    if 0 <= tmpx < n and 0 <= tmpy < m and board[tmpx][tmpy] == 0 and pathlength[tmpx][tmpy] == 0:
                        dQ.append((tmpx, tmpy))
                        pathlength[tmpx][tmpy] = pathlength[a][b] + 1
            board[x][y] = 1
            if pathlength[n-1][m-1] == 0:
                continue
            res = min(res, pathlength[n-1][m-1]) if res != -1 else pathlength[n-1][m-1]

print(res)