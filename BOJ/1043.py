n, m = map(int, input().split())
knowlist = list(map(int, input().split()))
knowlist.pop(0)
parent = [i for i in range(n+1)]

def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    pa = find(a)
    pb = find(b)
    
    if pa in knowlist and pb in knowlist:
        return

    if pa in knowlist:
        parent[pb] = pa
    
    elif pb in knowlist:
        parent[pa] = pb
    
    else:
        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb

party = []

for _ in range(m):
    plist = list(map(int, input().split()))
    plist.pop(0)
    party.append(plist)

    for i in range(len(plist)-1):
        union(plist[i], plist[i+1])
    
cnt = 0
    
for p in party:
    for i in range(len(p)):
        if find(p[i]) in knowlist:
            break
    else:
        cnt+=1

print(cnt)
