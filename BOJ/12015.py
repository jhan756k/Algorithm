import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
al = [(a[x], x) for x in range(n)]
al.sort()

for x in range(al):
    start = 0
