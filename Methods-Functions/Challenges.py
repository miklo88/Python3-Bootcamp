#Challenge Problems

#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 
#007 in order
# spy_game([1,2,4,0,0,7,5]) True
# spy_game([1,0,2,4,0,5,7]) True
# spy_game([1,7,2,0,4,5,0]) False

def spy_game(nums):
    # so if the list has 0 0 7 in sequential or nonsequential order we return true
    # if not we return false
    # you must check your list for 007. and if it occurs in that order in your list
    code = [0,0,7,'x']
    for num in nums:
        #i want to check if two zeros show up before a seven
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to 
# and including a given number.
#By convention we'll treat 0 and 1 as not prime.
def count_primes(nums):
    #check for 0 or 1 input
    if nums < 2:
        return 0
######################## check 2 or greater
#store our prime numbers
    primes = [2]
#counter going up to input num
    x = 3 
#x is going thru every number up to the input number
    while x <= nums:
    #check if x is prime
        # for y in range(3,x,2):
        for y in primes:
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
# print(primes)
    return len(primes)
print(count_primes(10))
# def count_prime(x):
#     if x <= 1:
#         return False
#     elif x == 2:
#         return true
#     else: 
#         for n in range(2, x):
#             if x % n == 0:
#                 return False
#         return True

# print(count_prime(11))
'''
return prime numbers up to the parameter
need division to check if every number is a prime number. so if it is divisible by no more than itself or 1
need a list to store prime numbers in
need to read a list or range of numbers
so your check is if it divides by 1 or iteself. any other number that it can means its not prime.

'''