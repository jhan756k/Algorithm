n, m = map(int, input().split())
res = [0]*m
ch = [0]*(n+1)
cnt = 0

def DFS(ind):
    global cnt
    if ind == m:
        for x in res:
            print(x, end=" ")
        cnt+=1
        print()

    else:
        for x in range(1, n+1):
            if ch[x] == 0:
                ch[x] = 1
                res[ind] = x
                DFS(ind+1)  
                ch[x] = 0

DFS(0)
print(cnt)