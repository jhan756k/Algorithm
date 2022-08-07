n = int(input())
maxn = 0

def calculate_prize(dlist):
    
    if dlist[0] == dlist[1] == dlist[2]:
        return 10000 + (dlist[0] * 1000)

    elif dlist[0] != dlist[1] != dlist[2]:
        return 1000 + max(dlist)*100

    else:
        return max(dlist, key = dlist.count) * 100

for x in range(n):
    nlist = list(map(int, input().split()))
    if calculate_prize(nlist) > maxn:
        maxn = calculate_prize(nlist)

print(maxn)