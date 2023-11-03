# Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.

# depth first solution
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f


def tree_include_depth(root, target):
    if not root:
        return False

    stack = [root]
    while stack:
        current = stack.pop()
        if current.val == target:
            return True

        if current.left:
            stack.append(current.left)

        if current.right:
            stack.append(current.right)

    return False


print(tree_include_depth(a, "e"))  # -> True


## breadth first solution

def tree_include_breadth(root, target):
    if not root:
        return False
    
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current.val == target:
            return True
        
        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return False

print(tree_include_breadth(a, "e"))  # -> True


## recursion

def tree_include_recurr(root, target):
    if not root:
        return False
    
    if root.val == target:
        return True
    
    return tree_include_recurr(root.left, target) or tree_include_recurr(root.right, target)


print(tree_include_recurr(a, "e"))  # -> True
