board = [list(map(int, input().split())) for _ in range(7)]
board[0][0] = 1
cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x==6 and y==6:
        cnt+=1

    else:
        for i in range(4):
            tx = x+dx[i]
            ty = y+dy[i]
            if 0<=tx<=6 and 0<=ty<=6 and board[tx][ty] == 0:
                board[tx][ty] = 1
                DFS(tx, ty)
                board[tx][ty] = 0

DFS(0,0)
print(cnt)
    