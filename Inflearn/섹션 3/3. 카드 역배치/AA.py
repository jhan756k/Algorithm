clist = list(range(1, 21))

for _ in range(10):
    ai, bi = map(int, input().split())

    if (bi-ai)%2 == 1:
        turn = (bi-ai)//2 + 1

    else:
        turn = (bi-ai)//2

    for y in range(turn):
        clist[ai-1+y], clist[bi-1-y] = clist[bi-1-y], clist[ai-1+y]

for x in clist:
    print(x, end=" ")