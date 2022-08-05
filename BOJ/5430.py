from collections import deque
t = int(input())

for _ in range(t):
    func = deque(list(str(input())))
    n = int(input())
    nlist = deque(input()[1:-1].split(","))

    st = False
    flag = 0

    while func:
        now = func.popleft()
        if now == "R":
            flag+=1
        elif now == "D":
            if not nlist or n == 0:
                print('error')
                st = True
                break
            else:
                if flag%2==0:
                    nlist.popleft()
                else:
                    nlist.pop()
    if st:
        continue

    if flag % 2 == 0:
            print("[" + ",".join(nlist) + "]")
            
    else:
        nlist.reverse()
        print("[" + ",".join(nlist) + "]")