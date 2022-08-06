n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
nlist.sort(key= lambda x: (x[1], x[0]))

cnt = 0
endtime = 0

for start, end in nlist:
    if start >= endtime:
        endtime = end
        cnt += 1    

print(cnt)
