import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split()))
pour = [1, 2, 4]

dQ = deque()
dQ.append([nlist, 0])

while dQ:
    tmp = dQ.popleft()
    p = tmp[0]
    p.sort()
    print(p)
    w = tmp[1]

    if len(set(p)) == 1:
        break        

    for x in range(n):
        if abs(p[0]-p[x]) < 4:
            p[x]+=pour[w%3]
            w+=1
            dQ.append([p, w])
            break

print(nlist)            





