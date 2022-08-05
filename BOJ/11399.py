n = int(input())

nlist = list(map(int, input().split()))
nlist_sort = sorted(list(set(nlist)))

dic = {nlist_sort[i]: i for i in range(len(nlist_sort))}

for x in nlist:
    print(dic[x], end=' ')