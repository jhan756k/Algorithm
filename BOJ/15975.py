import sys
n = int(sys.stdin.readline())
p = []
ans = 0
for _ in range(n):
  p.append(tuple(map(int, sys.stdin.readline().split())))

p.sort(key=lambda x:(x[1], x[0]))
for x in range(1, n-1):
  sl = float('inf')
  if p[x][1] == p[x-1][1]:
    sl = min(sl, p[x][0] - p[x-1][0])
  if p[x][1] == p[x+1][1]:
    sl = min(sl, p[x+1][0] - p[x][0])
  if sl == float('inf'):
    sl = 0
  ans+=sl
if p[1][1] == p[0][1]:
  ans += p[1][0] - p[0][0]
if p[n-1][1] == p[n-2][1]:
  ans += (p[n-1][0] - p[n-2][0])
print(ans)