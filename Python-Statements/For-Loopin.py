'''
Many objects in Python are "iterable", meaning we can iterate 
over every element in the object.

Such as every element in a list or every character in a string.

We can use for loops to execute a block of code for every iteration.

The term ITERABLE means you can 'iterate' over the object.

For example you can iterate over every character in a string, iterate over every item in a list, 
iterate over every key in a dictionary.

Syntax of a for loop
my_iterable = [1,2,3]
for item_name in my_iterable:
    print(item_name)

'''
myname = ["Carl", "Redding"]
for fullname in myname:
    print(fullname)

mylist = [1,2,3,4,5,6,7,8,9,10]

#the variable name num can be whatever you want
# mylist is the list your iterating so it has to be the same.
for num in mylist:
    # print(num)
    #check for even
    if num % 2 == 0:
        print(f'Even Number: {num}')
    else:
        print(f'Odd Number: {num}')

list_sum = 0

for num in mylist:
    list_sum = list_sum + num

    print(list_sum) #returns the sum of every num up to 55. shows how important whitespace is.
# print(list_sum) # returns 55

mystring = "Bienvenidos"

for letter in mystring:
    print(letter)

# _ gives meaning to how unimportant it is to not have a specific name but here allows you to iterate hey multiple times
for _ in 'MIRA':
    print('Hey')

# TUPLE LOOPIN
#can do the same for a tuple
#be mindful this is tuple unpacking and is very common in python
tup = (1,2,3)
for item in tup:
    print(item)

mylist = [(1,2),(3,4),(5,6),(7,8),(9,10)]
print(len(mylist))
for (a,b) in mylist:
    print(f'Tuple A: {a}')
    print(f'Tuple B: {b}')

#you can also pass the mylist tuple to the for loop as item and just return
#each tuple itself, like (10,20,30),(40,50,60),(70,80,90)
mylist = [(10,20,30),(40,50,60),(70,80,90)]
for a,b,c in mylist:
    print(f'Unpack A: {a}')
    print(f'Unpack B: {b}')
    print(f'Unpack C: {c}')

# DICTIONARY LOOPIN
# for loops and iterating thru a dictionary
d = {'k1':'one','k2':'two','k3':'three'}
for key,value in d.items():
    print(key)
    print(value)
# if you just want to return the keys
for item in d.keys():
    print(item)
#if you just want to return the values
for item in d.values():
    print(item)

