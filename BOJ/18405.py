n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
alist = []

for i in range(n):
  for j in range(n):
    if board[i][j] != 0:
      tmp = abs(x-1-i) + abs(y-1-j)
      if tmp <= s:
        alist.append((tmp, board[i][j]))

if not alist:
  print(0)
else:
  alist.sort(key=lambda x:(x[0], x[1]))
  print(alist[0][1])