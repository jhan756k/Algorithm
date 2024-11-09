import sys, itertools
l, c = map(int, sys.stdin.readline().split())
clist = list(sys.stdin.readline().split())
clist.sort()

def check(code):
  vow, cons = 0, 0
  vlist = ["a", "e", "i", "o", "u"]
  for char in code:
    if char in vlist:
      vow+=1
    else:
      cons+=1
  if vow >= 1 and cons >= 2: 
    return True
  else:
    return False
  
for comb in itertools.combinations(clist, l):
  if check(comb):
    print("".join(comb))