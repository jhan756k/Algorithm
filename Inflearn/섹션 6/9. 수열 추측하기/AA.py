n, f = map(int, input().split())
res = [0]*n
ch = [0] * (n+1)
mlist = [1] * (n)

def DFS(ind):
    if ind == n:
        tmp = 0
        for a in range(n):
            tmp += (mlist[a] * res[a])
        if tmp == f:
            for b in res:
                print(b, end = " ")
            exit()

    else:
        for x in range(1, n+1):
            if ch[x] == 0:
                ch[x] = 1
                res[ind] = x
                DFS(ind+1)
                ch[x] = 0

for x in range(1, n):
    mlist[x] = mlist[x-1] * (n-x)//x
    
DFS(0)