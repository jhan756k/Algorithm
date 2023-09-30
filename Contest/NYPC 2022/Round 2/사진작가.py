from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
dp = [0]*(n)
dp[0] = 1
used = deque()
used.append(nlist[0])
tmp = 1

for x in range(1, n):
    for a in range(tmp):
        if nlist[x] == used[a]:
            for de in range(a+1):
                used.popleft()
                tmp-=1
            break

    used.append(nlist[x])
    tmp+=1
    dp[x] = tmp

print(max(dp))
