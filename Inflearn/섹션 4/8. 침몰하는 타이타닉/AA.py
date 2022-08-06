n, m = map(int, input().split())
nlist = list(map(int, input().split()))
nlist.sort(reverse=True)
cnt = 0
ind = 1

while nlist:
    
    if len(nlist) == 1:
        cnt+=1
        break

    if nlist[0] + nlist[ind] <= m:
        cnt +=1
        nlist.pop(ind)
        nlist.pop(0)
        ind = 1

    else:
        if ind == len(nlist)-1:
            cnt +=1
            nlist.pop(0)
            ind = 1
        else:
            ind += 1

print(cnt)
