'''
Lambda Expressions, Map and Filter - 
Lambda functions are basically anonymous functions. A one time use function
Built in functions of map and filter will be covered as well.
'''

def square(num):
    return num**2

my_nums = [1,2,3,4,5]
#applying the square function to every number in my list
#lets try the map function instead
#you pass in the function you want to map to the said list.
print(map(square,my_nums)) #returns <map object at 0x109ecc040>

#one way of using map
for item in map(square,my_nums):
    print(item)
#returns 
# 1
# 4
# 9
# 16
# 25

#to get the list back
print(list(map(square,my_nums))) #returns [1, 4, 9, 16, 25]

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer,names)))
#returns ['EVEN', 'E', 'S']

#returns either True or False
def check_even(num):
    return num%2 == 0
mynums = [1,2,3,4,5,6]
#only want to grab a specific type of numbers
print(list(filter(check_even,mynums)))
#returns [2, 4, 6]
for n in filter(check_even,mynums):
    print(n)
# 2
# 4
# 6

#LAMBDA FUNCTIONS
#start with normal function 
def square(num):
    result = num**2
    return result
print(square(3)) #returns 9
#now lets start turning it into a lambda function
#you can drop the result=num**2 and add it to return
def square(num):
    return num**2
print(square(4)) #returns 16
#now on one line
def square(num): return num**2
#now the magic 
lambda num: num**2
# but wait there is more.. you can assign it to a variable and then run that variable..
square = lambda num: num**2
print(square(8)) #returns 64

#now lets get  into it
#example function
print(list(map(lambda num:num**2,mynums))) #returns [1, 4, 9, 16, 25, 36]
print(list(filter(lambda num:num%2==0,mynums))) #returns [2, 4, 6]

#grabbing first character of a string
names = ['Andy', 'Eve', 'Sally']
print(list(map(lambda x:x[0],names)))#returns ['A', 'E', 'S']
#lets make one that reverses the strings
print(list(map(lambda x:x[::-1],names)))#returns ['ydnA', 'evE', 'yllaS']

