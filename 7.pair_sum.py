'''
Write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return a tuple containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.

'''
def pair_sum(lst, target):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                return (i, j)


print(pair_sum([3,2,5,4,1], 8))
print(pair_sum([4, 7, 9, 2, 5, 1], 5)) # -> (0, 5)
print(pair_sum([4, 7, 9, 2, 5, 1], 3))
print(pair_sum([1, 6, 7, 2], 13))
print(pair_sum([9, 9], 18))
print(pair_sum([6, 4, 2, 8 ], 12))