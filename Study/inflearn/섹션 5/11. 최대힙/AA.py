import heapq as hq
a = []

# heapq 모듈은 기본적으로 최소힙임. 하지만 입력을 음수로 받으면 최대힙의 효과 낼 수 있음.

while True:
    n = int(input())

    if n == -1:
        break

    if n == 0:      
        if a:
            print(-hq.heappop(a)) # 출력할 땐 원상복귀
        else:
            print(-1)

    else:
        hq.heappush(a, -n) # 입력 음수로 하고
        