# 딕셔너리 해쉬
'''
first = str(input())
second = str(input())
l = dict()

for x in first:
    l[x] = l.get(x, 0) + 1

for x in second:
    l[x] = l.get(x, 0) - 1

for x in first:
    if l.get(x) > 0:
        print("NO")
        break

else:
    print("YES")
'''

# 딕셔너리 해쉬 검증 방법

''' 
for i in l.keys():
    if i in s.keys():
        if l[i]!=s[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
'''

'''
if l == s:
    print("YES")
else:
    print("NO")
'''

# 리스트 해쉬
first = input()
second = input()
f = [0]*52
s = [0]*52

for x in first:
    if x.isupper(): # 65 ~ 90 (65 빼면 0 ~ 25)
        f[ord(x)-65] += 1
    
    else: # 97 ~ 122 (71 빼면 26 ~ 51)
        f[ord(x)-71] += 1

for x in second:
    if x.isupper(): 
        s[ord(x)-65] += 1
    
    else: 
        s[ord(x)-71] += 1

for x in range(52):
    if f[x] != s[x]:
        print("NO")
        break
else:
    print("YES")