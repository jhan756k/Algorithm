import sys
sys.setrecursionlimit(10**9)
n, m, k = map(int, sys.stdin.readline().split())
seg = [1] * (1048577 * 2 + 40)
ll = [0] * 1000001


def init(ind, l, r):
  if l == r:
    seg[ind] = ll[l]
    return seg[ind]
  mid = (l+r)//2
  seg[ind] = init(ind*2, l, mid)*init(ind*2+1, mid+1, r)%1000000007
  return seg[ind]

def getmult(l, r, start, end, ind):
  if l > end or r < start:
    return 1
  if l <=start and r >= end:
    return seg[ind]
  mid = (start+end)//2
  return (getmult(l, r, start, mid, ind*2) * getmult(l, r, mid+1, end, ind*2+1))%1000000007

def update(ind, start, end, target, val):
  if start==end==target:
    seg[ind] = val
    return seg[ind]
  
  if target < start or target > end:
    return seg[ind]

  mid = (start+end)//2
  seg[ind] = (update(ind*2, start, mid, target, val)*update(ind*2 + 1, mid+1, end, target, val))%1000000007
  return seg[ind]

for i in range(n):
  tmp = int(sys.stdin.readline())
  ll[i+1] = tmp

init(1, 1, n)

for _ in range(m+k):
  a, b, c = map(int, sys.stdin.readline().split())
  if a == 1:
    update(1, 1, n, b, c)
  else:
    print(getmult(b, c, 1, n, 1))