from collections import deque

blueprint = str(input())
n = int(input())

for _ in range(n):
    hclass = deque(str(input()))
    copyprint = deque(blueprint)

    for x in range(len(hclass)):
        tmp = hclass.popleft()

        if tmp == copyprint[0]:
            copyprint.popleft()
            
        elif any(tmp == x for x in copyprint):
            break

        if not copyprint:
            break

    if copyprint:
        print(f"#{_+1} NO")
    else:
        print(f"#{_+1} YES")
