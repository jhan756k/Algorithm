import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
inf = 100000001
dis=[[inf]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dis[i][i]=0

for i in range(m):
    a, b, c = map(int, input().split())
    if dis[a][b]>c:
        dis[a][b]=c

for k in range(1, n+1): 

    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dis[i][j]==inf:
            print(0, end=' ')
        else:
            print(dis[i][j], end=' ')
    print()
