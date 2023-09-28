n, m = map(int, input().split())

def find_arr(ls,t):
    if t == m:
        print(' '.join(map(str, ls)))
        return
    
    else:
        if t != 0:
            tmp = ls[-1]
        else:
            tmp = 1
        for x in range(tmp, n+1):
            find_arr(ls + [x], t+1)

find_arr([], 0)