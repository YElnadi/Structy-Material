'''
Write a function, pair_product, that takes in a list and a target product as arguments. The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair whose product is the target.

'''


def pair_product(lst, target):
    previous = {}

    for index, num in enumerate(lst):
        complement = target / num

        if complement in previous:
            return (index, previous[complement])
        previous[num] = index


print(pair_product([3, 2, 5, 4, 1], 8))  # -> (1, 3)
print(pair_product([4, 7, 9, 2, 5, 1], 5))
print(pair_product([4, 7, 9, 2, 5, 1], 35))
print(pair_product([3, 2, 5, 4, 1], 10))
print(pair_product([4, 6, 8, 2], 16))
