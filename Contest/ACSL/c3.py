str1 = ""
str2 = ""
sp = 0
f1 = True
f2 = True

for x in range(len(n)):
    if value[x] == 0:
        str1 += letter[x]
        sp = x
        break

def ls(index, key):
    global tmp, letter, str1, tmplet, f1, f2
    
    if f1 == False and f2 == False:
        f1 = True
        f2 = True
        return
    
    if index == 0:
        f1 = False
        return rs(index, key)
    
    for x in range(index-1, -1, -1):
        if tmp[x] == key+1:
            str1 += (tmplet[x])
            f1 = True
            return ls(x, key+1)
    else:
        f1 = False
        return rs(index, key)

def rs(index, key):
    global tmp, letter, str1, tmplet, f1, f2

    if f1 == False and f2 == False:
        f1 = True
        f2 = True
        return

    if index == len(tmp)-1:
        f2 = False
        return ls(index, key)
    
    for x in range(index+1, len(tmp)):
        if tmp[x] == key+1:
            str1 += (tmplet[x])
            f2 = True
            return ls(x, key+1)
        
    else:
        f2 = False
        return ls(index, key)

tmplet = letter[:sp+1]
tmp = value[:sp+1]
ls(sp, 0)

tmplet = letter[sp:]
tmp = value[sp:]
rs(0, 0) 

print(str1)