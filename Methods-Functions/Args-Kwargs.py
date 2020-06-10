'''
*args and **kwargs
Two functional parameters. 
Arguments - args
Keyword arguments - kwargs

'''
def myfunc(a,b):
    #returns 5% of the sum of a and b
    return sum((a,b)) * 0.05
print(myfunc(40,60)) #returns 5.0

#lets beef it up
def myfunc(a,b,c=0,d=0,e=0):
    #returns 5% of the sum of a and b
    return sum((a,b,c,d,e)) * 0.05
print(myfunc(40,60,100,200,500))
#you eventually hit a limit of what you can pass it. another number here would return error like so.
# Traceback (most recent call last):
#   File "Args-Kwargs.py", line 17, in <module>
#     print(myfunc(40,60,100,200,500,60))
# TypeError: myfunc() takes from 2 to 5 positional arguments but 6 were given

#cleaner with args and you can pass in as many arguments as you want.
#this will return a tuple
#args can be any word you like. its common convention to call it args so don't be that guy.
def myfunc(*args):
    return sum(args) * 0.05
print(myfunc(40,50,60,40,50,90,70,80,30))

#this is best to work with dictionaries. bc the data type you'll be getting back is such.
#this returns a dictionary.
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    elif 'veggie' in kwargs:
        print('My veggie of choice is {}'.format(kwargs['veggie']))
    else:
        print('Did not find either or here')
myfunc(fruit='fruit')
myfunc(veggie='carrots')

#now lets combine the two
def myfunc(*args,**kwargs):
    
    print('I would like {} {}'.format(args[0],kwargs['fruit']))
myfunc(10,20,30, fruit='bananas', color='blue')
#now be mindful that you have to pass the arguments as they are passed into the function
#arguments first then keyword  arguments after. args then kwargs. no kwargs then args or 
#args kwargs args ya dig?