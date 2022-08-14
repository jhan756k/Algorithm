# 연속되는 것이 필수인 최장 공통 문자열과 달리
# 최장공통부분수열에서는 단순히 문자가 같을 때 dp[i-1][j-1] + 1 하는 것이 아니라
# 문자가 같을때/다를 때 이전 최장공통부분수열 길이의 최댓값으로 계산해야함.

str_1 = str(input())
str_2 = str(input())
a = len(str_1)
b = len(str_2)
dp = [[0]*(a+1) for _ in range(b+1)] # 위, 왼쪽에 마진 생성
res = 0 

for x in range(1, b+1):
    for y in range(1, a+1): 
        if str_1[y-1] == str_2[x-1]: # 만약 두 문자가 같다면
            dp[x][y] = dp[x-1][y-1] + 1 # 이전 최댓값에 1 더해서 저장 
        else:
            dp[x][y] = max(dp[x-1][y], dp[x][y-1]) # 아니라면 이전 최댓값 그냥 저장

        if dp[x][y] > res: # 최대 길이 갱신
            res = dp[x][y] # 하지만 이 코드 필요없이 print(dp[-1][-1]) 해도 됨
            # 어차피 맨 끝에는 최대 길이가 저장될 테니까 

print(res)
