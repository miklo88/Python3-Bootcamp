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
# # input("Please enter a value: ")
# #saving input. always returns a string. stores a string. using input you get a string muchacho.
# result = int(input("Choose your square!: "))
# #converting to an integer
# result_int = print(result)
'''
Validating user input.
implemented an input and converted its string input data type into another type such as an integer.
now further validating the user input to avoid errors for invalid conversions 
'''

#using while loop to check input 
def user_choice():
    #initial values we need to check
    choice = 'Incorrect choice' #if it is the correct input type
    accepted_values = range(0,10) #if the input is within our range
    within_range = False 
    #conditions to check.(2) digit or within range == false 
    #while choice is not a digit we keep asking for the correct digit.
    while choice.isdigit()==False or within_range==False:
        choice = input("Enter a number from 0-10: ")
        #digit check for data type
        if choice.isdigit() == False:
            print("That is not the correct digit ya goofball!")
        #range check for acceptable value
        if choice.isdigit() == True:
            if int(choice) in accepted_values:
                within_range = True
            else:
                print("Nope. You're outside of 0 to 10.")
                within_range = False
    return int(choice) 

print(user_choice())

