import sys

ans={}
while True:
  x = list(map(str, sys.stdin.readline().split()))
  if not x:
    break
  x.pop(0)
  a = "".join(x)
  if a not in ans:
    ans[a] = 1
print(len(ans))