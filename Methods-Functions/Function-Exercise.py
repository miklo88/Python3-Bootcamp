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