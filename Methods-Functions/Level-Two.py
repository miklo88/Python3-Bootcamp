## LEVEL TWO PROBLEMS

# Find 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) -> True
# has_33([1, 3, 1, 3]) -> False
# has_33([3, 1, 3]) -> False

def has_33(nums):
    #here you are saying for i in the len of nums you are going all the way up 
    #to the second to last digit
    for i in range(0,len(nums)-1):
        #now this line checks the nums next to each other. 
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

#another way of chuncking slices and comparing
# def has_33(nums):
#     for i in range(0,len(nums)-1):]
##grabing slices of the list and comparing them
#         if nums[i:i+2] == [3,3]
#             return True

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#Paper Doll: Given a string, return a string where for every
# character in the original there are three characters
#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMiiissssssiiippppppiii'

def paper_doll(text):
    result = ''
#the trick is understanding you need an empty string to concatenate to.
#for character in text multiply the result times 3
    for char in text:
        result += char*3
    return result
#check
print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal
# to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum
# by 10. Finally if the sum (even after adjustment exceeds 21 return BUST)
#blackjack(5,6,7)
#blackjack(9,9,9)
#blackjack(9,9,11)

#thoughts- range(1,11) 
# if sum <= 21 return sum 
# elif sum > 21 and there is an 11 reduce 10 from sum
# if the sum > 21 return BUST 
def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        return sum([a,b,c])-10
    else:
        return 'Bust'
#check 
print(blackjack(5,6,7))
#check
print(blackjack(9,9,9))
#check
print(blackjack(9,9,11))

#SUMMER OF 69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9). Return 0 for no numbers.
#summer_69([1,3,5]) -->9
#summer_69([4,5,6,7,8,9]) -->9
#summer_69([2,1,6,9,11]) -->14
#check
print(summer_69([1,3,5]))
#check
print(summer_69([4,5,6,7,8,9]))
#check
print(summer_69([2,1,6,9,11]))
