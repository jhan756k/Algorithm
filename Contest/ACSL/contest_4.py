n = int(input())
target = list(str(input()).split())
right, bottom = str(input()).split()
right = list(right)
bottom = list(bottom)
for i in range(n):
    right[i] = int(right[i])
    bottom[i] = int(bottom[i])
arrow = list(str(input()).split())
board = [[0 for i in range(n)] for j in range(n)]

for i in range(len(target)):
    board[int(target[i][0])][int(target[i][1])] = 1

def find_target(x, y, d):
    if d == "A":
        for i in range(y):
            if board[x][i] == 1:
                board[x][i] = 0
                return True
        return False

    elif d == "B":
        for i in range(x):
            if board[i][y] == 1:
                board[i][y] = 0
                return True
        return False

    elif d == "C":
        for i in range(y+1, n):
            if board[x][i] == 1:
                board[x][i] = 0
                return True
        return False

    elif d == "D":
        for i in range(x+1, n):
            if board[i][y] == 1:
                board[i][y] = 0
                return True
        return False
    
    elif d == "E":
        i = x-1
        j = y-1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                board[i][j] = 0
                return True
            i -= 1
            j -= 1
        return False

    elif d == "F":
        i = x-1
        j = y+1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                board[i][j] = 0
                return True
            i -= 1
            j += 1
        return False
    
    elif d == "G":
        i = x+1
        j = y+1
        while i < n and j < n:
            if board[i][j] == 1:
                board[i][j] = 0
                return True
            i += 1
            j += 1
        return False
    
    elif d == "H":
        i = x+1
        j = y-1
        while i < n and j >= 0:
            if board[i][j] == 1:
                board[i][j] = 0
                return True
            i += 1
            j -= 1
        return False

for i in range(len(arrow)):
    xp = int(arrow[i][0])
    yp = int(arrow[i][1])
    d = str(arrow[i][2])
    board[xp][yp] = "*"
    if (find_target(xp, yp, d)):
        right[xp] -= 1
        bottom[yp] -= 1
        board[xp][yp] = 0

for i in range(n):
    if right[i]==1:
        ansx = i
    if bottom[i]==1:
        ansy = i

dirlist = "ABCDEFGH"

for i in dirlist:
    if find_target(ansx, ansy, i):
        print(str(ansx) + str(ansy) + i)
        break