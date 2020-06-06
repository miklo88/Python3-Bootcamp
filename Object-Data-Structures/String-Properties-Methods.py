'''
String Indexing and Slicing
'''
mystring = "Hello world"
print(mystring)
# INDEXING
print('//////INDEXING')
print(mystring[0]) # H
print(mystring[8]) # r
# reverse indexing
print(mystring[-2]) # l
# If you want to grab the last index/character of a string default is -1. Great for long names etc.
longstring = "Carlos Adrian Redding Concepcion"
print(longstring[-1]) # n 

# SLICING
print('//////SLICING')
mystring = 'abcdefghijklmnopqrstuvwxyz'
#starting at c and going all the way to the end
print(mystring[2:])
#grabbing everything up to
print(mystring[:3])
#grabbing a subsection of a string
print(mystring[3:6])
print(mystring[1:8])
#step size. jumping indexes
print(mystring[::2])
#step size. reversing a string from all the way to the beginning to the end reversed.
print(mystring[::-1])

'''
String Properties and Methods
-Immutability: Cannot mutate or change

'''
# name = "Sam"
# name[0] = 'P'
# error will occur because we cannot re-assign a character to the string.

# We can do some string concatination
last_letters = 'am'
print('P' + last_letters)
# 'Pam'

#string concatination.
x = "Hello World"
print(x + " it is beautiful outside!")

#multiplication for string concatination
letter = 'z'
print(letter * 10)

print(letter.upper())
lowercase = 'AAAAAA'
print(lowercase.lower())

x = 'Hi this is a split string'
print(x.split('i'))

#STRING INTERPOLATION
print('//////////////Formating string literals, and .format method')
# a good way to format objects into your strings for print statements is with the string .format() method.
# the syntax is - 'String here{} also aqui {}'.format('something1', 'something2')
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
# returns - 'The fox brown quick' using integer assignment
print('First Name: {FName} Last Name: {LName}'.format(FName='Carl', LName='Redding'))
# returns - First Name Carl, Last Name Redding. - using variable assignment keywords.

#Float formatting follows "{value:width.precision f}"
result = 100/77
print(result)
print("The result was {r:10.3f}".format(r=result)) #1.299
# adding width will bring in more whitespace. but keep in mind you're mainly playing with precision.
print("The result was {r:13f}".format(r=result)) #1.298701
print("The result was {r:3.1f}".format(r=result)) #1.3

#F string literals
# new kid on the block. a lot of devs have been waiting for this feature to come out. crossplatform friendly.
name = 'Celia'
print(f'Her name is {name}')

