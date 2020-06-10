'''
Methods and Functions
Built in objects in Python have a variety of methods you can use!
Let's explore in a bit more detail how to find methods and how to get information about them.
'''

mylist = [1,2,3,4,5,6,7,8,9,10]

#methods we are familiar with. 
# mylist.append()
# mylist.pop()

#how to discover methods on your own.
# use that help() function to describe what method you're using
# help(mylist.insert)

'''
sources
https://www.learnpython.org/en/Functions
'''
'''
Functions -
Creating clean repeatable code is a key part of becoming an effective
programmer.
Functions allow us to create blocks of code that can be easily executed many times, without needing to constantly 
rewrite the entire block of code.
'''
#exploring syntax
#always going to start with def and always lowercase with snakecase _ _ :) 
def name_of_the_function():
    # Docstring explains function.
    print("Hello")
#what you get back
# name_of_the_function()
# Hello

#now lets pass some parameters
def name_of_the_function(name):
    # Docstring explains function.
    print("Hello" + name)
print(name_of_the_function("Carlitos"))
