# https://tipsyziasu.tistory.com/136 
# # 위 링크의 코드는 방문여부 체킹을 훨씬 더 단순하게 구현함

# 백준 2655 가장 높은 탑 쌓기 문제

n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]

for x in range(n): # nlist 정렬하기 전에 초기 번호 저장 (1, 2, 3, ...)
    nlist[x].append(x+1)

nlist.sort(key= lambda x:(x[2]), reverse=True)
nlist.insert(0,0)
dp = [0]*(n+1)
dp[1]=nlist[1][1]

use=[0]*(n+1)
use[1] = [nlist[1][3]] # 정렬된 리스트의 첫번째 블럭의 초기 번호 저장

for x in range(2, n+1): # LIS 변형식
    maxn=0
    tmp = -1
    for i in range(x-1, 0, -1):
        if nlist[x][0] < nlist[i][0]:
            if dp[i] > maxn:
                maxn=dp[i]
                tmp = i # 최대가 되는 블럭의 순서를 tmp에 저장하고

    use[x] = [nlist[x][3]] # x 번 블럭의 방문을 자기 자신으로 초기화 하고

    if tmp !=-1:
        use[x]+=use[tmp] # tmp 블럭이 이전에 사용된다면 그 블럭의 하위 방문 추가

    dp[x] = maxn+nlist[x][1]

ind = dp.index(max(dp)) # 최대 높이가 되는 dp 인덱스를 찾고
res = use[ind] # 그 인덱스 번호의 방문리스트를 res 변수에 저장

# 답(res) 출력
print(len(res))

for x in res:
    print(x)
