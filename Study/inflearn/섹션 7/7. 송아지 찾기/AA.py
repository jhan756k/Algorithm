from collections import deque
maxn = 10000 
n,m = map(int,input().split())
ch = [0] * maxn
ch[n] = 1
dQ = deque()
dQ.append(n)

while dQ:
    now = dQ.popleft()
    if now == m:
        break

    for next in (now-1, now+1, now+5):
        if 0<next<maxn:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = ch[now] + 1

print(ch[now]-1)
