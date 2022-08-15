import sys
input = sys.stdin.readline

n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3

for i in range(n):
    a, b, c = map(int, input().split())

    max_tmp[0] = a + max(max_dp[0], max_dp[1])
    min_tmp[0] = a + min(min_dp[0], min_dp[1])

    max_tmp[1] = b + max(max_dp[0], max_dp[1], max_dp[2])
    min_tmp[1] = b + min(min_dp[0], min_dp[1], min_dp[2])

    max_tmp[2] = c + max(max_dp[2], max_dp[1])
    min_tmp[2] = c + min(min_dp[2], min_dp[1])

    for j in range(3):
        max_dp[j] = max_tmp[j]
        min_dp[j] = min_tmp[j]

print(max(max_dp), min(min_dp))
for x in max_dp:
    print(x)