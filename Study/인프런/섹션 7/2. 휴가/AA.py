n = int(input())
nlist = [tuple(map(int, input().split())) for _ in range(n)]
maxn = 0

def DFS(day, money):
    global maxn

    if day == n+1:
        if money > maxn:
            maxn = money

    else:
        if day + nlist[day-1][0] <= n+1:
            DFS(day + nlist[day-1][0], money + nlist[day-1][1])
        DFS(day+1, money)

DFS(1, 0)
print(maxn)