def DFS(ind, tsum):
    if tsum > tot//2:
        return

    if ind == n:
        if tsum == tot-tsum:
            print("YES")
            exit()
    else:
        DFS(ind+1, tsum + nlist[ind])
        DFS(ind+1, tsum)
        
n = int(input())
nlist = list(map(int, input().split()))
tot = sum(nlist)
DFS(0, 0)
print("NO")
