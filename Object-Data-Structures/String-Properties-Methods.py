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