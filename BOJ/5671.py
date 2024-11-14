import sys

def check(n):
  l = [0] * 11
  for i in str(n):
    if l[int(i)] != 0:
      return False
    else:
      l[int(i)] += 1
  return True

while True:
  try:
    a, b = map(int, sys.stdin.readline().split())
    cnt = 0
    
    for i in range(a, b+1):
      if check(i):
        cnt+=1
    print(cnt)
  except:
    break