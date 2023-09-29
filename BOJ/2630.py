import sys
n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
b, w = 0, 0
def div(x, y, n):
    global b, w
    hb = [row[y:y+n] for row in board[x:x+n]]
    s = sum([sum(a) for a in hb])
    if s == n**2 or s == 0:
        if board[x][y] == 1:
            b+=1
        else:
            w+=1
    else:
        div(x, y, n//2)
        div(x, y+n//2, n//2)
        div(x+n//2, y, n//2)
        div(x+n//2, y+n//2, n//2)
        return
div(0, 0, n)
print(w)
print(b)