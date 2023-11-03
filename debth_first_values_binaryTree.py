# Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.

# Hey. This is our first binary tree problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ

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



def depth_first(root):
    if not root:
        return []
    
    stack = [root]
    values = []

    while stack:
        node = stack.pop()
        values.append(node.val)
        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return values


print(depth_first(a))

# RECURSIVE SOLUTION

def depth_first_values(root):
    if not root:
        return []
    
    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)

    return [root.val, *left_values, *right_values]


print(depth_first_values(a))