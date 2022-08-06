t = int(input())
k = int(input())
klist = [list(map(int, input().split())) for _ in range(k)]
cnt = 0

def DFS(ind, tsum):
    global cnt

    if tsum > t:
        return
            
    if ind == k:
        if tsum == t:
            cnt+=1
    else:
        for x in range(klist[ind][1]+1):
            DFS(ind+1, tsum+(klist[ind][0]*x))

DFS(0, 0)
print(cnt)
