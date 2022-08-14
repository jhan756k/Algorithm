from collections import deque
a,b = map(int,input().split())
dQ = deque()
dQ.append((a,1))

while(dQ):
    n,t = dQ.popleft()
    if n > b:
        continue
    if n == b:
        print(t)
        break
    dQ.append((n*10+1,t+1))
    dQ.append((n*2,t+1))
else:
    print(-1)