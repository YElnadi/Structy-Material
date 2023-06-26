'''
Write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return a tuple containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.

using hash map is a O(1) lookup

'''

def pair_sum(lst, target):
    pair_sum_dict ={}
    for index, number in enumerate(lst):
        complement = target - number 

        if complement in pair_sum_dict:
            return(pair_sum_dict[complement], index)
        pair_sum_dict[number] = index
        

print(pair_sum([3,2,5,4,1], 8))
