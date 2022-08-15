n, m = map(int, input().split())

nlist = []

def DFS(start):

    if len(nlist) == m: # 만약 배열 길이가 m이 된다면 출력
        print(' '.join(map(str, nlist)))
        return
    
    for i in range(start,n+1): # start 부터 n 까지
        nlist.append(i)
        DFS(i+1)
        nlist.pop()
        
DFS(1)
