import sys
n, c = map(int, sys.stdin.readline().split())
h = [int(sys.stdin.readline()) for _ in range(n)]
h.sort()
start = 0
end = max(h)+1
res = 0
while start <= end:
    mid = (start + end) // 2
    d = 0
    cnt = 1
    for x in range(n):
        if h[x]-h[d] >= mid:
            d = x
            cnt+=1
    if cnt >= c:
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res)