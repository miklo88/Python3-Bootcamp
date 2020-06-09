'''
The basics of a couple useful functions that come built in with python.
Also operator keywords that are important and don't really fit in anything
else we've covered this far.
'''
mylist = [1,2,3]
for num in range(10):
    print(num)
#returns 0,1,2,3,4,5,6,7,8,9 hint because you stated in the range of 10
#can initiate a starting int and a step size
# so start is 3, range of 10 and step size of 2
for num in range(3,10,2):
    print(num)

print(list(range(0,12,2)))

#Enumerate function. it can take in any iterable function and returns back an index counter and the object itself
index_count = 0 
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

#Enumerate function. it can take in any iterable function and returns back an index counter and the object itself
word = 'abcde'
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

# ZIP function - zips together these two lists and pairs them up by item
# unpacking tuples is huge because you'll be doing it a lot in python because most functions
# return tuples!
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for item in zip(mylist1, mylist2, mylist3):
    print(item)

print(list(zip(mylist1,mylist2)))

#IN operator
print('x' in [1,2,3]) #False 
print('x' in ['x','y','z']) #True
print('key1' in {'key1':123})#True

d = {'key1':456}
print(456 in d.keys())#False
#  MIN MAX FUNCTIONS
MYLIST = [10,20,30,40,50,60]
min(MYLIST)
max(MYLIST)

#SHUFFLE FUNCTION
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
random_list = shuffle(mylist)
print(type(random_list)) #<class 'NoneType'>
print(mylist) # returns a shuffled list

from random import randint
print(randint(0,100)) # returns a random number
#can save those random numbers
mynum = randint(0,50)
print(mynum)

#input function - always accepts whatever is put into it as a string
input('Enter a number here: ')

nameresult = input('What is your name? ')
print(nameresult)

intresult = input('Favorite Number: ')
print(int(intresult))
print(float(intresult))