import sys
sys.setrecursionlimit(10**6)
n = int(input())
nn = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
cnt = 0
vis = [0]*(n+1)

for _ in range(nn):
    tmpx, tmpy = map(int, input().split())
    graph[tmpx][tmpy] = 1
    graph[tmpy][tmpx] = 1

def DFS(v):
    global cnt
    vis[v] = 1
    for x in range(1, n+1):
        if graph[v][x] == 1 and vis[x] == 0:
            DFS(x)
            cnt+=1

DFS(1)
print(cnt)
