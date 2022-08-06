n = str(input())
txt = []
cnt = 0

def DFS(ind):
    global cnt
    if ind == len(n):
        cnt+=1
        print("".join(txt))
    
    else:
        for x in range(1, 27):
            if x < 10:
                if int(n[ind]) == x:
                    txt.append(chr(x+64)) 
                    DFS(ind+1)
                    txt.pop()

            else:
                if int(n[ind:ind+2]) == x:
                    txt.append(chr(x+64))
                    DFS(ind+2)
                    txt.pop()

DFS(0)
print(cnt)  
