import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, a ,b = map(int, input().split())
    plist = [1, n]
    ind = 1

    for x in range(n-1, 0, -1):
        plist.append(plist[ind]+x)
        ind += 1
        plist.append(plist[ind]+x)
        ind += 1

    for x in range(len(plist)): # x 는 코너 돈 개수 # plist[x] 는 다음 코너 값

        if a <= plist[x]:
            tmp = plist[x]-a 
            pos = x
            break

    if pos%4 == 1:
        yc = n-(plist[pos]-a + pos//4)-1
        print("s")

    elif pos%4 == 3:
        pos//4
        yc = tmp

    print(yc)
    

'''
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


for _ in range(t):
    N, a, b = map(int, input().split())
    nlist = [[0]*N for _ in range(N)]
    r, c = 0, 0
    dist = 0
    res = []

    for n in range(1, N*N + 1):
        nlist[r][c] = n
        if n == a or n == b:
            res.append((r,c))
            if len(res) == 2:
                break

        r += dx[dist]
        c += dy[dist]

        if r < 0 or c < 0 or r >= N or c >= N or nlist[r][c] != 0:
            r -= dx[dist]
            c -= dy[dist]
            dist = (dist + 1) % 4
            r += dx[dist]
            c += dy[dist]

for x in nlist:
    print(x)

'''