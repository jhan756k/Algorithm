import heapq, sys
input = sys.stdin.readline
n = int(input())
q = []

for x in range(n):
    inp = int(input())
    if inp != 0:
        heapq.heappush(q, (abs(inp), inp))

    else:
        try:
            print(heapq.heappop(q)[1])
        except:
            print(0)
