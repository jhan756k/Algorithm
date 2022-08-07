n, m = map(int, input().split())
nlist =[tuple(map(int, input().split())) for _ in range(n)]
maxn = 0

def DFS(ind, tsum, ssum):
    global maxn
    if tsum > m:
        return

    if ind == n:
        if ssum > maxn:
            maxn = ssum

    else:
        DFS(ind+1, tsum + nlist[ind][1], ssum+nlist[ind][0])
        DFS(ind+1, tsum, ssum)

DFS(0, 0, 0)
print(maxn)
