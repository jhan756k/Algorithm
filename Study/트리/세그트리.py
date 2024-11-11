data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
segtree = [0] * 40

def init(start, end, ind):
  if start == end:
    segtree[ind] = data[start]
    return segtree[ind]
  
  mid = (start + end)//2
  segtree[ind] = init(start, mid, ind*2) + init(mid+1, end, ind*2+1) 
  return segtree[ind]

def intsum(start, end, ind, l, r):
  print(start, end, ind, l, r)
  if l > end or r < start:
    return 0
  if l <= start and r >= end:
    print("Sdd")
    return segtree[ind]

  mid = (start + end)//2
  return intsum(start, mid, ind*2, l, r) + intsum(mid+1, end, ind*2+1, l, r)

def update(start, end, ind, what, val):
  if what < start or what > end:
    return
  
  segtree[ind] += val
  if start == end:
    return
  
  mid = (start + end)//2
  update(start, mid, ind*2, what, val)
  update(mid+1, end, ind*2+1, what, val)

init(0, len(data) - 1, 1)
# print(intsum(0, len(data) - 1, 1, 0, 9))  # 0부터 9까지의 구간 합 (1 + 2 + ... + 9 + 10)
print(intsum(0, len(data) - 1, 1, 0, 2))  # 0부터 2까지의 구간 합 (1 + 2 + 3)
# print(intsum(0, len(data) - 1, 1, 6, 7)) 