n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
ch = [0]*(n+1)
for _ in range(m):
    s, e = map(int, input().split())
    graph[s][e] = 1

cnt = 0
ch[1] = 1
path = [1]

def DFS(v):
    global cnt
    if v == n:
        cnt +=1
        print(path)
    else:
        for i in range(1, n+1):
            if graph[v][i]==1 and ch[i]==0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i] = 0

DFS(1)
print(cnt)
