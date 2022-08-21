import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[]for _ in range(n+1)]
parent = [0]*(n+1)

for x in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def DFS(start):
    global tree, parent
    for i in tree[start]:
        if parent[i] == 0:
            parent[i] = start
            DFS(i)

DFS(1)

for x in range(2, n+1):
    print(parent[x])

