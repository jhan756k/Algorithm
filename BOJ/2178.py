from collections import deque
n, m = map(int, input().split())
bd = [list(map(int, input())) for _ in range(n)]
dQ = deque()
dis = [[0]*m for _ in range(n)]
bd[0][0] = 0
dQ.append((0,0))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while dQ:
    now = dQ.popleft()
    
    for a in range(4):
        x = now[0] + dx[a]
        y = now[1] + dy[a]

        if 0<=x<=(n-1) and 0<=y<=(m-1):
            if bd[x][y] == 1:
                dis[x][y] = dis[now[0]][now[1]] + 1
                dQ.append((x,y))
                bd[x][y] = 0
                if x == n-1 and y == m-1:
                    b = True
                    print(dis[x][y]+1)
                    exit()
