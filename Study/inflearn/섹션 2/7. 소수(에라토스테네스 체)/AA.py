n = int(input())
nlist = [0] * (n+1)
cnt = 0
 
for x in range(2, n+1): # N 까지의 모든 수 중에서
    if nlist[x] == 0: # 체크가 안된수는 소수이므로 체크 하고 소수카운트 +=1
        cnt+=1
        for y in range(x, n+1, x): # 체크한 소수의 배수는 모두 체크
            nlist[y] = 1

print(nlist)
print(cnt)