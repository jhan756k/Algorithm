n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))
anslist = []
p0, p1 = 0, 0

while p0 < n and p1 < m:

    if nlist[p0] < mlist[p1]:
        anslist.append(nlist[p0])
        p0+=1
        
    else:
        anslist.append(mlist[p1])
        p1+=1

if p0<n:
    anslist += nlist[p0:]
if p1 < m:
    anslist += mlist[p1:]

for x in anslist:
    print(x, end=" ")