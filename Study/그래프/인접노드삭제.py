# 백준 10026 적록색약 문제

# 우선 일반인을 board에, 적록색약을 sboard 에 저장

from collections import deque
n = int(input())
board = [list(input()) for _ in range(n)]
sboard = [[0]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if board[x][y] == 'G': 
            sboard[x][y] = 'R' # 적록색약 배열에는 G와 R이 같아야 함으로 G 를 R 로 저장함
        else:
            sboard[x][y] = board[x][y]

dQ = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
use = [board, sboard] # 이 당시 일반인, 적록색약 배열을 for 문에서 어떻게 각각 호출할지 생각이 안나서 쓴 임시방편

for times in range(2):
    tmpboard = use[times] # 2번의 for 문 동안 일반인, 적록색약에 대한 계산 따로 함
    cnt = 0

    for x in range(n): # 배열의 모든 x, y 좌표 탐색하면서
        for y in range(n):

            if tmpboard[x][y] != 0: # 아직 그 (x,y) 가 0이 아니라면
                dQ.append((x,y)) # 데크에 좌표 추가 후 
                tmp = tmpboard[x][y]
                tmpboard[x][y] = 0

                while dQ: # BFS 로 근처에 인접한 자신과 같은 색깔을 모두 0으로 바꿔버림
                    now = dQ.popleft()
                    for i in range(4):
                        tx = now[0] + dx[i]
                        ty = now[1] + dy[i]
                        if 0<=tx<=n-1 and 0<=ty<=n-1 and tmpboard[tx][ty] == tmp:
                            dQ.append((tx,ty))
                            tmp = tmpboard[tx][ty]
                            tmpboard[tx][ty] = 0

                # 이 BFS while 문이 돌고 나면 인접한 색깔 군집 하나가 사라짐
                cnt += 1 # 따라서 군집 카운트 변수에 하나 추가
    print(cnt) 
    