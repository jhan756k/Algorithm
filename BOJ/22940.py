n = int(input())
A = []
for _ in range(n):
  A.append(list(map(int, input().split())))
x = [0] * n

for i in range(n):
  for j in range(i+1, n):
    ratio = A[j][i]/A[i][i]
    for k in range(n+1):
      A[j][k] -=ratio*A[i][k]
x[n-1] = A[n-1][n]/A[n-1][n-1]
for i in range(n-2,-1,-1):
  x[i]=A[i][n]
  for j in range(i+1,n):
      x[i] = x[i] - A[i][j]*x[j]
  x[i] = x[i]/A[i][i]

print(*map(round, x))