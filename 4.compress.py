'''
Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.


'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'
'''

def compress(string):
    j = 0
    i = 0
    result =[]
    count = 0
    string += '!'
    while j < len(string):
        if string[j] == string[i]:
            count += 1
            j += 1
        else:
            ele = str(count) + string[i]
            if count == 1:
                result.append(string[i])
                count = 0
            else:
                result.append(ele)
                count = 0
            i = j
            
    return ''.join(result)

print(compress('ccaaatsss'))
print(compress('ssssbbz'))
print(compress('ppoppppp'))
print(compress('nnneeeeeeeeeeeezz'))
print(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'))