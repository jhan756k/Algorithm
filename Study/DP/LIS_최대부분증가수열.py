# 배열 주어졌을 때 가장 길게 증가하는 수열의 길이 최댓값 구하기

n = int(input())
nlist = list(map(int, input().split()))
nlist.insert(0,0) # 번호와 인덱스 일치시키기 위함
dp=[0]*(n+1)
dp[1] = 1 # 첫 번째 값은 항상 길이 1인 증가수열임

for i in range(2, n+1): # dp 배열 채워나가는 for 문
    maxn = 0
    for j in range(i-1, 0, -1): # i 이전까지의 숫자를 돌면서
        if nlist[j] < nlist[i] and dp[j]>maxn: 
            # i 이전의 숫자가 i의 숫자보다 작고
            # j의 dp 값(배열최대길이)이 만약 i 이전의 숫자들 중 가장 크다면
            maxn = dp[j] # dp[j] 를 최대에 대입

    # 모든 i 이전의 값 순회 후 가장 큰 dp 값에 현재 번호의 길이 (1) 을 더해 저장
    dp[i] = maxn+1 
    
print(max(dp)) # 가능한 배열 길이중 최댓값 출력