# 분할 정복 : 배열을 2개 부분으로 계속 나눠서 정렬 한 후 다시 merge 하는 정렬 
# 시간복잡도 O(nlogn) 
# 시간복잡도 이해: https://devlimk1.tistory.com/138

def Dsort(lt, rt):
    if lt < rt:
        mid = (lt+rt)//2
        Dsort(lt, mid)
        Dsort(mid+1, rt)
        p1 = lt
        p2 = mid+1
        tmp = []
        while p1<=mid and p2<=rt:
            if arr[p1]<arr[p2]:
                tmp.append(arr[p1])
                p1+=1
            else:
                tmp.append(arr[p2])
                p2+=1

        if p1<=mid:
            tmp+=arr[p1:mid+1]
        if p2<=rt:
            tmp+=arr[p2:rt+1]

        for i in range(len(tmp)):
            arr[lt+i] = tmp[i]

arr = [23, 11, 45, 36, 15, 67, 33, 21]
Dsort(0, 7)
print(arr)