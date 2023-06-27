'''
Given two binary strings a and b, return their sum as a binary string.

'''
def addBinary(a, b):
    sum = bin(int(a,2) + int(b,2))
    return sum[2:]


print(addBinary("1010", "1011"))