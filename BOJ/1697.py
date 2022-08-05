from collections import deque
n, k = map(int, input().split())
dQ = deque()
dis = [0]*100001
dQ.append(n)

while dQ:
    now = dQ.popleft()
    if now == k:
        print(dis[now])
        break
    else:
        for x in (now-1, now+1, now*2):
            if 0<=x<=100000 and dis[x]==0:
                dQ.append(x)
                dis[x] = dis[now] + 1
