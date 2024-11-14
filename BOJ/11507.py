c = str(input().rstrip())
clist = [[1 for _ in range(13)] for _ in range(4)]
mat = {"P":0, "K":1, "H":2, "T":3}
card = ""

for i in range(0, len(c), 3):
  tmp = c[i:i+3]
  if clist[mat[tmp[0]]][int(tmp[1:])-1] == 0:
    print("GRESKA")
    exit()
  clist[mat[tmp[0]]][int(tmp[1:])-1] -= 1

ans = [sum(x) for x in clist]
print(*ans)