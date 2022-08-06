# 백준 9095 
# 한 개의 dp 배열을 만들고 배열의 크기가 n 이상이 될때까지 dp 배열을 채워서
# 모든 테스트 케이스에 적용시킨 코드

# 그러나 매번 dp = [0]*(n+1) 이런식으로 배열을 새로 정의하는 것보다
# 밑에 있는 코드가 시간이 더 오래 걸림..??

t = int(input())
nlist = [int(input()) for _ in range(t)]
dp = [None, 1, 2, 4]
    
for n in nlist:

    while n+1 > len(dp):
        tmp = len(dp)
        dp.append(dp[tmp-1]+dp[tmp-2]+dp[tmp-3])

    print(dp[n])

# 가능한 원인
# 1.문제에서 배열 크기 제한이 너무 작아서 단순하게 매번 배열 재정의 하는 것이 빠름
# 2.매번 호출되는 append 와 len 함수 때문에 시간 차이가 생김 

# 모르겠다 
