import heapq as hq
a = []

while True:
    n = int(input())

    if n == -1:
        break

    if n == 0:      
        if a:
            print(hq.heappop(a))
        else:
            print(-1)

    else:
        hq.heappush(a, n)
        