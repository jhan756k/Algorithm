n, c = map(int, input().split())
nlist = [int(input()) for _ in range(n)]
nlist.sort()

start = 1
end = nlist[-1]
res = 0

while start <= end:
    mid = (start+end)//2
    last = 0
    cnt = 1

    while True:
        for x in range(last, n):
            if nlist[x] - nlist[last] >= mid:
                last = x
                cnt += 1
                break
        else:
            break

    if cnt >= c:
        res = mid
        start = mid+1

    else:
        end = mid-1

print(res)

    

        


