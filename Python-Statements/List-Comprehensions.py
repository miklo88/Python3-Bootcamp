'''
List Comprehension - 
Are a unique way of quickly creating a list with Python.
If you find yourself using a for loop along with .append() to create
a list, List Comprehensions are a good alternative!

Basically a flattened out for loop
'''

mystring = 'hello'

mylist = []
for letter in mystring:
    mylist.append(letter)

print(mylist)
#returns ['h', 'e', 'l', 'l', 'o']

mylist = [letter for letter in 'asdfghjkl']
print(mylist)

mylist = [num for num in range(0,20)]
print(mylist)

mylist = [num**2 for num in range(0,10)]
print(mylist)

mylist = [x for x in range(0,10) if x%2==0]
print(mylist)

celcius = [0,10,20,34.5]
fahrenheit = [( (9/5)*temp + 32) for temp in celcius]
print(fahrenheit) #returns [32.0, 50.0, 68.0, 94.1] #so much cleaner :)

#example in for loop to see the diff and similarities
fahrenheit = []
for temp in celcius:
    fahrenheit.append(( (9/5)*temp + 32))
print(fahrenheit) #returns [32.0, 50.0, 68.0, 94.1]

#if else statements in a list comprehension
#be mindful of readability. longhand is easier to comprehend down the road.
results = [x if x%2==0 else 'ODD' for x in range(0,12)]
print(results)

# #what we are doing here is taking a list of nums 2,4,6 and multiplying it by 
mylist = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
print(mylist)

#using list comprehension sacraficing readability.
mylist = [x*y for x in [2,4,6] for y in [1, 10, 1000]]

