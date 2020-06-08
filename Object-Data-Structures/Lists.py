'''
Lists in Python
Lists are ordered sequences that can hold a variety of object types.
They use [] brackets and commas to separate objects in the list.
ex [1,2,3.4.5]

Lists support indexing and slicing. Lists can be nested and also have a variety of useful methods that can be called off of them.
'''
# with a string, ints and a float in a list
# the giveaway here is the [] brackets
my_list = ["List", 1, 2, 3, 5.21]
print(my_list)
print(len(my_list))

#slicing and indexing
mylist = ["one", "two", "three"]
print(mylist[1:]) # returns ['two', 'three']
print(mylist[:2]) # returns ['one', 'two']
print(mylist[::]) # returns ['one', 'two', 'three']
print(mylist[::-1]) # returns ['three', 'two', 'one']

otherlist = ["four", "five"]
newlist = mylist + otherlist
print(newlist)

newlist[0] = "One"
print(newlist)
# ['One', 'two', 'three', 'four', 'five']
#append allows you to place a new item on the list and changes the list
newlist.append("six")
newlist.append("seven")
print(newlist)

#pop 
newlist.pop()
#getting sneaky and saving the items that have been popped off of the list
poppeditem = newlist.pop() #six will be the number for the poppeditem variable
print(newlist)
print(poppeditem)
# seven gets popped off of the list. it returns the item popped off of the list.
#popping a specific item off of the list meow. just pass in an index number
newlist.pop(3) #should get rid of four and return that. remember indexing starts at 0
print(newlist)

#goofin with a new lists that are out of order
goofin = ['l','k','j','h','g','f','d','s','a']
goofinnoms = ['1','3','6','5','8','7','8','9','2']
#sortinggggg
goofin.sort()
print(goofin)
# returns - ['a', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 's']
#newb mistake is this
#newsortedgoofin = goofin.sort()
#this wont work because sort wont return anything to be assigned to newsortedgoofin
#lets do it again with goofinnoms
goofinnoms.sort()
print(goofinnoms)
# returns - ['1', '2', '3', '5', '6', '7', '8', '8', '9']
#does exactly what it says. reverses the list.
goofin.reverse()
goofinnoms.reverse()
print(goofin)
print(goofinnoms)
#sneaky way of reversing a string with indexing.
sneakylist = [1,2,3,4,5,6,7,8,9,10]
print(sneakylist[::-1])


