import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
  p, c, w = map(int, sys.stdin.readline().split())
  tree[p].append((c, w))
  tree[c].append((p, w))

mv, mn = -1, 1
visited = []

def dfs(node, dist):
  global mv, mn, visited
  if node > n: # 노드 초과
    return
  
  visited.append(node)
  
  for x in tree[node]: # 리프노드 일시
    if x[0] not in visited:
      break
  else:
    if dist > mv:
      mv = dist
      mn = node
    return
  
  for child in tree[node]:
    if child[0] not in visited:
      dfs(child[0], dist+child[1])
      visited.remove(child[0])

dfs(1, 0)
un = mn
mv, mn = -1, 1
visited = []
dfs(un, 0)
print(mv)