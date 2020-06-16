'''
Learning function increases your python skills
exponentially.
This also means that the difficulties of problems you can
solve will increase like crazy so have fun muchacho.
'''
#Function practice exercises
#Lesser of two evens
def lesser_of_two_evens(a,b):
    #if this statement happens to be true
    #if both numbers are even we need to return the lesser of the two
    if a%2==0 and b%2==0:
        # if a < b:
            # result = a
        # else:
            # result = b
        #min max method
        result = min(a,b)
         
    else:
        #one or both numbers are odd
        # if a > b:
            # result = a
        # else:
            # result = b
        #min max method
        result = max(a,b)
    return result

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

#ANIMAL CRACKERS
#write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False
def animal_crackers(text):
    #creating a variable where you can pull in the words in a string and create two strings. 
    wordlist = text.lower().split()
    print(wordlist)
#now lets make a list of two words
    first = wordlist[0]
    second = wordlist[1]
    return first[0] == second[0] #now we are seeing if they are equal to each other. hint the first letter will create a false statement.
#check1
print(animal_crackers('Levelheaded Llama'))
#check2
print(animal_crackers('Crazy Kangaroo'))

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
#makes_twenty(20, 10) -- True
#makes_twenty(12, 8) -- True
#makes_twenty(2, 3) -- False
def makes_twenty(n1,n2):
    # pass
    if n1 + n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False
    #or doing it all on one single line of code since this is all just boolean checks. we can pass it into a logical operator.
    # return (n1+n2) == 20 or n1==20 or n2==20
#check
# print(makes_twenty(20,10))
#check
# print(makes_twenty(2,3))
#check
print(makes_twenty(12,8))



