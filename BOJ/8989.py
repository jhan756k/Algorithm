import sys
t = int(sys.stdin.readline())

def calc_angle(tlist):
  ans = []
  for t in tlist:
    t1 = t[1]
    if t1 > 12:
      t1 -= 12
    hm = t[2]*6
    ha = t1*30 + t[2]*0.5
    ang = abs(ha - hm)
    if ang > 180:
      ang = 360 - ang
    ans.append((ang, t[0], t[1], t[2]))
  return sorted(ans, key=lambda x:(x[0], x[2], x[3]))

for _ in range(t):
  tlist = list(map((lambda x:[str(x), int(x[:2]), int(x[3:]), 0]), sys.stdin.readline().split()))
  print(calc_angle(tlist)[2][1])