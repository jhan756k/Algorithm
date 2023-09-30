from collections import deque

n, m = map(int, input().split())
nlist = deque([(pos, val) for pos, val in enumerate(list(map(int, input().split())))])
cnt = 0

while True:
    tmp = nlist.popleft()

    if any(tmp[1]< x[1] for x in nlist):
        nlist.append(tmp)

    else: 
        cnt +=1
        if tmp[0] == m:
            print(cnt)
            break