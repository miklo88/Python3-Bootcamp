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
    # DOCSTRING: Information about the function
    # INPUT: name or whatever you're going to put in.
    # OUTPUT: Hello
    print("Hello")
#what you get back --->
# name_of_the_function() # you can pass in arguments to the function here!
# Hello #what we see when we invoke the function.

#now lets pass some parameters
def name_of_the_function(name):
    # Docstring explains function.
    # print("Hello" + name)
    print(f'Hello {name}')
print(name_of_the_function("Carlitos"))

'''
WHY RETURN AND PRINT?
Return - Typically we use the return keyword to send back the result of the function,
instead of just printing it out.
Return allows us to assign the output of the function to a new variable.

Print - Just print out the executed code. Think of console.log. 
'''
#example of return 
def add_function(num1,num2):
    return num1+num2
result = add_function(1,2)
print(result)
#anotha for ya mind.
def string_concatenate(str1,str2):
    return str1+str2
saying = string_concatenate('hi',' hello')
print(saying) # returns hi hello
print(len(saying)) # 8 
#and anotha
def funky_function():
    print('Keep it funky')
funky_function()

#adding parameters and arguments
def say_hello(name):
    print('hello' +name)
say_hello('funkyhomosapien')
#anotha way of doing it
# def say_hello(name='NAME'):
#     print('Hello ' +name)
# result = say_hello('Bob Ross')
#NOW HOLD ON. if you check the type of result you'll get the type
# print(type(result)) <class 'NoneType'>
#this is why we RETURN in the function :)
#anotha way of doing it
def say_hello(name):
    return(f'Hello ' +name)
result = say_hello('Bob Ross')
print(result)

# take in parameters. adhere logical operations and recieve solutions.
#mas practice
# find our if the word "dog" is in the string
def dog_check(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False

print(dog_check('My dog ran away')) # True
print(dog_check('My cat ran away')) # False
print(dog_check('Dog ran away')) # True
#this works but it can become apart of the DRY2020 campaign

def dog_check(mystring):
    return 'dog' in mystring.lower() #is cleaner because .lower() returns a boolean value
print(dog_check('Dog ran away')) #True

#PIG LATIN FUNCTION FUN - the skinny
# if word starts with a vowel, add 'ay' to end
# if word does not start with a vowel, put first letter at the end, then add 'ay'
# word --> ordway
# apple --> appleay
def pig_latin(word):

    first_letter = word[0]
    #check if vowel 
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

print(pig_latin('apple'))
print(pig_latin('cow'))
print(pig_latin('mouse'))






