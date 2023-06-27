'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.
'''

s = "Hello World"
def last_word(s):
    new_arr = s.strip().split(' ')
    for ele in new_arr:
        if not ele.isalpha():
            new_arr.remove(ele)
    return len(new_arr[-1])


print(last_word(s))


