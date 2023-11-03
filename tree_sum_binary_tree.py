# Write a function, tree_sum, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree.

# breadth_first solution
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_sum(root):
    if not root:
        return 0

    sum = 0
    queue = deque([root])

    while queue:
        current = queue.popleft()
        sum += current.val

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return sum


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(tree_sum(a))  # -> 21

# depth_first_solution


def tree_sum_depth(root):
    if not root:
        return 0
    stack = [root]
    sum = 0

    while stack:
        current = stack.pop()
        sum += current.val

        if current.left:
            stack.append(current.left)

        if current.right:
            stack.append(current.right)

    return sum

print(tree_sum_depth(a))


# depth first recurrsionsolution

def tree_sum_depth_recurr(root):
    if not root:
        return 0
    
    return root.val + tree_sum_depth_recurr(root.left) +tree_sum_depth_recurr(root.right)
    

print(tree_sum_depth_recurr(a))