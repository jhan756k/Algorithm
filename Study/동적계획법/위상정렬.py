# 일 선후관계 지켜서 하기 문제

# 위상정렬을 하기 위해서는 모든 노드의 진입 차수 (노드에 들어오는 간선의 개수) 를 기록하는 배열 필요
# for 문 돌리면서 진입차수가 0인 노드는 큐에 계속 append
# 큐에 append 된 노드는 하나씩 pop 하면서 해당 노드로 인해 생긴 다른 노드의 진입차수를 -1 함.
# 이를 통해 생긴 또다른 진입차수가 0인 노드를 큐에 넣음
# 이를 반복하면 배열의 모든 노드를 거쳐가며 진입차수를 0으로 만들고 최종적으로 일의 순서를 알 수 있음

from collections import deque
n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
degree = [0]*(n+1) # 진입차수 배열
dQ=deque()

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1 
    degree[b]+=1 # 진입차수 배열 초기화
    
for i in range(1, n+1):
    if degree[i]==0: # 처음 진입차수가 0인 노드 추가
        dQ.append(i)

while dQ:
    now = dQ.popleft()
    print(now, end = " ")
    for i in range(1, n+1):
        if graph[now][i]==1: # 현재 노드로 인해 진입차수 변하는 노드 탐색
            degree[i]-=1 # 그 노드의 진입차수 -1 하고
            if degree[i]==0: # 만약 그 노드의 진입차수가 0이 되어버리면 dQ에 append해서 다시 연산
                dQ.append(i)

# 입력예제
'''
6 6
1 4
5 4
4 3
2 5
2 3
6 2
'''

# 출력예제
'''
1 6 2 5 4 3
'''
