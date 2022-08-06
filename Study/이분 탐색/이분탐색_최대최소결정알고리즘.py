# 백준 2805 나무 자르기 문제 

n, m = map(int, input().split())
nlist = list(map(int, input().split()))

def bt(): 
    s, e, res =0, max(nlist), 0
    
    while s <= e: # 같은 경우도 while문 돌아야함 마지막에 원소 2개 탐색할때 잘못 탐색되는 경우 존재
        
        mid = (s+e)//2 # mid 값 정해주고

        cut_tree = 0 # mid 값에 의해 잘린 나무 길이 계산하는 for 문
        for x in nlist:
            if x > mid:
                cut_tree += (x-mid)

        if cut_tree == m: # 만약 같으면 이미 최소이므로 res에 mid 값 저장 한 후 break
            res = mid
            break

        elif cut_tree > m: # 잘린 나무가 이미 m 보다 많다면 일단 res 에 mid 저장 후 더 좁은 범위에서 계속 이분 탐색 (s<=e까지)
            res = mid
            s = mid+1

        elif cut_tree < m: # 잘린 나무가 적다면 절단기 높이 탐색 범위를 s__mid__e 에서 s_mid_e_____ 로 바꿈
            e = mid-1

    return res # s > e 되면 res 값 반환 

print(bt())
