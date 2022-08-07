n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mincnt = 2147000000
nlist.sort(reverse=True)

def DFS(cnt, tsum):
    global mincnt

    if cnt >= mincnt:
        return
    if tsum > m:
        return
    
    if tsum == m:
        if cnt < mincnt:
            mincnt = cnt

    else:
        for x in range(n):
            DFS(cnt+1, tsum+nlist[x])

DFS(0, 0)
print(mincnt)