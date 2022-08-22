# 백준 3273 문제
# 배열을 정렬하고 양 끝의 인덱스에 포인터 정하고 연산

n = int(input())
nlist = list(map(int, input().split()))
nlist.sort() # 무조건 정렬해야함
x = int(input())
res = 0
l, r = 0, n-1

while l < r: # l == r 이면 같은수 두번더해서 결과 오류
    tmp = nlist[l]+nlist[r] # 계산
    
    if tmp == x: # 두 수의 합이 x이면 res 에 1 더함
        res += 1
        l+=1 # 그리고 왼쪽 포인터 앞으로 하나 이동

    elif tmp < x: # x 보다 작으면 합 늘리기 위해 왼쪽 포인터 1 증가
        l+=1
        
    elif tmp > x: # x 보다 크면 합 줄이기 위해 오른쪽 포인터 1 증가 
        r-=1

print(res)
