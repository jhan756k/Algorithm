n, m = map(int, input().split())
seg = [[float('inf'), -1] for _ in range(400001)]

def init(ind, start, end, val):

  if start==end:
    seg[ind][0] = val
    seg[ind][1] = val
    return seg[ind]
  
  mid = (start+end)//2
  seg[ind][0] = min(init(ind*2, start, mid, val)[0], init(ind*2+1, mid+1, end, val)[0])
  seg[ind][1] = max(init(ind*2, start, mid, val)[1], init(ind*2+1, mid+1, end, val)[1])
  return seg[ind]

for i in range(n):
  tmp = int(input())
  init(1, 1, n, tmp)
print(seg[:100])


for _ in range(m):
  a, b = map(int, input().split())

