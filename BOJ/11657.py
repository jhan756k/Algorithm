import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
inf = 1e9
dist = [inf] * (n + 1)
dist[1] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

def bellman_ford():

    for i in range(n): 
        for a, b, c in edges: 
            if dist[a] != inf and dist[b] > dist[a] + c:
                if i == n - 1:  
                    return False
                dist[b] = dist[a] + c

    return True

if not bellman_ford():
    print(-1)
else:
    for x in dist[2:]:
        print(x) if x!=inf else print(-1)
