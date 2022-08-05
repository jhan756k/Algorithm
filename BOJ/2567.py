board=[[0]*101 for _ in range(101)]
n = int(input())
for x in range(n):
    tx, ty = map(int, input().split())
    for a in range(tx, tx+10):
        for b in range(ty, ty+10):
            board[a][b]=1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

for x in range(100):
    for y in range(100):
        if board[x][y] == 1:
            for p in range(4):
                if board[x+dx[p]][y+dy[p]] == 0:
                    cnt+=1

print(cnt)


