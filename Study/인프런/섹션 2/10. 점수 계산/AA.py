n = int(input())
nlist = list(map(int, input().split()))
score = 0
tmpcount = 1

for x in range(len(nlist)):
    
    if nlist[x] == 1:
        score += tmpcount
        tmpcount +=1
        
    else:
        tmpcount = 1
    
print(score)
