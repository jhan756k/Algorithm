n, m = map(int, input().split())
flist = [list(map(int, input().split())) for _ in range(n)]
row = [0]*(n+1)
col = []*(m+1)
res = []
done = False
while not done:
    done = True
    for r in range(n):
        rtmp = set(flist[r])
        if len(rtmp) == 1+(0 in rtmp) and rtmp != {0}:
            res.append(("H", f"{r+1}", f"{max(rtmp)}"))
            flist[r] = [0]*(m)
            done = False

    for c in range(m):
        ctmp = set(list(map(lambda x:x[c], flist)))
        if len(ctmp) == 1+(0 in ctmp) and ctmp != {0}:
            res.append(("V", f"{c+1}", f"{max(ctmp)}"))
            for _ in range(n):
                flist[_][c] = 0
            done = False

print(len(res))
res.reverse()
for x in res:
    print(" ".join(x))    
