t = int(input())

for _ in range(t):
    a, b = map(int, input().split())    
    d = b-a
    n = 1
    ind = 0
    for x in range(1, d):
        for _ in range(x):
            ind+=1
            if ind==d:
                print(n)
                break
            
        if ind == d:
            break

        for _ in range(x):
            ind+=1
            if ind==d:
                print(n)
                break
        if ind == d:
            break
        n+=2