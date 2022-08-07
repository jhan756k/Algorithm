# 최대점수 구하기 문제
# 1회 사용 문제는 무한 사용과 동일하나 중복 방지 위해서
# 왼쪽 -> 오른쪽 이 아닌 오른쪽 -> 왼쪽 순서대로 연산한다

n, m = map(int, input().split())
dp = [0]*(m+1)

for i in range(n):
    pv, pt = map(int, input().split())
    for j in range(m, pt-1, -1): # m부터 pt까지 (거꾸로)
        tmp = dp[j-pt]+pv # 무한사용과 로직은 동일
        if dp[j] < tmp:
            dp[j] = tmp

print(dp[m])    