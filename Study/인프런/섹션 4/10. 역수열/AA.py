n = int(input())
nlist = list(map(int, input().split()))
anslist = [0]*n

for number in range(1, n+1):
    cnt = 0
    ind = 0
    while cnt != nlist[number-1]+1:
        if anslist[ind] == 0:
            cnt +=1
            ind +=1
        else:
            ind+=1

    anslist[ind-1] = number

for n in anslist:
    print(n, end = " ")