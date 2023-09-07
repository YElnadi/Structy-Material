# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# ## unconnectd nodes
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #       a
# #      / \
# #     b   c
# #    / \   \
# #    d  e   f

# def search (nums, target):
#     for index, num in enumerate(nums):
#         if num == target:
#             return index
#     return -1


# print(search([-1,0,3,5,9,12], 9))


# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return -1

#         left_path = maxDepth(root.left)
#         right_path = maxDepth(root.right)

#         return 1 + max(left_path, right_path)


# def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#     count_nums = {}
#     ans = []
#     for i in nums:
#         if nums[i] not in count_nums:
#             count_nums[i] = 0
#         count_nums[i] += 1

#     res = [key, value for keys, values in count_nums.items()]  # [(1,3), (2,2), (3,1)]

#     for i in range(0, k-1):
#         ans.append(res[i[0]])
#     return ans


