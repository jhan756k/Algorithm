import sys
n, m = map(int, sys.stdin.readline().split())
ls = list(map(int, sys.stdin.readline().split()))
ls.sort()
vis = [False]*n
ans = []
def find(l, d):
    global ls
    if d == m:
        tmp = ' '.join(map(str, l))
        if tmp not in ans:
            ans.append(tmp)
        return
    else:
        for x in range(n):
            if not vis[x]:
                vis[x] = True
                find(l+[ls[x]], d+1)
                vis[x] = False
find([], 0)

for a in ans:
    print(a)