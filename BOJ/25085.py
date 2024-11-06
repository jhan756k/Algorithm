import math
t = int(input())

for _ in range(t):
  ans = 0
  n = int(input())
  flist = []
  for i in range(1, int(math.sqrt(n))+1):
    if n%i==0:
      flist.append(i)
  alist = []
  for x in flist:
    if n//x != x:
      alist.append(n//x)
  flist += alist
  for x in flist:
    if str(x) == str(x)[::-1]:
      ans += 1
  print("Case #" + str(_+1) + ": " + str(ans))