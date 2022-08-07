nlist = [list(map(int, input().split())) for _ in range(10)]
for x in range(10):
    if nlist[9][x]==2:
        sx = 9
        sy = x
        break

def DFS(x, y):
    if x == 0:
        print(y)

    else:
        if 0<=y-1 and nlist[x][y-1] == 1:
            nlist[x][y-1] = 0
            DFS(x, y-1)
        elif y+1<=9 and nlist[x][y+1] == 1:
            nlist[x][y+1] = 0
            DFS(x, y+1) 
        else:
            nlist[x-1][y] = 0
            DFS(x-1, y)

DFS(sx, sy)