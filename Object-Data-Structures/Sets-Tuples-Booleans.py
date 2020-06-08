'''
Tuples - Are very similar to lists. However they have one key difference - immutability.
Once an element is inside a tuple, it can not be reassigned.
Tuples use parentheses: (1,2,3)

Sets - 

Booleans - 

'''
# t the tuple
t = (1,2,3)
print(type(t)) # return <class 'tuple'>
print(len(t)) # return  3
print(t) # return (1, 2, 3)

t = ('one', 2)
print(t[0]) # returns - one

t = ('a','a','b')
print(t.count('a')) # returns 2 because there are 2 a's in the tuple
print(t.index('a')) # returns 0 because the first a is at index 0