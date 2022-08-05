import sys
n, m = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))

def bt():
    s, e, res =0, max(nlist), 0
    
    while s <= e:
        mid = (s+e)//2
        cut_tree = 0
        for x in nlist:
            if x > mid:
                cut_tree += (x-mid)

        if cut_tree == m:
            res = mid
            break

        elif cut_tree > m:
            res = mid
            s = mid+1

        elif cut_tree < m:
            e = mid-1
    return res

print(bt())
