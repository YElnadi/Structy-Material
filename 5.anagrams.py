'''
Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

'''

def anagrams(s1, s2):
    s1_dict = {}
    s2_dict = {}

    for ele in s1:
        if ele not in s1_dict:
            s1_dict[ele] = 0
        s1_dict[ele] += 1

    for ele in s2:
        if ele not in s2_dict:
            s2_dict[ele] = 0
        s2_dict[ele] += 1

    return s1_dict == s2_dict


print(anagrams('cats', 'tocs'))
print(anagrams('restful', 'fluster'))
print(anagrams('monkeyswrite', 'newyorktimes'))
print(anagrams('paper', 'reapa'))
print(anagrams('elbow', 'below'))
print(anagrams('tax', 'taxi'))
print(anagrams('taxi', 'tax'))
print(anagrams('night', 'thing') )
print(anagrams('abbc', 'aabc'))
print(anagrams('po', 'popp'))
print(anagrams('pp', 'oo'))


        
