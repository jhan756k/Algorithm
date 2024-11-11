import sys
n = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))
ac = [0 for _ in range(max(h)+1)]

for x in h:
  if ac[x] > 0:
    ac[x] -= 1
    ac[x-1] += 1
  else:
    ac[x-1] += 1

print(sum(ac))

# 시간초과 풀이 (감소수열 전부 구해서 그 개수 구하기)
# dp = [[x] for x in map(int, sys.stdin.readline().split())]

# for i in range(n):
#   if dp[i] == 0:
#     continue
#   for j in range(i+1, n):
#     if dp[j] == 0:
#       continue
#     elif dp[i][-1] == dp[j][0]+1:
#       dp[i].append(dp[j][0])
#       dp[j] = 0
#       print(dp)
#   dp[i] = 1

# print(sum(dp))