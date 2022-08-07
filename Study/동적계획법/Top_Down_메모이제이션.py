# 알리바바와 40인의 도적 문제

n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

def DFS(x, y): # 이 함수는 (x,y) 좌표의 최댓값 불러오는 함수임
    
    if dp[x][y]!=0: # 만약 0 이 아닌 값이 dp 배열에 저장되어 있으면 그 값 반환
        return dp[x][y]

    if x==0 and y==0:
        dp[x][y] = nlist[0][0] # 그냥 return nlist[0][0] 해도 됨 
        return dp[x][y]        # dp 배열의 (0,0)좌표에 아무것도 저장되지 않을 뿐임

    else:
        if y==0: # 모든 경우에 바로 재귀함수를 호출하는게 아니라 먼저 dp 배열에 저장(메모이제이션)
                 # 하고 그 값이 나중에 다시 호출될 때 위 if dp[x][y]!=0 조건문에서 값 반환
            dp[x][y] = DFS(x-1, y) + nlist[x][y]
            return dp[x][y]

        elif x==0:
            dp[x][y] = DFS(x, y-1) + nlist[x][y]
            return dp[x][y]

        else:
            dp[x][y] =  min(DFS(x,y-1), DFS(x-1,y))+nlist[x][y]
            return dp[x][y] 

print(DFS(n-1, n-1))