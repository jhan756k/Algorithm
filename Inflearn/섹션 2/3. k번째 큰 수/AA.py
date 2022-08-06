n, k = map(int, input().split())
nlist = list(map(int, input().split()))
anslist = list()

for x in range(n):
    for y in range(x+1, n):
        for z in range(y+1, n):
            if (nlist[x] + nlist[y] + nlist[z]) not in anslist:
                anslist.append(nlist[x] + nlist[y] + nlist[z])

anslist.sort(reverse=True)
print(anslist[k-1])
