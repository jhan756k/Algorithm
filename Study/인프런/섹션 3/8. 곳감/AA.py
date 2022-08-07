n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]

m = int(input())

for _ in range(m):
    row, dir, num = map(int, input().split())

    if dir == 0:
        for p in range(num):
            nlist[row-1].append(nlist[row-1].pop(0))

    if dir == 1:
        for q in range(num):
            nlist[row-1].insert(0, nlist[row-1].pop())

res = 0
start = 0
end = n

for x in range(n):

    res += sum(nlist[x][start:end])

    if x<(n//2):
        start +=1
        end -=1
    
    else:
        start -=1
        end +=1
            
print(res)