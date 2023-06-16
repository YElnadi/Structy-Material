#######################################
# another solution using built in function 


from collections import Counter

def anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

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