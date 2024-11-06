import sys
n, m = map(int, sys.stdin.readline().split())
xans, xans1, yans, yans1 = 0, 0, 0, 0
points = []
for _ in range(m):
  x, y = map(int, sys.stdin.readline().split())
  points.append((x, y))
points.sort(key=lambda x:x[0])
ax = points[m//2][0]
for p in points:
  xans += abs(p[0]- ax)
  xans1 += abs(p[0]- ax+1)
points.sort(key=lambda x:x[1])
ay = points[m//2][1]
for p in points:
  yans += abs(p[1]- ay)
  yans1 += abs(p[1]- ay+1)
ans = min(xans, xans1) + min(yans, yans1)
print(ans)
'''
7 11
6 7
4 7
1 7
5 3
6 2
7 1
6 1
5 4
3 6
1 6
6 6
output: 38
correct answer: 39
'''