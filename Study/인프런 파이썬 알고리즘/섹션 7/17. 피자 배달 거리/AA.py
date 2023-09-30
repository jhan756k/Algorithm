import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
house = []
pizza = []
res = 21470000000
for x in range(n):
    tmp = list(map(int, input().split()))
    for y in range(n):
        if tmp[y] == 1:
            house.append((x, y))
        elif tmp[y] == 2:
            pizza.append((x, y))

def calc_dis(plist):
    global res
    tmpn = 0
    for h in range(len(house)):
        tmpnn = 2147000000
        hx, hy = house[h]
        for p in range(m):
            px, py = plist[p]
            tmpnn = min(tmpnn, abs(hx-px) + abs(hy-py))
        tmpn+=tmpnn
    res = min(res, tmpn)

vis = [0]*(len(pizza))

def DFS(ind, end, tmplist):
    if ind == m:
        calc_dis(tmplist)
    else:
        for a in range(end, len(pizza)):
            if vis[a] == 0:
                vis[a] = 1
                DFS(ind+1, a+1, tmplist+[pizza[a]])
                vis[a] = 0
        
DFS(0, 0, [])
print(res)
