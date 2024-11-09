n = int(input())
s = 30001
dp = [[] for _ in range(s)]
dp[0] = 0

for _ in range(n):
  p, k = map(int, input().split())
  dp[k].append((p, k))

for t in range(1, s):
  p = dp[t-1]
  if dp[t] != []:
    for l in dp[t]:
      p = max(p, dp[l[0]] + l[1] - l[0])
  dp[t] = p

print(dp[-1])