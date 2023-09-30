n = int(input())
nlist = [int(input()) for _ in range(n)]
minn = 2147000000

def DFS(ind, asum, bsum, csum):
    global minn
    if ind == n:
        if asum!=bsum and asum != csum and bsum != csum:
            tmp = max(asum, bsum, csum) - min(asum, bsum, csum)
            if tmp < minn:
                minn = tmp
    else:
        DFS(ind+1, asum+nlist[ind], bsum, csum)
        DFS(ind+1, asum, bsum+nlist[ind], csum)
        DFS(ind+1, asum, bsum, csum+nlist[ind])

DFS(0, 0, 0, 0)
print(minn)
