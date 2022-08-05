from collections import deque
n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
vis = [0]*(n+1)
dQ = deque()

for _ in range(m):
    ix, iy = map(int, input().split())
    graph[ix][iy]=1
    graph[iy][ix]=1

def DFS(v):
    vis[v]=1
    print(v, end = " ")
    for i in range(n+1):
        if vis[i]==0 and graph[v][i] == 1:
            DFS(i)
DFS(v)
dQ.append(v)
vis = [0]*(n+1)
print()
print(v, end = " ")
vis[v] = 1
while dQ:
    now = dQ.popleft()
    for i in range(n+1):
        if vis[i] == 0 and graph[now][i] == 1:
            dQ.append(i)
            vis[i] = 1
            print(i, end = " ")


