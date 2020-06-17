'''
warm up for the milestone project
create a tic tac toe game!
- Grab user input
- Manipulate a variable based on input
- Return back adjusted variable
### TIC TAC TOES
STEPS 
1)creating an updated visual representation of what a user can see
then
2)user input
then 
3)function
then 
4)updates
then 
5)new visual
'''
#DISPLAY INFORMATION. three different lines of numbers. you can do it this way
# print([1,2,3])
# print([4,5,6])
# print([7,8,9])
# or create a function that allows you to print it out this way.
#three params row1, row2, row3
def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)
#declaring an example row.
row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
#printing the example row three times.
# display(row1,row2,row3)
#grabbing a spot and replace it with data
# row2[1] = 'X'
# display(row1,row2,row3)
#now we need to take a user input and be able to re-assign x and o's to the three lists.
'''
Accepting user input
'''
# input("Please enter a value: ")
#saving input. always returns a string. stores a string. using input you get a string muchacho.
result = int(input("Choose your square!: "))
#converting to an integer
result_int = print(result)





