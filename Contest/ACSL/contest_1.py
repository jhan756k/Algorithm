n, b, s = input().split()

def ttn(n, b):
    tempnum = ''
    while n:
        n, r = divmod(n, b)
        tempnum = '0123456789ABCDEF'[r] + tempnum
    return tempnum

def findModeCount(n, b, s):
    s = str(s)
    b = int(b)
    n = int(n)
    sdec = int(s, b)

    nlist = [0]*16

    for _ in range(sdec, sdec+n):
        temp = ttn(_, b)
        for i in str(temp):
            if i=="A":
                nlist[10]+=1
            elif i=="B":
                nlist[11]+=1
            elif i=="C":
                nlist[12]+=1
            elif i=="D":
                nlist[13]+=1
            elif i=="E":
                nlist[14]+=1
            elif i=="F":
                nlist[15]+=1
            else:
                nlist[int(i)]+=1
    
    return max(nlist)

print(findModeCount(n, b, s))
