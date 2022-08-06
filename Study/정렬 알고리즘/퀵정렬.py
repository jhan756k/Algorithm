# 병합정렬과는 달리 구역의 끝값을 pivot 값으로 정하고 이보다 작은 
# 수와 큰 수로 나눠서 정렬함 
# https://gyoogle.dev/blog/algorithm/Quick%20Sort.html 

def Qsort(lt, rt):
    if lt<rt:
        pos = lt
        pivot = arr[rt]
        for i in range(lt, rt):
            if arr[i] <= pivot:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos+=1
        arr[rt], arr[pos] = arr[pos], arr[rt]
        print(arr)
        Qsort(lt, pos-1)
        Qsort(pos+1, rt)
        
arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
Qsort(0, 9)
