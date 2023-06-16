'''
Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty.
'''

def most_frequent_char(s1):
    s1_dict = {}

    for char in s1:
        if char not in s1_dict:
            s1_dict[char] = 0
        s1_dict[char] += 1

    return max(s1_dict, key=s1_dict.get)

print(most_frequent_char('bookeeper'))
print(most_frequent_char('david'))
print(most_frequent_char('abby'))
print(most_frequent_char('mississippi'))
print(most_frequent_char('potato'))
print(most_frequent_char('eleventennine'))
print(most_frequent_char('riverbed'))
