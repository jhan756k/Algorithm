# UNION-FIND 유니언 파인드 알고리즘

# Disjoint set --> 서로소 집합
# 1. Find() --> 노드가 어느 집합 포함되어있는지 찾는 함수
# 2. Union() --> 두 노드의 집합 합치는 함수

# 예시: 백준 1717 집합의 표현

n, m = map(int, input().split())
parents = [i for i in range(n+1)] # 1부터n까지 자기 자신에 대응하는 부모 생성

def find(a):
        if a == parents[a]: # 만약 자신이 부모와 같다면 최종부모노드임 --> 리턴
            return a
        else: # return find(parents[a]) 가능 but 메모이제이션 사용해서 시간단축
            parents[a] = find(parents[a]) # 최종 부모노드 업데이트 (메모이제이션)
            return parents[a]

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa == pb: # 만약 이미 부모 같으면 리턴
        return
    parents[pa] = pb # a의 부모를 b의 부모로 바꿈

for _ in range(m):
    q, a, b = map(int, input().split())

    if q == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

