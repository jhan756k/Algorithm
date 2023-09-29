import sys
t = int(sys.stdin.readline())
n = [int(sys.stdin.readline()) for _ in range(t)]
ml = max(n)+2
dpz, dpo = [0]*ml, [0]*ml
dpz[0], dpz[1], dpo[0], dpo[1] = 1, 0, 0, 1
for x in range(2, ml):
    dpz[x] = dpz[x-1] + dpz[x-2]
    dpo[x] = dpo[x-1] + dpo[x-2]
for a in n:
    print(dpz[a], dpo[a])