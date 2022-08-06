n = int(input())
nlist = [tuple(map(int, input().split())) for _ in range(n)]
nlist.sort(key = lambda x: (x[0], x[1]))
cnt = 0

for x in range(n):
    if any(nlist[x][1] < nlist[r][1] for r in range(x+1, n)):
        cnt +=1

print(n-cnt)