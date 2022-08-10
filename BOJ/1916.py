import heapq, sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for x in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

sp, ep = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    dis = [INF]*(n+1)
    dis[start] = 0
    while q:
        ndist, node = heapq.heappop(q)

        if dis[node] < ndist:
            continue

        for i in graph[node]:
            cost = ndist + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return dis       

print(dijkstra(sp)[ep])
