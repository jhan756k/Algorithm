n = int(input())
m = int(input())
dis=[[100001]*(n+1) for _ in range(n+1)]

for i in range(1, n+1): # 딱히 필요 없음; 출력때 알아서 INF는 0 출력해줌
    dis[i][i]=0

for i in range(m):
    a, b, c=map(int, input().split())
    if dis[a][b]>c:
        dis[a][b]=c

for k in range(1, n+1): 

    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dis[i][j]==5000:
            print(0, end=' ')
        else:
            print(dis[i][j], end=' ')
    print()
