# 도시 최소 이동 문제
# 플로이드-워셜 알고리즘은 모든 노드에서 다른 노드까지 *나가는* 간선이
# 하나라도 있으면 모든 최소거리가 구해짐
# 하지만 하나의 노드라도 *나가는* 간선이 없으면 M 이 출력됨
# K값의 노드까지 가지 못하기 때문.

n, m=map(int, input().split())
dis=[[5000]*(n+1) for _ in range(n+1)] # 5000 -> INF

for i in range(1, n+1): # 자기자신까지의 경로비용 = 0 으로 초기화
    dis[i][i]=0 

for i in range(m): # 간선 입력 (노드간 직행), dp 초기화
    a, b, c=map(int, input().split())
    if dis[a][b]>c: # 전에 있었던 입력 덮어씌우기 방지
        dis[a][b]=c

# 플로이드-워셜 알고리즘 O(n^3)
for k in range(1, n+1):  # k: k번 노드 거쳐 가는 경로비용

    for i in range(1, n+1): # 행
        for j in range(1, n+1): # 열 
            dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])
            # 이미 있는 값보다 k 번 노드 지나가는 경로비용이 작으면 대입

for i in range(1, n+1): # 출력
    for j in range(1, n+1):
        if dis[i][j]==5000:
            print("M", end=' ')
        else:
            print(dis[i][j], end=' ')
    print()
