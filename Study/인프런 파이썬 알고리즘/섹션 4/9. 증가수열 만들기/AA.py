n=int(input())
nlist=list(map(int, input().split()))
lt=0
rt=n-1
last=0
res=""
tmp=[]
while lt<=rt:
    if nlist[lt]>last:
        tmp.append((nlist[lt], 'L'))
    if nlist[rt]>last:
        tmp.append((nlist[rt], 'R'))
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        res=res+tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=='L':
            lt=lt+1
        else:
            rt=rt-1
    tmp.clear()

print(len(res))
print(res)