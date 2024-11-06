n = int(input())
e = int(input())
ans = set([x for x in range(1, n+1)])
for _ in range(e):
  ppl = list(map(int, input().split()))
  ppl.pop(0)
  ppls = set(ppl)
  if 1 not in ppls:
    if ppls & ans:  
      ans |= ppls
      print(ans)
  else:
    ans &= ppls
    print(ans)
for x in sorted(ans):
  print(x)