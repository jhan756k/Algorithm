import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
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
        if not vis[i]:
            DFS(i)

for i in range(1, n+1):
    if not vis[i]:
        if not graph[i]:
            cnt+=1
            vis[i] = True
        else:
            DFS(i)
            cnt+=1

print(cnt)
