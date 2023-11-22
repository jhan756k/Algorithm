import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
start = 0
end = n
while start <= end:
    mid = (start+end)//2

    

    if a[mid] > a[mid+1]:
        end = mid-1
    else:
        start = mid+1