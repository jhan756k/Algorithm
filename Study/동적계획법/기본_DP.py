# DP는 기본적으로 Bottom-up, Top-down 두가지 방식이 있음. 

# 기본적인 Bottom-up 방식
# - for 문 사용해서 dp 배열 채워나감

n = int(input())
dp = [0]*(n+1)
dp[1] = 1
dp[2] = 2

for x in range(3, n+1):
    dp[x] = dp[x-1]+dp[x-2]

print(dp[n])

# 기본적인 Top-down 방식
# - DFS 호출로 하위 값들을 불러내서 연산함 

n = int(input())
dp = [0]*(n+1)
dp[1]=1
dp[2] = 2

def DFS(v):
    if dp[v]>0:
        return dp[v]

    elif v == 1 or v == 2:
        return v

    else:
        dp[v] = DFS(v-1)+DFS(v-2)
        return dp[v]

DFS(n)
print(dp[n])

# 예시: 계단 1/2 만큼씩만 올라갈수 있을 때 n층까지 가는 경우의 수 구하기