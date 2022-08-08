import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
# 핵심: 굳이 graph 0 으로 채울 필요 없이 간선있는 것만 필요하기 때문에
# 간선 append 만 해도 됨.
graph = [[]*(n+1) for _ in range(n+1)]
vis = [False]*(n+1)
cnt = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def DFS(v):
    vis[v] = True 
    for i in graph[v]:
        # 호출된 v와 연결된 노드 중 방문하지 않은 노드 존재하면 호출
        if not vis[i]:
            DFS(i)

for i in range(1, n+1): # 모든 노드 돌면서 방문 기록 없으면 간선 여부 따라 실행
    if not vis[i]:
        if not graph[i]:
            cnt+=1
            vis[i] = True
        else:
            DFS(i)
            cnt+=1

print(cnt)
