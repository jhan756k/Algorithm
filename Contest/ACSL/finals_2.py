class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_binary_tree(input_list):
    if not input_list:
        return None

    nodes = [Node(value) for value in input_list]
    root = nodes[0]
    queue = [root]
    i = 1

    while queue and i < len(nodes):
        current = queue.pop(0)

        if current:
            current.left = nodes[i]
            queue.append(current.left)
            i += 1

            if i < len(nodes):
                current.right = nodes[i]
                queue.append(current.right)
                i += 1

    return root

def find_paths(root):
    if not root:
        return []

    paths = []

    def dfs(node, path, sums):
        if not node:
            return

        path.append(node.value)

        if not node.left and not node.right:
            sums.append(sum(path))

        dfs(node.left, path, sums)
        dfs(node.right, path, sums)

        path.pop()

    sums = []
    dfs(root, [], sums)
    return sums

# Example usage
input_list = [3, 1, 4, 1, 5, 9, 2, 6]
tree = build_binary_tree(input_list)
sums = find_paths(tree)
distinct_sums = set(sums)

print("Sums of paths between each pair of nodes:")
for path_sum in sums:
    print(path_sum)

print("Number of distinct sums:", len(distinct_sums))

'''
(a b (ac) (a (bc)) (cb)(abc)) --> cons
( (abc) (cb) (a(bc)) (ac) b a)   --> reverse
(a(bc)) --> CADDR
c --> CADDR



'''