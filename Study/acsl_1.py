def transform():
    n, p = map(int, input().split())

    nlist = []

    for x in str(n):
        nlist.append(int(x))

    p_index = len(nlist) - p

    for x in range(len(nlist)):
        if x < p_index:
            add_num = str(nlist[x] + nlist[p_index])
            nlist[x] = int(add_num[-1])
            
        if x > p_index:
            add_num = abs(nlist[x] - nlist[p_index])
            nlist[x] = add_num

    ans = ""

    for x in nlist:
        ans += str(x)

    print(int(ans))

for x in range(5):
    transform()

