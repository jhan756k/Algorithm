# 백준 11779번 최소비용 2 문제

# 기존 다익스트라에서 한줄만 추가
import heapq, sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
path = [-1]*(n+1) # 경로 배열 생성

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
                path[i[0]] = now # 기존 다익스트라와 이줄만 다름;
                # 만약 최소비용이 갱신된다면 경로저장배열의 현재 탐색되는 노드의 
                # 부모를 현재노드 (now) 로 갱신

    return dis[ep]

print(dijkstra(sp))

pathres = [ep] # 출력용 경로배열
tmp = ep # 끝점부터 역추적

while path[tmp] != -1: # 만약 path[tmp] 가 갱신이 된적이 있다면
    pathres.append(path[tmp]) # 경로출력배열에 path[tmp] 추가
    tmp = path[tmp] # tmp 를 그 path[tmp] 로 저장해서 호출 노드의 부모 계속 탐색

print(len(pathres))  
pathres.reverse() # 끝점부터 저장했으니 sort 아닌 reverse
print(*pathres) # 파이썬 list-unpacking 문법 (가변할당)
