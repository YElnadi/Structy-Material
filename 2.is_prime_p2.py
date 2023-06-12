'''
Write a function, is_prime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.

A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.

You can assume that the input number is a positive integer.

'''


# to cut down complexity we use this approache 
from math import sqrt, floor
def is_prime(input):
    if input < 2:
        return False
    for num in range(2, floor(sqrt(input))+1):
        if input % num == 0:
            return False
    return True



print(is_prime(4))
print(is_prime(5))
print(is_prime(6))
print(is_prime(7))
print(is_prime(8))
print(is_prime(25))
print(is_prime(31))
print(is_prime(2017))
print(is_prime(2048))
print(is_prime(1))
print(is_prime(713))


'''
complexity
input: input number
let input = 64
instead of checking all the possuble factors from 2 to 64
we check from 2 to 8 (the sqrt of 64)
Time: O(sqrt(n))
Space: O(1)
'''
