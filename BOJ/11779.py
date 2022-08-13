import heapq, sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
path = [-1]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

sp, ep = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis = [INF]*(n+1)
    dis[start] = 0 
    
    while q:
        dist, now = heapq.heappop(q)

        if dis[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))  
                path[i[0]] = now

    return dis[ep]

print(dijkstra(sp))
pathres = [ep]
tmp = ep

while path[tmp] != -1:
    pathres.append(path[tmp])
    tmp = path[tmp]

print(len(pathres))  
pathres.reverse()
print(*pathres)
