from collections import deque
n, k = map(int, input().split())
tim = [0] * (100100)

dQ = deque()
dQ.append(n)
tim[n] = 1

while dQ:
    now = dQ.popleft()
    if now == k:
        print(tim[k]-1)
        break
    
    
    for x in (now*2, now-1, now+1):
        if 0<=x<=100001:
            if x == now*2 and tim[x] == 0:
                tim[x] = tim[now]
                dQ.append(x)

            else:
                if tim[x] == 0:
                    tim[x] = tim[now] + 1
                    dQ.append(x)
