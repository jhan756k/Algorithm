from collections import deque
n, m = map(int, input().split())
board = []
dQ = deque()
res = -1
for _ in range(n): board.append([int(x) for x in str(input())])
visited = [[False]*m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for x in range(n):
    for y in range(m):
        if board[x][y] == 1:
            board[x][y] = 0

            board[x][y] = 1

print(res)