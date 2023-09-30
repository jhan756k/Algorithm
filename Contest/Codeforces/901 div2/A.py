import sys
t = int(sys.stdin.readline())
for _ in range(t):
    a, b, n = map(int, sys.stdin.readline().split())
    nlist = list(map(int, sys.stdin.readline().split()))
    nlist.sort()
    cnt = b
    while nlist:
        tmp = nlist.pop(0)
        if tmp + 1 <= a:
            cnt += tmp
        else:
            cnt += a-1
    print(cnt)