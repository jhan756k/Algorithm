c = str(input())
stack = []

for x in c:
    if x.isdecimal():
        stack.append(int(x))

    elif x == "+":
        stack.append(stack.pop() + stack.pop())

    elif x == "-":
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2-n1)

    elif x == "*":
        stack.append(stack.pop() * stack.pop())
    
    elif x == "/":
        stack.append(stack.pop() / stack.pop())

print(stack[0])   


