'''
Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern: for example, '2c' or '3a'.

The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.
'''

# using two pointers algorithem
def uncompress (string):
    j = 0
    i = 0
    result = []
    while j < len(string):
        if string[j].isdigit():
            j += 1
        else:
            num = int(string[i:j])
            result.append(num * string[j])
            j +=1 
            i = j
    return ''.join(result)
        
print(uncompress("2c3a1t"))
print(uncompress("4s2b"))
print(uncompress("2p1o5p"))
print(uncompress("3n12e2z"))
print(uncompress("127y"))


'''
n : group of input (3e)
m: group of the output (eee)
time complexity = O(nm)
space complexity = O(nm)
'''