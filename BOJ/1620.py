import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}

for x in range(n):
    pname = input().rstrip()
    dic[pname] = x+1
    dic[x+1]=pname

for y in range(m):
    ans = input().rstrip()
    if ans.isdigit():
        print(dic[int(ans)])
    else:
        print(dic[ans])
