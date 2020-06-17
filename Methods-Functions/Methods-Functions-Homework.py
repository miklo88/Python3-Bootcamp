'''
Functions and Methods Homework
'''
'''
Write a function that computes the volume of a sphere given its radius
The volume of a sphere is given as
'''

def vol(rad):
    return (4/3)*(3.14)*(rad**3)
# Check
print(vol(2))

'''
Write a function that checks whether a number is in a given range (inclusive of high and low)
'''
# for item in range(0,5):
#     print(item)

def ran_check(num,low,high):
    if num in range(low,high+1):
        print(f'{num} is in range of {low} and {high}')
    else:
        print('not in range')
# Check
print(ran_check(5,2,7))
# 5 is in the range between 2 and 7
# If you only wanted to return a boolean:
def ran_bool(num,low,high):
    pass
# ran_bool(3,1,10)
'''
Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33

HINT: Two string methods that might prove useful: .isupper() and .islower()

If you feel ambitious, explore the Collections module to solve this problem!
'''
#dictionary way of doing it
def up_low(s):
    d = {'upper':0, 'lower':0}
    for char in s:
        if char.isupper():
            d['upper'] += 1
        elif char.islower():
            d['lower'] += 1
        else:
            pass
    print(f'Original String: {s}')
    print(f'Lowercase Count: {d["lower"]}')
    print(f'Uppercase Count: {d["upper"]}')

# #two separate variables
def up_low(s):
    lowercase = 0
    uppercase = 0

    for char in s:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        else:
            pass
    print(f'Original String: {s}')
    print(f'Lowercase Count: {lowercase}')
    print(f'Uppercase Count: {uppercase}')
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))
# Original String :  Hello Mr. Rogers, how are you this fine Tuesday?
# No. of Upper case characters :  4
# No. of Lower case Characters :  33

'''
Write a Python function that takes a list and returns a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''
def unique_list(lst):
    pass
# unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
# [1, 2, 3, 4, 5]
'''
Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24
'''
def multiply(numbers):  
    pass
# multiply([1,2,3,-4])
# -24
'''
Write a Python function that checks whether a word or phrase is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, 
or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. 
Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.
'''
def palindrome(s):
    pass
# palindrome('helleh')
# True
'''
Hard:
Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

Hint: You may want to use .replace() method to get rid of spaces.
Hint: Look at the string module
Hint: In case you want to use set comparisons
'''
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    pass
# ispangram("The quick brown fox jumps over the lazy dog")
# True

# string.ascii_lowercase
# 'abcdefghijklmnopqrstuvwxyz'
