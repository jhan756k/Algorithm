# N Queens 문제
# 한 행에는 퀸이 하나밖에 존재할 수 없으니까 for 문의 주체를 행으로 잡는게 핵심

n = int(input())
col=[0]*15 # col[i] = j 이면 i번째 행에서 퀸이 위치한 곳은 j번 좌표라는 뜻
cnt = 0

def check(x):
    for i in range(x): # x번 행 이전 퀸까지 순회
        if col[x] == col[i] or abs(col[i]-col[x]) == x-i:
        # 만약 x번행과 열이 같은 퀸이 존재 or 대각선상 겹치면 거짓 반환
            return False
    return True

def DFS(x):
    global cnt
    if x == n: # 만약 보드의 끝이면 cnt++ 후 리턴
        cnt += 1
        return

    for i in range(n): # 한 행의 모든 값 순회
        col[x] = i # x번째 행에는 i번에 퀸이 위치해있다 (어차피 한 행에는 퀸 하나)
        if check(x): # 겹침 여부 확인하고 만약 안겹치면 다음행으로 이동
            DFS(x+1)

DFS(0)
print(cnt)
