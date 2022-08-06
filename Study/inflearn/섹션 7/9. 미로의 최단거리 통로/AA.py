from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
bd = [list(map(int, input().split())) for _ in range(7)]
dis = [[0]*7 for _ in range(7)]
dQ = deque()
dQ.append((0,0))
bd[0][0] = 1
b = False

while dQ:
    now = dQ.popleft()
    for i in range(4):
        x = now[0] + dx[i]
        y = now[1] + dy[i]
        if 0<=x<=6 and 0<=y<=6 and bd[x][y] == 0:
            dQ.append((x,y))
            bd[x][y] = 1
            dis[x][y]=dis[now[0]][now[1]] + 1
            if x==6 and y ==6:
                b = True
                break
    if b:
        break
    
if dis[6][6] == 0:
    print(-1)

else:
    print(dis[6][6])
