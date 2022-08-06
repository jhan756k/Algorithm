n, m = map(int, input().split())
graph = [[0]*(n) for _ in range(n)]

def print_graph():
    for x in graph:
        for y in x:
            print(y, end = " ")
        print()

for _ in range(m):
    s, e, d = map(int, input().split())
    graph[s-1][e-1] = d

print_graph()
