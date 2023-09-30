import sys
num = int(sys.stdin.readline())
k = int(sys.stdin.readline())
start = 1
end = k

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for x in range(1, num+1):
        cnt += min(mid//x, num)
    if cnt >= k:
        ans = mid
        end = mid-1
    else:
        start = mid+1        
print(ans)    

# def getMyDivisor(n):
#     global num
#     nd = 0
#     for i in range(1, int(n**(1/2)) + 1):
#         if (n % i == 0) and n//i <= num:
#             nd+=1 
#             if ( (i**2) != n) : 
#                 nd+=1
#     return nd
# s = 0
# while k > 0:
#     s += 1
#     k -= getMyDivisor(s)
# print(s)