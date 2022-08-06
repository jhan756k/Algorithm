n, m = map(int, input().split())

nlist = []

for x in range(1, n+1):
    for y in range(1, m+1):
        nlist.append(x + y)

nlist.sort()
anslist = []
duplist = []
[duplist.append(x) for x in nlist if x not in duplist]
countlist = []

for x in duplist:
    tmpcount = 0

    for y in range(len(nlist)):
        if x == nlist[y]:
            tmpcount +=1
    
    countlist.append(tmpcount)

for x in range(len(countlist)):
    if countlist[x] == max(countlist):
        print(duplist[x], end=" ")

    
    
    