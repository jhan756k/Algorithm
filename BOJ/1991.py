import sys
input = sys.stdin.readline
n = int(input())
tree = {}

for _ in range(n):
    a, b, c = map(str, input().split())
    tree[a] = [b, c]

def prefix(v):
    if v != ".":
        print(v, end = "")
        prefix(tree[v][0])
        prefix(tree[v][1])

def infix(v):
    if v != ".":
        infix(tree[v][0])
        print(v, end = "")
        infix(tree[v][1])

def postfix(v):
    if v != ".":
        postfix(tree[v][0])
        postfix(tree[v][1])
        print(v, end = "")
    
prefix("A")
print()
infix("A")
print()
postfix("A")
