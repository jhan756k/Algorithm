c, n = map(int, input().split())
nlist = [int(input()) for _ in range(n)]
tot = sum(nlist)
maxn = 0

def DFS(ind, sumw, tsum):
    global maxn

    if sumw > c:
        return

    if (tot-tsum)+sumw <maxn:
        return

    if ind == n:
        if maxn < sumw:
            maxn = sumw

    else:
        DFS(ind+1, sumw + nlist[ind], tsum+nlist[ind])
        DFS(ind+1, sumw, tsum+nlist[ind])  

DFS(0, 0, 0)
print(maxn)
