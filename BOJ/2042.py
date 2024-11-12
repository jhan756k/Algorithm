import sys
sys.setrecursionlimit(10**9)
n, m, k = map(int, sys.stdin.readline().split())
seg = [0] * 4000050
l = [0] * 1000001

def update(ind, start, end, target, val):
  if target > end or target < start:
    return
  seg[ind] += val
  if start==end:
    return
  mid = (start+end)//2
  update(ind*2, start, mid, target, val)
  update(ind*2 + 1, mid+1, end, target, val)

def getsum(l, r, start, end, ind):
  if l > end or r < start:
    return 0
  if l <=start and r >= end:
    return seg[ind]
  mid = (start+end)//2
  return getsum(l, r, start, mid, ind*2) + getsum(l, r, mid+1, end, ind*2+1)

for i in range(n):
  tmp = int(sys.stdin.readline())
  l[i+1] = tmp
  update(1, 1, n, i+1, tmp)

for _ in range(m+k):
  a, b, c = map(int, sys.stdin.readline().split())
  if a == 1:
    t = c - l[b]
    update(1, 1, n, b, t)
    l[b] = c
  else:
    print(getsum(b, c, 1, n, 1))