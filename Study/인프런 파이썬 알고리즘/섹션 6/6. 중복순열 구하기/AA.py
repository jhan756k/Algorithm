n, m = map(int, input().split())
cnt = 0
res = [0]*m

def DFS(ind):
    global cnt
    if ind == m:
        cnt+=1
        for x in res:
            print(x, end = " ")
        print()
    else:
        for i in range(1, n+1):
            res[ind] = i
            DFS(ind+1)

DFS(0)
print(cnt)