n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
res = 0
start = end = n//2

for x in range(n):
    for y in range(start, end+1):
        res += nlist[x][y]

    if x >= n//2:
        start +=1
        end -=1
        
    else:
        start -=1
        end += 1

print(res)
