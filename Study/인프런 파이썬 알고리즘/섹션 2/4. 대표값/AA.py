n = int(input())
nlist = list(map(int, input().split()))
unsortlist = nlist.copy()
mean_score = round(sum(nlist)/len(nlist))
nlist.sort()
min = float('inf')
minindex = 0

for x in range(len(nlist)):
    tmp = abs(nlist[x] - mean_score)
    if tmp < min: 
        min = tmp
        minindex = x
    elif tmp == min: # 절댓값 편차가 최솟값과 동일할 때 
        if nlist[x] - mean_score != nlist[minindex] - mean_score: # 실제 편차가 같지 않다면
            min = tmp
            minindex = x # 정렬된 리스트 오름차순으로 돌아서 가능 

print(mean_score, end=" ")
print(unsortlist.index(nlist[minindex]) + 1)
    