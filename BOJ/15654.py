n, m = map(int, input().split())
nlist = list(map(int, input().split()))

nlist.sort()
vis = [False] * n
out = []

def DFS(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return

    for i in range(N):
        if not vis[i]:
            vis[i] = True
            out.append(nlist[i])
            DFS(depth+1, N, M)
            out.pop()
            vis[i] = False

DFS(0, n, m)
