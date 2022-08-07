n = int(input())
p = dict()

for i in range(n):
    word = input()
    p[word] = 1

for i in range(n-1):
    word = input()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)
        break

'''
n = int(input())
prelist = [str(input()) for _ in range(n)]
wlist = [str(input()) for _ in range(n-1)]

for x in prelist:
    if x not in wlist:
        print(x)
        break
'''