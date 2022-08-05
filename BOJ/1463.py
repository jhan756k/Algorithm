from collections import deque
n = int(input())
dis = [0]*(1000001)
dQ = deque()
dQ.append(n)
dis[n] = 1
while dQ:
    now = dQ.popleft()
    if now == 1:
        print(dis[now]-1)
        break

    else:
        if 1<=now-1<=1000001 and dis[now-1]==0:
            dQ.append(now-1)
            dis[now-1] = dis[now]+1

        if now%3==0 and 1<=now//3<=1000001 and dis[now//3]==0:
            dQ.append(now//3)
            dis[now//3] = dis[now]+1

        if now%2==0 and 1<=now//2<=1000001 and dis[now//2]==0:
            dQ.append(now//2)
            dis[now//2] = dis[now]+1



        

