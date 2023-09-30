n = str(input())
letter = [None] * len(n)
value = [None] * len(n)

letter[0] = n[0]
value[0] = 0

for x in range(1, len(n)): 
    for a in range(len(n)):
        if letter[a] == None:
            letter.insert(a, n[x])
            letter.pop()
            value.insert(a, value[a-1]+1)
            value.pop()
            break

        if n[x] <= letter[a]:
            letter.insert(a, n[x])
            letter.pop()
            if a-1 < 0 or a-1 == None:
                value.insert(a, value[a]+1)
            else:
                value.insert(a, max(value[a-1], value[a])+1)

            value.pop()
            break  
str1 = ""
str2 = ""

class Node:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
        self.left = None
        self.right = None

def search(varr, larr):
    global str1

    if not varr:
        return None
    
    pivot = min(varr)
    tree = Node(larr[varr.index(pivot)], pivot)

    if varr.index(pivot) != 0:
        tree.left = search(varr[:pivot], larr[:pivot])
    if varr.index(pivot) != len(varr)-1:
        tree.right = search(varr[pivot+1:], larr[pivot+1:])
    
    return tree

def printTree1(root):
    global str1

    if root:
        printTree1(root.left)
        str1 += root.letter
        printTree1(root.right)

printTree1(search(value, letter))
print(str1)