# 가방문제
# 냅색 문제는 기본적으로 dp[j] 에 j(금액)일때 최소/최대가 되는 가치 저장 

n, m = map(int, input().split())
dp = [0]*(m+1)

for i in range(n): # 각 인풋 물건에 대하여 (w, v) = (무게, 가치)
    w, v = map(int, input().split())

    for x in range(w, m+1): # 보석의 무게부터 끝까지
        tmp = dp[x-w] + v  # dp[x-w]+v 가 dp[x] 보다 크면 대입
        
        if tmp > dp[x]: # 이때 dp[x-w]에서 x-w은 자신의 무게를 넣고 남은 값이라 생각.
            dp[x]=tmp # 그 남은 값을 채우는 가치의 최댓값이 dp[x-w]이니
            # 이를 자기 가치(v) 와 더하면 x번째의 가치(dp[x])의 최댓값이 됨  

print(dp[m])