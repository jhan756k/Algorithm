import heapq
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

n, m = map(int, input().split())
start = int(input())
distance = [INF]*(n+1)

graph = [[] for i in range(n+1)]

for _ in range(m): # 그래프의 i 번째 행에는 (b,c): b까지 가는 거리 c 형식으로 저장됨
  a,b,c = map(int, input().split())
  graph[a].append((b,c))

# 다익스트라 알고리즘 (힙 자료구조 이용) --> O(nlogn) {힙 구조가 최댓값 구하는데 O(logn)}
# 만약 아래 코드처럼 방문체크 배열 써서 선형탐색을 하면 O(n^2)

'''
def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index
'''

def dijkstra(start):
  q=[]
  heapq.heappush(q, (0,start)) # 시작점 초기화
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist: # 이미 처리된 노드는 무시
      continue

    for i in graph[now]: # i = now 노드에서 갈수 있는 (노드번호, 거리)
      cost = dist + i[1] # cost 는 start 에서 now 까지 거리 (dist) + now 에서 i 까지의 거리

      if cost < distance[i[0]]: # 만약 cost가 현재 i까지의 최단거리보다 작으면 최단거리 대입
        distance[i[0]] = cost
        heapq.heappush(q, (cost,i[0])) # heap에 start 에서 i 까지 가는 거리 와 i의 노드번호 추가
                        # (i까지 거리, i의 노드번호)  

dijkstra(start) # 실행

# 출력
for i in range(1, n+1):
  # 도달할 수 없는 경우 (INF 가 그대로 남아있는 경우)
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])
