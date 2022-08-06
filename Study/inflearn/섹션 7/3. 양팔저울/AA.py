k = int(input())
klist = list(map(int, input().split()))
s = sum(klist)
ch = [0]*s

def DFS(ind, tsum):
    if ind == k :
        if 1 <= tsum <= s:
            if ch[tsum-1] == 0:
                ch[tsum-1] = 1
    
    else:
        DFS(ind+1, tsum+klist[ind])
        DFS(ind+1, tsum-klist[ind])
        DFS(ind+1, tsum)

DFS(0, 0)
cnt = ch.count(0)
print(cnt)
