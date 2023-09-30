class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

for _ in range(5):
    inp = str(input())

    # create a binary search tree with letters
    # and their values
    tree = Node(inp[0])
    for i in range(1, len(inp)):
        temp = tree
        while True:
            if inp[i] < temp.value:
                if temp.left == None:
                    temp.left = Node(inp[i])
                    break
                else:
                    temp = temp.left
            else:
                if temp.right == None:
                    temp.right = Node(inp[i])
                    break
                else:
                    temp = temp.right
    