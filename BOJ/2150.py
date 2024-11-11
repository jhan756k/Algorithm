import sys
sys.setrecursionlimit(100000)
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
reverse = [[] for _ in range(v+1)]
vis = [0] * (v+1)
sccstack = []
scc = []

for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  reverse[b].append(a)

def dfs(n):
  vis[n] = 1
  for p in graph[n]:
    if vis[p] == 0:
      dfs(p)
  
  return sccstack.append(n)

for i in range(1, v+1):
  if vis[i] == 0:
    dfs(i)

vis = [0] * (v+1)

def revdfs(n):
  global scc, sl
  vis[n] = 1
  sl.append(n)
  for p in reverse[n]:
    if vis[p] == 0:
      revdfs(p)
  
  return

for i in range(v-1, -1, -1):
  if vis[sccstack[i]] == 0:
    sl = []
    revdfs(sccstack[i])
    scc.append(sorted(sl))

print(len(scc))

scc.sort(key=lambda x:x[0])
for i in scc:
  print(*i, -1)

'''
9 10
1 2
2 3
3 4
4 1
5 1
5 6
6 7
7 8
8 9
9 6

'''