import heapq, sys
input = sys.stdin.readline
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for x in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    distance = [INF]*(n+1)
    q=[]
    heapq.heappush(q, (0, start))
    distance[start]=0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
    
        for i in graph[now]:
            cost = dist+i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance

v1, v2 = map(int, input().split())

dv1 = dijkstra(v1)
dv2 = dijkstra(v2)
original = dijkstra(1)

path1 = original[v1] + dv1[v2] + dv2[n] 
path2 = original[v2] + dv2[v1] + dv1[n]
res = min(path1, path2)

if res < INF:
    print(res)

else:
    print(-1)
