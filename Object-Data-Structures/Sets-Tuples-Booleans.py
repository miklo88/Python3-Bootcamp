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

#lets see a side by side comparison
mylist= [1,2,3,4,5 ]
mylist[0] = 'One'
print(mylist) # returns - ['One', 2, 3, 4, 5] # no problem! lets try this with a tuple

# t[0] = 'One'
# print(t)
# returns - Traceback (most recent call last):
#   File "Sets-Tuples-Booleans.py", line 29, in <module>
#     t[0] = 'One'
# TypeError: 'tuple' object does not support item assignment
# womp womp, tuples aren't havin it.
'''
Arises the question of why would I use tuples? As a beginner you won't use them much but after becoming more advanced you'll see 
the importance of their data-integrity and being able to flow throughout a program without having their values reassigned. 
'''


