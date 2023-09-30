txt = str(input())
bintxt = ""
octtxt = ""
dectxt = ""

for i in txt:
    bintxt += (bin(ord(i))[2:]).zfill(8)

cnt = 0

while True:
    x = len(bin(cnt)[2:])

    for start in range(0, len(bintxt)-x+1):
        if bintxt[start: start+x] == bin(cnt)[2:]:
            bintxt = bintxt[:start] + bintxt[start+x:]
            break
    else:
        break
    
    for start in range(len(bintxt)-x+1, -1, -1):
        if bintxt[start: start+x] == bin(cnt)[2:]:
            bintxt = bintxt[:start] + bintxt[start+x:]
            break

    cnt+=1    

octtxt = format(int(bintxt, 2), 'o')

if "0" not in octtxt:
    print(-1)
    exit()

cnt = 0

while True:
    x = len(oct(cnt)[2:])

    for start in range(0, len(octtxt)-x+1):
        if octtxt[start: start+x] == oct(cnt)[2:]:
            octtxt = octtxt[:start] + octtxt[start+x:]
            break
    else:
        break
    
    for start in range(len(octtxt)-x+1, -1, -1):
        if octtxt[start: start+x] == oct(cnt)[2:]:
            octtxt = octtxt[:start] + octtxt[start+x:]
            break

    cnt+=1
    
print(cnt)
print(octtxt)
