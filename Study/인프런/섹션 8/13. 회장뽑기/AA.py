n = int(input())
dp = [[100]*(n) for _ in range(n)]

for x in range(n):
    dp[x][x] = 0

while True:
    a, b = map(int, input().split())
    if a==-1 and b==-1:
        break
    dp[a-1][b-1]=1
    dp[b-1][a-1]=1

for k in range(n):

    for i in range(n):
        for j in range(n):
            if dp[i-1][j-1] > dp[i-1][k-1]+dp[k-1][j-1]:
                dp[i-1][j-1] = dp[i-1][k-1]+dp[k-1][j-1]

res = []

for x in dp:
    res.append(max(x))

print(min(res), end = " ")
print(res.count(min(res)))
for x in range(len(res)):
    if res[x]==min(res):
        print(x+1, end = " ")
