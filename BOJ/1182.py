def DFS(ind, nsum):
    global cnt

    if ind == n:
        if nsum == s:
            cnt+=1

    else:
        DFS(ind+1, nsum+nlist[ind])
        DFS(ind+1, nsum)
        

n, s = map(int, input().split())
nlist = list(map(int, input().split()))
cnt = 0
DFS(0, 0)

if s == 0:
    print(cnt-1)
else:
    print(cnt)