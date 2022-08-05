n, m = map(int, input().split())
dic = {}

for x in range(n):
    site, pw = map(str, input().split())
    dic[site] = pw

for x in range(m):
    print(dic[str(input())])