t = int(input())
ans = []
for _ in range(t):
    a, b = map(int, input().split())    
    d = b-a
    n = 1
    ind = 0
    if d == 0:
        ans.append(0)
        continue
    elif d==1:
        ans.append(1)
        continue
    
    for x in range(1, d):
        ind += x
        if ind >= d:
            ans.append(n)
            break
        ind += x
        n+=1
        if ind >= d:
            ans.append(n)
            break
        n+=1

for x in ans:
    print(x)