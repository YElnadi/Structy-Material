'''
Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.
'''
# s1 = {'apple', 'banana', 'orange'}
# s2 = {1,2,3,4}
# s2.add('lemon')
# s3 =s2.copy()
# s4 = s2.difference(s1) 

# print(s2)
# print(s3)
# print(s4)


def intersection(lst1, lst2):
    s1 = set(lst1)
    s2 = set(lst2)
    s3 = s1.intersection(s2)
    return(list(s3))

    
    



print(intersection([4,2,1,6], [3,6,9,2,10]))
print(intersection([2,4,6], [4,2]))
print(intersection([4,2,1], [1,2,4,6]))
print(intersection([0,1,2], [10,11]))

a = [ i for i in range(0, 50000) ]
b = [ i for i in range(0, 50000) ]
print(intersection(a, b))