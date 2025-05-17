n = int(input())
mlist = []

for _ in range(n):
  a, b = map(int, input().split())
  mlist.append((a, b))

mlist.sort(key=lambda x:(-x[0], x[1]))
print(*mlist[0], *mlist[1])
mlist.sort(key=lambda x:(x[1], -x[0]))
print(*mlist[0], *mlist[1])