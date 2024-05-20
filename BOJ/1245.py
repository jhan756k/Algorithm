import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def bfs(x, y):
  return

for x in range(n):
  for y in range(m):
    bfs(x, y)