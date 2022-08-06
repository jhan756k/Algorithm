n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
nlist.insert(0, [0]*n)
nlist.append([0]*n)

for x in nlist:
    x.insert(0, 0)
    x.append(0)

res = 0

for x in range(1, n+1):
    for y in range(1, n+1): 
        if all(nlist[x][y] > nlist[x+dx[k]][y+dy[k]] for k in range(4)):
            res +=1

print(res)
