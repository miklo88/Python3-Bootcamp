#LEVEL ONE PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name. 
    # old_macdonald('macdonald') --> MacDonald
    #note: 'macdonald'.capitalize() returns 'Macdonald'
def old_macdonald(name):
    # #slice it up!
    # #declare the first letter in name
    # first_letter = name[0]
    # #declare the letters inbetween the first and fourth
    # inbetween = name[1:3]
    # #declare the fourth letter in name
    # fourth_letter = name[3]
    # #then there is everything else after the fourth letter. 
    # rest = name[4:]
    # return first_letter.upper() + inbetween + fourth_letter.upper() + rest
    
    #now the capitalize method allows us to do fewer slices.  
    #from the beginning to all the way to index three. 
    first_half = name[:3]
    #for second part is from 3 to the very end. 
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()

#check
print(old_macdonald('macdonald'))

## MASTER YODA: Given a sentence, return a sentence with the words reversed
    # master_yoda('I am home') --> 'home am I'
    # master_yoda('We are ready') --> 'ready are We'
def master_yoda(text):
    #using the split method. we create a variable worldlist for our wordlist and .split() method helps us create that
    worldlist = text.split()
    #ok so we have a list so we need to reverse it. indexing we're going to index from begging to end and calling the last item first!
    reverse_word_list = worldlist[::-1]
    #join method to make a list into a string. ' '.join(reverse_word_list)
    #so you pass the variable to the method. but you must add "" in front to tell the join what will be between each item in the list.
    return ' '.join(reverse_word_list)
#check  
print(master_yoda('I am home'))
#check
print(master_yoda('We are ready'))

#ALMOST THERE
#Given an integer n, return True if n is within 10 of either 100 or 200
    # almost_there(90) --> True
    # almost_there(104) --> True
    # almost_there(150) --> False
    # almost_there(209) --> True
# NOTE: abs(num) returns the absolute value of a number
def almost_there(n):
#shorthand
    #return (abs(100-n) <= 10) or (abs(200-n) <= 10):
    if (abs(100-n) <= 10):
        return True
    elif (abs(200-n) <= 10):
        return True
    else:
        return False
#check
print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
