import sys

n, m = map(int, sys.stdin.readline().split())
nlist = [sys.stdin.readline().strip() for i in range(n)]
mlist = [sys.stdin.readline().strip() for i in range(m)]

dup = list(set(nlist) & set(mlist))

print(len(dup))
for name in sorted(dup):
    print(name)