import sys
m = int(sys.stdin.readline())
s = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    
    else:
        func, x = temp[0], int(temp[1])

        if func == "add":
            s.add(x)
        elif func == "remove":
            s.discard(x)
        elif func == "check":
            print(1 if x in s else 0)
        elif func == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)
                