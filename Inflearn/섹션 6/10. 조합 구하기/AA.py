n, m = map(int, input().split())
res = [0] * m
cnt = 0

def DFS(ind, s):
    global cnt

    if ind == m:
        for x in res:
            print(x, end = " ")
        cnt+=1
        print()

    else:
        for a in range(s, n+1):
            res[ind] = a
            DFS(ind+1, a+1) 

DFS(0, 1)
print(cnt)
