def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 배열 전체를 i 번 순회하며 arr[j], arr[j+1] 를 비교하여 하나씩 바꿔서 정렬함
# 버블정렬의 시간복잡도는 for 문 두개가 n개를 각각 탐색함 --> O(n^2)
# 느린 속도 때문에 보통 사용 X