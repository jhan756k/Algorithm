import heapq, sys
input = sys.stdin.readline
n = int(input())
q = []
for x in range(n):
    tmp = int(input())
    if tmp != 0:
        heapq.heappush(q, tmp)
    
    else:
        if not q:
            print(0)

        else:
            print(heapq.heappop(q))

