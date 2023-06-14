'''
Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern: for example, '2c' or '3a'.

The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.
'''

def uncompress(string):  #'2c3a1t'
    arr =[]
    num = [] #2
    for ele in string:
        if ele.isdigit():
            num.append(ele)
        else:
            multiper = ''.join(num)
            arr.append(int(multiper) * ele)
            num.clear()
    return ''.join(arr)
print(uncompress("2c3a1t"))
print(uncompress("4s2b"))
print(uncompress("2p1o5p"))
print(uncompress("3n12e2z"))
print(uncompress("127y"))