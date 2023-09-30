for x in range(5):
    n, p = map(int, input().split())
    nlist = [int(x) for x in str(n)]
    
    p_index = len(nlist) - p

    for x in range(len(nlist)):
        if x < p_index:
            add_num = str(nlist[x] + nlist[p_index])
            nlist[x] = int(add_num[-1])
            
        if x > p_index:
            add_num = abs(nlist[x] - nlist[p_index])
            nlist[x] = add_num

    print(int("".join(list(map(str, nlist)))))
