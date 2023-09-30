n, k = map(int, input().split())
nlist = list(map(int, input().split()))
m = int(input())
cnt = 0

def DFS(ind, start, tsum):
    global cnt
    if ind == k:
        if tsum != 0 and tsum%m==0:
            cnt+=1

    else:
        for x in range(start, n):
            DFS(ind+1, x+1, tsum + nlist[x])

DFS(0, 0, 0)
print(cnt)