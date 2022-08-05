def DFS(v):
    if v > 7:
        return
    
    else:
        DFS(v*2)
        print(v, end = " ")
        DFS(v*2+1) 

DFS(1)