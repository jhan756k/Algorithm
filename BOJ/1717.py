import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
parents = [i for i in range(n+1)]

def find(a):
        if a == parents[a]:
            return a
        else:
            parents[a] = find(parents[a])
            return parents[a]

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa == pb:
        return
    parents[pa] = pb

for _ in range(m):
    q, a, b = map(int, input().split())

    if q == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
