n = int(input())
nlist = list(map(int, input().split()))

def digit_sum(x):
    count = 0 
    for num in str(x):
        count += int(num)
    
    return count

maxn = -2147000000

for x in range(n):
    tmp = digit_sum(nlist[x])
    if tmp > maxn:
        maxn = tmp
        ans = nlist[x]

print(ans)
