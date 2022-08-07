n, m = map(int, input().split())
nlist = list(map(int, input().split()))
nlist.sort()

start = 0 
end = n-1

while start <= end:
    
    mid = (start+end)//2

    if nlist[mid] == m:
        print(mid+1)
        break   
    elif nlist[mid] > m:
        end = mid-1
    elif nlist[mid] < m:
        start = mid+1
