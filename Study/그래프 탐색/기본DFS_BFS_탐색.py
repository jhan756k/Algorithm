# 백준 1260

from collections import deque
n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
vis = [0]*(n+1)
dQ = deque()

# 그래프 저장
for _ in range(m):
    ix, iy = map(int, input().split())
    graph[ix][iy]=1
    graph[iy][ix]=1

# 매번 새로운 노드 DFS 호출 될 때마다 
def DFS(v):
    vis[v]=1 # 방문 체크
    print(v, end = " ") # 후 출력
    for i in range(n+1):
        if vis[i]==0 and graph[v][i] == 1: # 방문했었는지, 그리고 간선이 존재하는지 확인
            # 충족하면 그 노드 재귀 호출
            DFS(i)
DFS(v)

# BFS 데크에 출발 노드 append
dQ.append(v)
vis = [0]*(n+1)
print()
print(v, end = " ")
vis[v] = 1

while dQ:
    now = dQ.popleft()
    # 데크 맨앞을 pop 하고 now 에 저장
    for i in range(n+1):
        if vis[i] == 0 and graph[now][i] == 1:
            # DFS 와 같은 조건 충족하면 재귀 호출 대신 
            # 데크에 해당 노드 append 하고 방문 체크
            dQ.append(i)
            vis[i] = 1
            print(i, end = " ")
