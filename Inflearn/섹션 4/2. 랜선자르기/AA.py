k, n = map(int, input().split())
nlist = [int(input()) for _ in range(k)]
nlist.sort()

start = 1
end = max(nlist)
res = 0

while start <= end:
    cnt = 0
    mid = (start + end)//2

    for x in range(k):
        cnt += (nlist[x])//mid  

    if cnt < n: 
        end = mid-1

    elif cnt >= n:
        res = mid
        start = mid + 1

print(res)
                