import sys
n = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
res = road[0]*price[0]
m = price[0]
dist = 0
for x in range(1, n-1):
    if price[x] < m:
        res += m*dist
        dist = road[x]
        m = price[x]
    else:
        dist += road[x]
    if x == n-2:
        res += m*dist
print(res)