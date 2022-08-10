import sys, heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())
INF = int(1e9)
tot = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    dis = [INF]*(n+1)
    dis[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
 
        if dis[now] < dist:
            continue

        for i in graph[now]:
            cost = dist+i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            
    return dis

res = 0

for a in range(1, n+1):
    g = dijkstra(a)
    b = dijkstra(x)
    res = max(res, g[x] + b[a])

print(res)
