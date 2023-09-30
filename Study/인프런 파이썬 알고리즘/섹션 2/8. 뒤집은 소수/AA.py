n = int(input())
nlist = list(map(int, input().split()))

revlist = list(map(lambda x:int(str(x)[::-1]), (x for x in nlist)))

def isPrime(x):
    if x == 1:
        return False
    for y in range(2, x//2 + 1):
        if x%y == 0:
            return False
    return True

for x in range(n):
    if isPrime(revlist[x]):
        print(revlist[x], end=" ")
