import sys
sys.setrecursionlimit(10**5)
n = int(sys.stdin.readline())
a = [0] * 1000001
x = list(map(int, sys.stdin.readline().split()))
h = list(map(int, sys.stdin.readline().split()))
seg = [0] * 500000 * 5
ans = 0

for i in range(n):
  a[x[i]] = i

for i in range(n):
  h[i] = a[h[i]] + 1

def update(ind, start, end, target, val):
  if target < start or target > end:
    return
  seg[ind]+=val
  if start==end:
    return
  mid = (start + end)//2
  update(ind*2, start, mid, target, val)
  update(ind*2+1, mid+1, end, target, val)

def getsum(l, r, start, end, ind):
  if l > end or r < start:
    return 0
  if l <= start and r >= end:
    return seg[ind]
  mid = (start + end)//2
  return getsum(l, r, start, mid, ind*2) + getsum(l, r, mid+1, end, ind*2+1)

for i in range(n):
  ans += getsum(h[i]+1, n, 1, n, 1)
  update(1, 1, n, h[i], 1)
print(ans)