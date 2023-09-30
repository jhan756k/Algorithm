board = [list(map(int, input().split())) for _ in range(9)]
done = "YES"

for x in range(9):
    if any(board[x].count(n) > 1 for n in board[x]):
        done = "NO"
        break

    elif any([ab[x] for ab in board].count(k) > 1 for k in range(1, 10)):
        done = "NO"
        break

for a in range(0,7,3): 
    for b in range(0,7,3): 
        if any([y for x in [c[b:b+3] for c in board[a:a+3]] for y in x].count(k) > 1 for k in range(1, 10)):
            done = "NO"
            break       

print(done)
