import sys
input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split()))
nlist.sort()
x = int(input())
res = 0
l, r = 0, n-1

while l < r:
    tmp = nlist[l]+nlist[r] 
    
    if tmp == x:
        res += 1
        l+=1
    elif tmp < x:
        l+=1
    elif tmp > x:
        r-=1

print(res)
