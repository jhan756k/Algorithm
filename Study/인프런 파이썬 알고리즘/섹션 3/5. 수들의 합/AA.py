# Timeout Error

''' 
n, m = map(int, input().split())
nlist = list(map(int, input().split()))
cnt = 0

for i in range(n):
    for j in range(i, n):

        if sum(nlist[i:j+1]) > m:
            break

        if sum(nlist[i:j+1]) == m:
            cnt +=1
            break
'''

n, m = map(int, input().split())
nlist = list(map(int, input().split()))

lt = 0
rt = 1
tot = nlist[0]
cnt = 0

while True:
    if tot<m:
        if rt < n:
            tot += nlist[rt]
            rt +=1

        else:
            break

    elif tot==m:
        cnt +=1
        tot -=nlist[lt]
        lt +=1

    else:
        tot -= nlist[lt]
        lt+=1

print(cnt)