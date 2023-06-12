'''
Write a function, max_value, that takes in list of numbers as an argument. The function should return the largest number in the list.

Solve this without using any built-in list methods.

You can assume that the list is non-empty.
'''

def max_value(nums):
    max = float('-inf') 
    for num in nums:
        if num > max:
            max = num
        elif num == max:
            max = num
    return max


print(max_value([4, 7, 2, 8, 10, 9]))
print(max_value([10, 5, 40, 40.3]))
print(max_value([-5, -2, -1, -11]))
print(max_value([42]))
print(max_value([1000, 8]))
print(max_value([1000, 8, 9000]))
print(max_value([2, 5, 1, 1, 4]))


'''
Complexity
n : number of array elements 
we use loop to iteriate over each element
Time: O(n)

we dont store any variable so I only hve a constant
variable which is max so,
Space: O(1)
'''