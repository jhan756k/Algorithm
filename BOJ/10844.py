n = int(input())
m = [[0]*10 for _ in range(n+1)]

for x in range(1, 10):
    m[1][x] = 1

for i in range(2, n+1):
    m[i][0] = m[i-1][1]
    m[i][9] = m[i-1][8]
    for j in range(1, 9):
        m[i][j] = m[i-1][j-1] + m[i-1][j+1]

print(sum(m[n])%1000000000)

