charlist = str(input())
stack = []
res = 0

for x in range(len(charlist)):

    if charlist[x] == "(":
        stack.append(charlist[x])

    else:
        if charlist[x-1] == "(":
            stack.pop()
            res += len(stack)
        
        else:
            stack.pop()
            res+=1

print(res)
