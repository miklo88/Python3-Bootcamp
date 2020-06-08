'''
Tuples - Are very similar to lists. However they have one key difference - immutability.
Once an element is inside a tuple, it can not be reassigned.
Tuples use parentheses: (1,2,3)

Sets - Are unordered collection of unique elements. 
Meaning there can only be one representative of the same object.
Unique values!

Booleans - Are operators that allow you to convey True or False statements.
These are very important later on when we deal with control flow and logic.

'''
#TUPLES ###
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
# SETS ###
myset = set()
print(myset) # returns set()
myset.add(1)
print(myset) # returns {1}
myset.add(2) 
print(myset) # returns {1, 2}
#now if you try to add(2) again to myset. you'll recieve the same object as before
# that is because sets only work with unique values.
# so any data that is similiar or repetitive are not good for sets.
# what they are good for are casting unique values from a list example below
l = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4]
print(set(l)) # returns {1, 2, 3, 4}
# be mindful that sets don't have a particular order to them.

#BOOLEANS ###
print(True) # returns - True
print(type(True)) # returns - <class 'bool'>
print(False) # returns - False
print(type(False)) # returns - <class 'bool'>

print(1 > 2) # False
print("Yes" == "No") # False
a = 3
b = 3
print(a == b) # True
# Can use NONE as a placeholder for a boolean value if you want to wait to replace its value with something later on.
c = None
print(c) # None



