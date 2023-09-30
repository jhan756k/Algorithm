board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for x in range(7):
    for y in range(3):
        tmpx = board[x][y:y+5]
        if tmpx == tmpx[::-1]:
            cnt += 1

        tmpy = [a[x] for a in board][y:y+5]
        if tmpy == tmpy[::-1]:
            cnt += 1

print(cnt)