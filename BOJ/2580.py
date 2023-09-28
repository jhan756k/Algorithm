board = [list(map(int, input().split())) for _ in range(9)]
coord = []

def row(x, a):
    for i in range(9):
        if a == board[x][i]:
            return False
    return True

def col(y, a):
    for i in range(9):
        if a == board[i][y]:
            return False
    return True

def box(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == board[nx+i][ny+j]:
                return False
    return True

def find_board(num):
    if len(coord) == num:
        for i in range(9):
            print(*board[i])
        exit()
    a, b = coord[num][0], coord[num][1]
    for k in range(1, 10):
        if row(a, k) and col(b, k) and box(a, b, k):
            board[a][b] = k
            find_board(num+1)
            board[a][b] = 0


for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            coord.append((i, j))

find_board(0)