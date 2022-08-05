n, k = map(int, input().split())
cnt = 0

while True:
    if bin(n).count('1') > k:
        n+=1
        cnt +=1
    else:
        break

print(cnt)


'''
while True:
    for x in range(len(wlist)):
        if wlist[x] >= 2:
            if len(wlist) < x+2:
                wlist.append(wlist[x]//2)
                wlist[x] %=2
            else:
                wlist[x+1] += wlist[x]//2
                wlist[x] %= 2

    if sum(wlist) > k: 
        wlist[0] += 1
        cnt += 1

    else:
        break

print(cnt)
'''
