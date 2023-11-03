#Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. The function should return the minimum value within the tree.
from collections import deque
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

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


## depth first solution
def tree_min_val_depth(root):
    min = float("inf")
    if not root:
        return 0
    
    stack = [root]
    while stack:
        current = stack.pop()
        if current.val < min:
            min = current.val

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return min


print(tree_min_val_depth(a)) # -> -2


## breadth first solution 
def tree_min_val_breadth(root):
    min = float("inf")
    queue = deque([root])

    while queue:
        current = queue.popleft()
        if current.val < min:
            min = current.val

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)
    return min


print(tree_min_val_breadth(a))

## recurrsion 

def tree_min_val_recur(root):
    if not root:
        return 0


    left = tree_min_val_recur(root.left)
    right = tree_min_val_recur(root.right)

    return min(root.val, left, right)


print(tree_min_val_recur(a))