# 다익스트라 알고리즘은 간선 가중치가 최소인 노드를 뽑아 순서대로 갱신해서
# 음수 간선을 고려 못하고 계산 할 수 있음

# 하지만 벨만-포드 알고리즘은 모든 노드를 거쳐가는 경로를 한번씩 계산해서
# 음수 가중치가 있어도 상관이 없음. 

n, m = map(int, input().split())
edges = []
inf = 1e9

for _ in range(m): # 인접행렬/리스트가 아닌 간선 그대로 1차원 배열에 저장
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

def bellman_ford(start):
    dist = [inf] * (n + 1)
    dist[start] = 0 # start to start 거리 0 

    # 모든 간선을 n-1번 순회하면 음의 순환이 없다는 가정하에
    # 모든 노드까지의 최단 거리를 구할 수 있으니
    # 총 n번을 순회했을때 마지막 n번에 값이 바뀐다는 것은
    # 가중치가 음수인 간선들이 무한 루프를 돈다는 소리임. --> 음수 사이클

    for i in range(n): # 두 노드사이 최단거리중 지나는 최대 노드의 수는 (v-1)
        # n 번째 순회는 음수사이클 판별 위함
        for a, b, c in edges: 
            #  다익스트라처럼 모든 노드를 탐색하는 것이 아닌 모든 간선 탐색

            # 무한이 아니고, 현재 노드를 거쳐 가는 것이 더 비용이 적으면 갱신
            if dist[a] != inf and dist[b] > dist[a] + c:
                if i == n - 1:  # n번째에 갱신된 경우
                    dist[0] = False # 0번째 리스트에 음수사이클 여부 저장 
                    return dist
                dist[b] = dist[a] + c

    dist[0] = True # 음수사이클 아니라고 저장
    return dist

ans = bellman_ford(1)

if not ans[0]: # 음수 사이클 존재하면
    print(-1)
else:
    ans.pop(0) # 음수사이클 여부 출력 방지
    for x in ans:
        if x == inf: # 경로 존재 안하면
            print("INF")
        elif x != 0: # 시작점 출력 X
            print(x)
            