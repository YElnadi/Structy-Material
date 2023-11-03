#Write a function, breadth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in breadth-first order.
from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f



def breadth_first(root):
    if not root:
        return []
    
    queue = deque([root])
    values = []
    while queue:
        current = queue.popleft()
        values.append(current.val)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return values


print(breadth_first(a))



    
