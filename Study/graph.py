class Node:
    def __init__(self, item):
        self.item = item    
        self.left = None
        self.right = None
    
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)
n8 = Node(80)

class Binary_Tree():
    def __init__(self):
        self.root = None

tree = Binary_Tree()
tree.root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8

def preord(n):

    if n != None:

        if n.left:
            preord(n.left)
        
        print(n.item, end=' ')
        if n.right:
            preord(n.right)

preord(n1)

