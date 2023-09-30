n, m = map(int, input().split())
checklist = [-1]*(n+1)
good = True

for _ in range(m):
    t, i, s = map(int, input().split())

    if checklist[i] == -1: # 저장 기록이 없다면
        if s == 1: # 시작하지도 않았는데 끝나면
            good = False
            continue

        else:
            checklist[i] = t

    else: # 저장 기록이 있다면
        if s == 1: # 끝나면
            if t - checklist[i] < 60: # 만약 60분이 넘지 않는다면
                good = False
                continue

            else: # 만약 60분이 넘으면 i번 초기화
                checklist[i] = -1

        else: # 만약 저장 기록이 있는데 시작하면
            good = False
            continue

for x in checklist:
    if x != -1:
        good = False

if good:
    print("YES")
else:
    print("NO")
