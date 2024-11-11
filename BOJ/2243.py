n = int(input())
size = 1000001
seg = [0] * (size*4)

def update(ind, target, val, start, end):
  if target < start or target > end: # 범위밖
    return
  seg[ind]+=val # 누적합
  if start == end: # 리프노드 도달하면 리턴
    return
  mid = (start + end)//2
  update(ind*2, target, val, start, mid)
  update(ind*2+1, target, val, mid+1, end)

def query(ind, target, start, end):
  if start == end: # 리프노드의 인덱스 (맛 수치) 리턴
    return start
  mid = (start + end)//2
  if target <= seg[ind*2]: # 좌/우 갈건지 판별
    return query(ind*2, target, start, mid)
  else:
    return query(ind*2+1, target-seg[ind*2], mid+1, end)

for _ in range(n):
  a = list(map(int, input().split()))
  if a[0] == 2:
    update(1, a[1], a[2], 1, size)
  else:
    ans = query(1, a[1], 1, size)
    print(ans)
    update(1, ans, -1, 1, size)