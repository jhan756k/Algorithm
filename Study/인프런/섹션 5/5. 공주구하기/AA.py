from collections import deque 

n, k = map(int, input().split())
dq = deque(list(range(1, n+1)))

while dq:
    for x in range(k-1):
        dq.append(dq.popleft())

    dq.popleft()

    if len(dq) == 1:
        print(dq[0])
        break
