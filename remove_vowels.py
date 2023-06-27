'''
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

'''
s = "leetcodeisacommunityforcoders"
def remove_vowels(s):
    vowels = "aeiou"
    new_s =''
    for ele in s:
        if ele not in vowels:
            new_s += ele
    return new_s


print(remove_vowels(s))