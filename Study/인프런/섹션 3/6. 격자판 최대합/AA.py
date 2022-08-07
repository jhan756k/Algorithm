n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
maxn = 0

for x in range(n):
    sum1, sum2 = 0, 0
    for y in range(n):
        sum1 += nlist[x][y]
        sum2 += nlist[y][x]

    if sum1 > maxn:
        maxn = sum1

    if sum2 > maxn:
        maxn = sum2

sum1, sum2 = 0, 0

for x in range(n):
    sum1 += nlist[x][x]
    sum2 += nlist[x][n-x-1]

if sum1 > maxn:
    maxn = sum1

if sum2 > maxn:
    maxn = sum2

print(maxn)